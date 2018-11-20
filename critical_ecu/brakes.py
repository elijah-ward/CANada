import can

class Brakes:

	def __init__(self):
		self.pressure = 0.0
		self.filters = [{
			"can_id": 0x1,
			"can_mask": 0x12345
		}]

	def listen(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		bus.set_filters(self.filters)

		# iterate over received messages
		for msg in bus:
		    print("BRAKES - {}: {}".format(msg.arbitration_id, msg.data))

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
