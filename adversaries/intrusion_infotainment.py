import can
import time
from config import Config
from messages.message_factory import Message
from hsm.intrusion_detection import ECUMonitor

'''
The following class represents an example where an adversary has gained control over the infotainment unit
and uses it to flood messages onto the bus
'''

class IntrusionInfotainment:

	def __init__(self, journal):
		self.is_malicious = False
		self.bus = can.Bus(interface='virtual', channel='vcan1')
		self.monitor_hsm = ECUMonitor()
		self.journal = journal

	def start(self):
		start_time = time.time()

		while True:
			self.monitor_hsm.scan(self.is_malicious, self.bus)	
			current_time = time.time()
			if ( current_time - start_time ) >= Config.intrusion_detection['start_delay']:
				self.is_malicious = True

			time.sleep(Config.intrusion_detection['scan_delay'])


