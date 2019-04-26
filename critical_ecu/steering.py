import can
from utils.better_printer import BetterPrinter

class Steering:

	def __init__(self):
		self.pitch = 0.5
		self.filters = [{
			"can_id": 0x5,
			"can_mask": 0x12345
		}]

	def start(self, stop_event):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		bus.set_filters(self.filters)

		# asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), BetterPrinter()])

		while True:
			if stop_event.is_set():
				notifier.stop()
				bus.shutdown()
				break