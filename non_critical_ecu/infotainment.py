import can

class Infotainment:

	def __init__(self):
		self.volume = 0.0
		self.mode = 'menu'
		self.brightness = 0.5

	def listen(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan0')

		# iterate over received messages
		for msg in bus:
		    print("INFOTAINMENT - {}: {}".format(msg.arbitration_id, msg.data))

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
