import can
import time
from config import Config
from messages.message_factory import Message

'''
The following class represents an example where an adversary has added an external node to listen to messages sent over the network and replays them
'''

class ExternalNode:

	def __init__(self, journal):
		self.bus = can.Bus(interface='virtual', channel='vcan1')
		self.journal = journal

	def start(self, stop_event):

		# Normally this message would be stolen off of the bus and then replayed, but for sake of demo we'll use a message with a random key
		hostile_message = Message(target_component='fuel', data=[0x66, 0x66, 0x66])
		time.sleep(Config.adversaries['external_node']['start_delay'])

		while True:
			self.bus.send(hostile_message)
			self.journal.incr_hostile()
			time.sleep(Config.adversaries['ddos_infotainment']['injection_delay'])

			if stop_event.is_set():
				self.bus.shutdown()
				break

