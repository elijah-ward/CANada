import can

class FuelInjection:

	def __init__(self):
		self.gas = 0.0

	def listen(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		# iterate over received messages
		for msg in bus:
		    print("FUEL INJECTION - {}: {}".format(msg.arbitration_id, msg.data))

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
