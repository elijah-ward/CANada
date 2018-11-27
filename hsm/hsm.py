import can
import time
from config import Config

class HSM:

	def __init__(self, security_module):
		self.security_module = security_module

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
