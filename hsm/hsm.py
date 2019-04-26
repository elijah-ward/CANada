import can
import time
from config import Config

class HSM:

	def __init__(self, security_module, journal):
		self.security_module = security_module
		self.journal = journal

	def start(self, stop_event):
		critical_bus = can.Bus(interface='virtual',
    		channel='vcan0')

		non_critical_bus = can.Bus(interface='virtual',
    		channel='vcan1')

		crit_listener = self.security_module(Config.general['channels']['critical_bus'], self.journal)
		non_crit_listener = self.security_module(Config.general['channels']['non_critical_bus'], self.journal)

		# asynchronous notifier
		crit_notifier = can.Notifier(critical_bus, [crit_listener])
		non_crit_notifier = can.Notifier(non_critical_bus, [non_crit_listener])

		while True:
			if stop_event.is_set():
				critical_bus.shutdown()
				non_critical_bus.shutdown()
				crit_notifier.stop()
				non_crit_notifier.stop()
				crit_listener.stop()
				non_crit_listener.stop()
				break
