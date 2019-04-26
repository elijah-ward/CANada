import time
import can
from termcolor import colored
from can.listener import Listener
from config import Config

class Noop(Listener):

	def __init__(self, channel, journal):
		self.channel = channel

		# Outward bus, target channel is vcan0 if this listener is receiving on vcan1 and vice-versa
		self.outbound_channel = 'vcan1' if channel == 'vcan0' else 'vcan0'
		self.outbound_bus = can.Bus(interface='virtual', channel=self.outbound_channel)
		self.journal = journal

	def relay(self, msg):

		print(colored('\nRECEIVED INTER-BUS MESSAGE... Relaying:\n','green'), colored(msg, 'green'))
		self.outbound_bus.send(msg)

	def on_message_received(self, msg):

		msg_id = msg.arbitration_id

		if Config.components[Config.id_assignment[msg_id]]['can_channel'] != self.channel:
			self.relay(msg)



