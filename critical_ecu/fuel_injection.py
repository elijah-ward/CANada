import can

class FuelInjection:

	def __init__(self):
		self.gas = 0.0
		self.filters = [{
			"can_id": 0x4,
			"can_mask": 0x12345
		}]

	def listen(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		bus.set_filters(self.filters)

		# iterate over received messages
		for msg in bus:
		    print("FUEL - {}: {}".format(msg.arbitration_id, msg.data))

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
