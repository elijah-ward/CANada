import can
from can.listener import Listener
from config import Config

class BetterPrinter(Listener):

	def on_message_received(self, msg):
		msg_id = msg.arbitration_id
		print('[ Timestamp: {} ] - [ ID: {} ] - [ Target Component: {} ] - [ Data: {} ] - [ Channel: {} ]'
			.format(msg.timestamp, msg_id, Config.id_assignment[msg_id], msg.data, msg.channel))