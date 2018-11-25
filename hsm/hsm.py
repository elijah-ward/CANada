import can
import time
from config import Config
from hsm.frequency_analyzer import FrequencyAnalyzer

class HSM:

	def __init__(self):
		self.frequencies = { v['id'] : 0 for k,v in Config.components.items() }
		# self.algorithm = FrequencyAnalyzer

	def relay_message(message, target):
		target.send(message)

	def start(self):
		critical_bus = can.Bus(interface='virtual',
    		channel='vcan0')

		non_critical_bus = can.Bus(interface='virtual',
    		channel='vcan1')

		listener = FrequencyAnalyzer()


		# or use an asynchronous notifier
		crit_notifier = can.Notifier(critical_bus, [listener])
		non_crit_notifier = can.Notifier(non_critical_bus, [listener])
