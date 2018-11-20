# import the library
import can
import threading
from hsm.hsm import HSM
from critical_ecu.fuel_injection import FuelInjection
from critical_ecu.brakes import Brakes
from critical_ecu.steering import Steering
from non_critical_ecu.infotainment import Infotainment
from non_critical_ecu.climate_control import ClimateControl
from driver_control import DriverControl


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
		# hsm = HSM()

		modules = [fuel,brakes,steering,infotainment,climate_control, driver_controls]

		threads = []

		for mod in modules:		
		    t = threading.Thread(target=mod.start)
		    threads.append(t)
		    t.start()

		while True:
			continue