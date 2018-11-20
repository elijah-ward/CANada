# import the library
import can
import threading
from hsm.hsm import HSM
from critical_ecu.fuel_injection import FuelInjection
from critical_ecu.brakes import Brakes
from critical_ecu.steering import Steering
from non_critical_ecu.infotainment import Infotainment
from non_critical_ecu.climate_control import ClimateControl


class Vehicle:

	def __init__(self):
		self.speed = 0
		self.pitch = 0

	def ignition(self):

		#########################
		# Virtual bus instances #
		#########################

		# Initialize bus for critical ECU components, identified by vcan0
		critical_bus = can.Bus(interface='virtual',
		              channel='vcan0')

		# Initialize bus for non-critical ECU components, identified by vcan1
		non_critical_bus = can.Bus(interface='virtual',
		              channel='vcan1')

		################################################
		# Messages Addressed to Various Critical Nodes #
		################################################

		# message with id for the brakes ecu
		brake_message = can.Message(arbitration_id=1, extended_id=True,
		                      data=[0x11, 0x11, 0x11])

		# message with id for the brakes ecu
		fuel_message = can.Message(arbitration_id=4, extended_id=True,
		                      data=[0x44, 0x44, 0x44])

		# message with id for the steering ecu
		steering_message = can.Message(arbitration_id=5, extended_id=True,
		                      data=[0x55, 0x55, 0x55])

		####################################################
		# Messages Addressed to Various Non-Critical Nodes #
		####################################################

		# message with id for the infotainment ecu
		infotainment_message = can.Message(arbitration_id=64, extended_id=True,
		                      data=[0x64, 0x64, 0x64])

		# message with id for the climate control ecu
		climate_message = can.Message(arbitration_id=65, extended_id=True,
		                      data=[0x65, 0x65, 0x65])


		critical_bus.send_periodic(brake_message, period=1.0)
		critical_bus.send_periodic(fuel_message, period=1.0)
		critical_bus.send_periodic(steering_message, period=1.0)

		non_critical_bus.send_periodic(infotainment_message, period=1.0)
		non_critical_bus.send_periodic(climate_message, period=1.0)

		fuel = FuelInjection()
		brakes = Brakes()
		steering = Steering()
		infotainment = Infotainment()
		climate_control = ClimateControl()

		# hsm = HSM()

		modules = [fuel,brakes,steering,infotainment,climate_control]

		threads = []

		for mod in modules:		
		    t = threading.Thread(target=mod.listen)
		    threads.append(t)
		    t.start()

		while True:
			continue