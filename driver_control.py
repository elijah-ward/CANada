import can
import random
import time
from config import Config
from messages.message_factory import Message

class DriverControl:

	def __init__(self):

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

	##############################
	# Driver Behaviour Functions #
	##############################

	def apply_brakes(self):
		# message with id for the brakes ecu
		brake_message = Message(target_component='brakes', payload=[0x11, 0x11, 0x11])
		self.critical_bus.send(brake_message)

	def accelerate(self):
		# message with id for the brakes ecu
		fuel_message = Message(target_component='fuel', payload=[0x11, 0x11, 0x11])
		self.critical_bus.send(fuel_message)

	def turn(self):
		# message with id for the steering ecu
		steering_message = Message(target_component='steering', payload=[0x11, 0x11, 0x11])
		self.critical_bus.send(steering_message)

	def change_music(self):
		# message with id for the infotainment ecu
		infotainment_message = Message(target_component='infotainment', payload=[0x64, 0x64, 0x64])
		self.non_critical_bus.send(infotainment_message)
		
	def adjust_temperature(self):
		# message with id for the climate control ecu
		climate_message = Message(target_component='climate_control', payload=[0x65, 0x65, 0x65])
		self.non_critical_bus.send(climate_message)

	def drive(self):

		actions = [self.apply_brakes, self.accelerate, self.turn, self.change_music, self.adjust_temperature]

		while True:
			actidx = random.randint(0,4)
			actions[actidx]()
			time.sleep(random.random() * self.action_delay_factor)

	def start(self):

		self.drive()




