import can
from utils.better_printer import BetterPrinter

class Brakes:

	def __init__(self):
		self.pressure = 0.0
		self.filters = [{
			"can_id": 0x1,
			"can_mask": 0x12345
		}]

	def start(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		bus.set_filters(self.filters)
		
		# asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), BetterPrinter()])
