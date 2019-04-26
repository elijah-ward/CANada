import time
import can
from termcolor import colored
from can.listener import Listener
from config import Config
import pprint

class FrequencyAnalyzer(Listener):

	def __init__(self, channel, journal):
		self.channel = channel
		self.traffic = { v['id'] : { 'last_timestamp': None, 'count': 0, 'cumulative_interval': 0.0 ,'avg_interval': 0.0 } for k,v in Config.components.items() }
		self.intervals = { v['id'] : { 'last_timestamp': None } for k,v in Config.components.items() }
		self.training_end = time.time() + Config.frequency_analyzer['seconds_training_time']
		self.allowed_variance = Config.frequency_analyzer['allowed_variance']
		self.journal = journal

		# Outward bus, target channel is vcan0 if this listener is receiving on vcan1 and vice-versa
		self.outbound_channel = 'vcan1' if channel == 'vcan0' else 'vcan0'
		self.outbound_bus = can.Bus(interface='virtual', channel=self.outbound_channel)
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

		print(colored('Detecting: Adjusting normal range for message with id of {}. Training time remaining: {}s.'.format(msg_id, int(self.training_end - time.time())), 'yellow'))

	def enforce_range(self, msg):

		msg_id = msg.arbitration_id

		if self.intervals[msg_id]['last_timestamp'] == None:
			self.intervals[msg_id]['last_timestamp'] = msg.timestamp
		else:
			current_timestamp = msg.timestamp
			prior_timestamp = self.intervals[msg_id]['last_timestamp']
			current_interval = current_timestamp - prior_timestamp
			threshold = self.traffic[msg_id]['avg_interval'] - self.allowed_variance

			self.intervals[msg_id]['last_timestamp'] = current_timestamp

			if current_interval < threshold:
				print(colored('\nIRREGULAR MESSAGE FREQUENCY - BLOCKING MESSAGE\navg_interval - {}, current_interval - {}, last_timestamp: {}\n'
					.format(threshold, current_interval, prior_timestamp), 'red'), colored('{}\n'.format(msg), 'red'))
				if bytes(msg.data)[0] == 102:
					self.journal.incr_hostile_blocked()
				else :
					self.journal.incr_innocent_blocked()
			else:
				print(colored('\nReceived Inter-Bus Message... Relaying:\navg_interval - {}, current_interval - {}, last_timestamp: {}\n'
					.format(threshold, current_interval, prior_timestamp), 'green'), colored(msg, 'green'))
				self.outbound_bus.send(msg)

				if bytes(msg.data)[0] == 102:
					self.journal.incr_hostile_forwarded()
				else :
					self.journal.incr_innocent_forwarded()

	def on_message_received(self, msg):

		msg_id = msg.arbitration_id

		if time.time() < self.training_end:
			self.detect_normal_range(msg)
		elif Config.components[Config.id_assignment[msg_id]]['can_channel'] != self.channel:
			self.enforce_range(msg)



