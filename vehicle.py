# import the library
import can
import threading
from critical_ecu.engine import Engine
from critical_ecu.brakes import Brakes
from critical_ecu.steering import Steering
from non_critical_ecu.infotainment import Infotainment


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

		bus.send_periodic(message, period=1.0)

		eng = Engine()
		brakes = Brakes()
		steering = Steering()
		infotainment = Infotainment()

		modules = [eng, brakes, steering, infotainment]

		threads = []

		for mod in modules:		
		    t = threading.Thread(target=mod.listen)
		    threads.append(t)
		    t.start()