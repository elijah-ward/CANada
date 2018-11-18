# import the library
import can
import threading
from critical_ecu.engine import Engine
from critical_ecu.brakes import Brakes
from critical_ecu.steering import Steering
from non_critical_ecu.infotainment import Infotainment
from non_critical_ecu.climate_control import ClimateControl


class Vehicle:

	def __init__(self):
		self.speed = 0
		self.pitch = 0

	def ignition(self):

		# Virtual bus instances

		# Initialize bus for critical ECU components, identified by vcan0
		critical_bus = can.Bus(interface='virtual',
		              channel='vcan0')

		# Initialize bus for non-critical ECU components, identified by vcan1
		non_critical_bus = can.Bus(interface='virtual',
		              channel='vcan1')

		# send a message
		message = can.Message(arbitration_id=123, extended_id=True,
		                      data=[0x11, 0x22, 0x33])

		critical_bus.send_periodic(message, period=1.0)
		non_critical_bus.send_periodic(message, period=1.0)

		eng = Engine()
		brakes = Brakes()
		steering = Steering()
		infotainment = Infotainment()
		climate_control = ClimateControl()

		modules = [eng, brakes, steering, infotainment, climate_control]

		threads = []

		for mod in modules:		
		    t = threading.Thread(target=mod.listen)
		    threads.append(t)
		    t.start()