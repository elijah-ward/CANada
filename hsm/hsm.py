import can
import time
from config import Config
from hsm.frequency_analyzer import FrequencyAnalyzer
from hsm.authentication import Authentication

class HSM:

	def __init__(self):
		self.security_module = Authentication

	def relay_message(message, target):
		target.send(message)

	def start(self):
		critical_bus = can.Bus(interface='virtual',
    		channel='vcan0')

		non_critical_bus = can.Bus(interface='virtual',
    		channel='vcan1')

		crit_listener = self.security_module(Config.general['channels']['critical_bus'])
		non_crit_listener = self.security_module(Config.general['channels']['non_critical_bus'])

		# asynchronous notifier
		crit_notifier = can.Notifier(critical_bus, [crit_listener])
		non_crit_notifier = can.Notifier(non_critical_bus, [non_crit_listener])
