import can

class FuelInjection:

	def __init__(self):
		self.gas = 0.0
		self.filters = [{
			"can_id": 0xA0,
			"can_mask": 0x21
		}]

	def listen(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
