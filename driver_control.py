import can
from messages.message_factory import Message

class DriverControl:

	def __init__(self):
		
		#########################
		# Virtual bus instances #
		#########################

		# Initialize bus for critical ECU components, identified by vcan0
		self.critical_bus = can.Bus(interface='virtual',
		              channel='vcan0')

		# Initialize bus for non-critical ECU components, identified by vcan1
		self.non_critical_bus = can.Bus(interface='virtual',
		              channel='vcan1')

	def apply_brakes(self):
		# message with id for the brakes ecu
		brake_message = Message(target_component='brakes', payload=[0x11, 0x11, 0x11])
		self.critical_bus.send_periodic(brake_message, period=1.0)

	def accelerate(self):
		# message with id for the brakes ecu
		fuel_message = Message(target_component='fuel', payload=[0x11, 0x11, 0x11])
		self.critical_bus.send_periodic(fuel_message, period=1.0)

	def turn(self):
		# message with id for the steering ecu
		steering_message = Message(target_component='steering', payload=[0x11, 0x11, 0x11])
		self.critical_bus.send_periodic(steering_message, period=1.0)

	def change_music(self):
		# message with id for the infotainment ecu
		infotainment_message = Message(target_component='infotainment', payload=[0x64, 0x64, 0x64])
		self.non_critical_bus.send_periodic(infotainment_message, period=1.0)
		
	def adjust_temperature(self):
		# message with id for the climate control ecu
		climate_message = Message(target_component='climate_control', payload=[0x65, 0x65, 0x65])
		self.non_critical_bus.send_periodic(climate_message, period=1.0)

	def start(self):

		self.accelerate()
		self.apply_brakes()
		self.turn()
		self.change_music()
		self.adjust_temperature()




