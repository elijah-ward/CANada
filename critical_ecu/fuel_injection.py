import can
from utils.mask_helper import MaskHelper

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

		mh = MaskHelper()
		mh.check_match(100, self.filters[0]["can_id"], self.filters[0]["can_mask"])

		# or use an asynchronous notifier
		notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
