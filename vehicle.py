# import the library
import can
import threading
from hsm.hsm import HSM

# critical ECUs
from critical_ecu.fuel_injection import FuelInjection
from critical_ecu.brakes import Brakes
from critical_ecu.steering import Steering

# non-critical ECUs
from non_critical_ecu.infotainment import Infotainment
from non_critical_ecu.climate_control import ClimateControl

# driver behaviour simulator
from driver_control import DriverControl

# ddos injection adversary
from adversaries.ddos_infotainment import DDOSInfotainment
from adversaries.external_node import ExternalNode


class Vehicle:

	def __init__(self):
		self.speed = 0
		self.pitch = 0

	def ignition(self):

		# Listeners
		fuel = FuelInjection()
		brakes = Brakes()
		steering = Steering()
		infotainment = Infotainment()
		climate_control = ClimateControl()

		# Dispatchers
		driver_controls = DriverControl()

		# Hardware Security Module
		hsm = HSM()

		# Adversaries
		# adversary = DDOSInfotainment()
		adversary = ExternalNode()

		modules = [fuel,brakes,steering,infotainment,climate_control, driver_controls, hsm, adversary]

		threads = []

		for mod in modules:		
		    t = threading.Thread(target=mod.start)
		    threads.append(t)
		    t.start()

		while True:
			continue