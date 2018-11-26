import can

class ClimateControl:

	def __init__(self):
		self.volume = 0.0
		self.mode = 'menu'
		self.brightness = 0.5
		self.filters = [{
			"can_id": 0x41,
			"can_mask": 0x12345
		}]

	def start(self):
		bus = can.Bus(interface='virtual',
    		channel='vcan1')

		bus.set_filters(self.filters)

		# iterate over received messages
		# for msg in bus:
		#     print("CLIMATE CONTROL - {}: {}".format(msg.arbitration_id, msg.data))

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
