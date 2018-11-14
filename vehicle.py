# import the library
import can
from ecu.engine import Engine
from ecu.brakes import Brakes
from ecu.infotainment import Infotainment
from ecu.steering import Steering

class Vehicle:

	def __init__(self):
		self.speed = 0
		self.pitch = 0

	def ignition(self):

		# create a bus instance
		# many other interfaces are supported as well (see below)
		bus = can.Bus(interface='virtual',
		              channel='vcan0')

		# send a message
		message = can.Message(arbitration_id=123, extended_id=True,
		                      data=[0x11, 0x22, 0x33])

		bus.send_periodic(message, period=0.25)

		eng = Engine()
		brakes = Brakes()
		steering = Steering()
		infotainment = Infotainment()

		eng.listen()
		brakes.listen()
		steering.listen()
		infotainment.listen()