# import the library
import can
import threading
import time
import sys
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


class Vehicle:

	def __init__(self, adversary, security_module, journal):
		self.adversary = adversary
		self.security_module = security_module
		self.journal = journal

	def ignition(self, duration):

		# Listeners
		fuel = FuelInjection()
		brakes = Brakes()
		steering = Steering()
		infotainment = Infotainment()
		climate_control = ClimateControl()

		# Dispatchers
		driver_controls = DriverControl(self.journal)

		# Hardware Security Module
		hsm = HSM(self.security_module, self.journal)

		# Adversaries
		adversary = self.adversary(self.journal)

		modules = [fuel,brakes,steering,infotainment,climate_control, driver_controls, hsm, adversary]

		threads = []

		start_time = time.time()
		stop_event = threading.Event()
		print('Start Time: {}'. format(start_time))
		for mod in modules:		
		    t = threading.Thread(target=mod.start, args=(stop_event,))
		    threads.append(t)
		    t.start()

		while True:
			elapsed_time = time.time() - start_time
			if elapsed_time >= duration:
				stop_event.set()
				break

		for t in threads:
			t.join()