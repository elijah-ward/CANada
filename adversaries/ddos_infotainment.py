import can
import time
from config import Config
from messages.message_factory import Message

'''
The following class represents an example where an adversary has gained control over the infotainment unit
and uses it to flood messages onto the bus
'''

class DDOSInfotainment:

	def __init__(self, journal):
		self.bus = can.Bus(interface='virtual', channel='vcan1')
		self.journal = journal

	def start(self, stop_event):

		time.sleep(Config.adversaries['ddos_infotainment']['start_delay'])

		while True:
			hostile_message = Message(target_component='fuel', data=[0x66, 0x66, 0x66])
			self.bus.send(hostile_message)
			self.journal.incr_hostile()
			time.sleep(Config.adversaries['ddos_infotainment']['injection_delay'])

			if stop_event.is_set():
				self.bus.shutdown()
				break

