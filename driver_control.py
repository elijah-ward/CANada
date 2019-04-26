import can
import random
import time
from config import Config
from messages.message_factory import Message

class DriverControl:

	def __init__(self, journal):

		# Longest time in seconds between actions
		self.action_delay_factor = Config.driver_behaviour['action_delay_factor']
		
		#########################
		# Virtual bus instances #
		#########################

		# Initialize bus for critical ECU components, identified by vcan0
		self.critical_bus = can.Bus(interface='virtual',
		              channel='vcan0')

		# Initialize bus for non-critical ECU components, identified by vcan1
		self.non_critical_bus = can.Bus(interface='virtual',
		              channel='vcan1')

		self.journal = journal

	##############################
	# Driver Behaviour Functions #
	##############################

	def apply_brakes(self):
		# message with id for the brakes ecu
		brake_message = Message(target_component='brakes', data=[0x11, 0x11, 0x11])
		self.critical_bus.send(brake_message)
		self.journal.incr_innocent()

	def accelerate(self):
		# message with id for the brakes ecu
		fuel_message = Message(target_component='fuel', data=[0x11, 0x11, 0x11])
		self.critical_bus.send(fuel_message)
		self.journal.incr_innocent()

	def turn(self):
		# message with id for the steering ecu
		steering_message = Message(target_component='steering', data=[0x11, 0x11, 0x11])
		self.critical_bus.send(steering_message)
		self.journal.incr_innocent()

	def change_music(self):
		# message with id for the infotainment ecu
		infotainment_message = Message(target_component='infotainment', data=[0x11, 0x11, 0x11])
		self.non_critical_bus.send(infotainment_message)
		self.journal.incr_innocent()
		
	def adjust_temperature(self):
		# message with id for the climate control ecu
		climate_message = Message(target_component='climate_control', data=[0x11, 0x11, 0x11])
		self.non_critical_bus.send(climate_message)
		self.journal.incr_innocent()

	def drive(self, stop_event):

		actions = [self.apply_brakes, self.accelerate, self.turn, self.change_music, self.adjust_temperature]

		while True:
			actidx = random.randint(0,4)
			actions[actidx]()
			time.sleep(random.random() * self.action_delay_factor)
			if stop_event.is_set():
				self.critical_bus.shutdown()
				self.non_critical_bus.shutdown()
				break

	def start(self, stop_event):

		self.drive(stop_event)




