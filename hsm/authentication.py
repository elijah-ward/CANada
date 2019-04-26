import time
import can
from termcolor import colored
from can.listener import Listener
from config import Config
import pprint

class Authentication(Listener):

	def __init__(self, channel, journal):
		self.channel = channel

		# Outward bus, target channel is vcan0 if this listener is receiving on vcan1 and vice-versa
		self.outbound_channel = 'vcan1' if channel == 'vcan0' else 'vcan0'
		self.outbound_bus = can.Bus(interface='virtual', channel=self.outbound_channel)
		self.printer = pprint.PrettyPrinter(indent=4)
		self.journal = journal

	def verify_signature(self, msg):
		msg_time = str(msg.timestamp)
		msg_seconds = msg_time.split('.')[0]
		lsd = int(msg_seconds[len(msg_seconds)-1])
		data = msg.data
		msg_sig_bytes = data[Config.message_structure['signature']['start_byte']:]
		msg_sig = msg_sig_bytes.decode('utf-8')

		return Config.identity_keys[lsd] == msg_sig

	def enforce_auth(self, msg):

		if self.verify_signature(msg):
			print(colored('\nRECEIVED INTER-BUS MESSAGE WITH CORRECT KEY... Relaying:\n','green'), colored(msg, 'green'))
			self.outbound_bus.send(msg)
		else:
			print(colored('\nINCORRECT KEY - BLOCKING MESSAGE\n', 'red'), colored('{}\n'.format(msg), 'red'))

	def on_message_received(self, msg):

		msg_id = msg.arbitration_id

		if Config.components[Config.id_assignment[msg_id]]['can_channel'] != self.channel:
			self.enforce_auth(msg)



