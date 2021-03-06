import can
import random
import time
from config import Config
from messages.message_factory import Message
from utils.better_printer import BetterPrinter

class Infotainment:

	def __init__(self):
		self.volume = 0.0
		self.mode = 'menu'
		self.brightness = 0.5
		self.filters = [{
			"can_id": 0x40,
			"can_mask": 0x12345
		}]
		self.bus = can.Bus(interface='virtual', channel='vcan1')
		self.diagnostic_delay_factor = Config.components['infotainment']['diagnostic_delay_factor']

	def request_fuel_diagnostic(self):
		fuel_message = Message(target_component='fuel', data=[0x22, 0x22, 0x22])
		self.bus.send(fuel_message)

	def start(self, stop_event):

		self.bus.set_filters(self.filters)

		# asynchronous notifier
		notifier = can.Notifier(self.bus, [can.Logger("recorded.log"), BetterPrinter()])

		while True:

			if stop_event.is_set():
				notifier.stop()
				self.bus.shutdown()
				break

			self.request_fuel_diagnostic()
			time.sleep(self.diagnostic_delay_factor)

