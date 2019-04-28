import time
import random
import can
from termcolor import colored
from config import Config

class ECUMonitor:

	def __init__(self, journal):
		self.detection_rate = Config.intrusion_detection['detection_rate']
		self.journal = journal
		self.containment_mode = False

	def scan(self, malicious_state, bus):
		threat_detected = False
		print(colored('ECU monitor scanning for threats...', 'yellow'))

		if malicious_state:
			detection_roll = random.random()
			if detection_roll <= self.detection_rate:
				threat_detected = True
				print(colored('INTRUSION DETECTED, ISOLATING NON-CRITICAL ECU', 'red'))
				self.containment_mode = True
				bus.shutdown()
		if not threat_detected:
			print(colored('No threats detected... hibernating.', 'yellow'))




