import time
from can.listener import Listener
from config import Config
import pprint

class FrequencyAnalyzer(Listener):

	def __init__(self):
		self.traffic = { v['id'] : { 'last_timestamp': None, 'count': 0, 'cumulative_interval': 0.0 ,'avg_interval': 0.0 } for k,v in Config.components.items() }
		self.intervals = { v['id'] : { 'last_timestamp': None } for k,v in Config.components.items() }
		self.messages_received = 0
		self.allowed_variance = Config.frequency_analyzer['allowed_variance']
		self.printer = pprint.PrettyPrinter(indent=4)

	def detect_normal_range(self, msg):

		msg_id = msg.arbitration_id
		self.traffic[msg_id]['count'] += 1

		if self.traffic[msg_id]['last_timestamp'] == None:
			self.traffic[msg_id]['last_timestamp'] = msg.timestamp
		else:
			current_timestamp = msg.timestamp
			prior_timestamp = self.traffic[msg_id]['last_timestamp']
			current_interval = current_timestamp - prior_timestamp

			self.traffic[msg_id]['cumulative_interval'] += current_interval
			self.traffic[msg_id]['avg_interval'] = self.traffic[msg_id]['cumulative_interval'] / self.traffic[msg_id]['count']
			self.traffic[msg_id]['last_timestamp'] = current_timestamp

		print('Detecting: Adjusting normal range for message with id of {}. Count is {}.'.format(msg_id, self.messages_received))

	def enforce_range(self, msg):

		msg_id = msg.arbitration_id

		if self.intervals[msg_id]['last_timestamp'] == None:
			self.intervals[msg_id]['last_timestamp'] = msg.timestamp
		else:
			current_timestamp = msg.timestamp
			prior_timestamp = self.intervals[msg_id]['last_timestamp']
			current_interval = current_timestamp - prior_timestamp
			threshold = self.traffic[msg_id]['avg_interval'] + self.allowed_variance

			self.intervals[msg_id]['last_timestamp'] = current_timestamp

			if current_interval > threshold:
				print('\nREEEEEEEEEEEEEEEEEEE: avg - {}, current - {}, last_time: {}\n'.format(threshold, current_interval, prior_timestamp))




	def on_message_received(self, msg):

		self.messages_received += 1

		if self.messages_received < Config.frequency_analyzer['training_set_size']:
			self.detect_normal_range(msg)
		else:
			self.enforce_range(msg)



