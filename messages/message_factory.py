import can
import time
from config import Config

def create_payload(data, signature):
	byte_data = bytearray(data)
	byte_sig = bytearray(signature, 'utf-8')
	return byte_data + byte_sig

def get_signature():
	curr_time = str(time.time())
	curr_seconds = curr_time.split('.')[0]
	lsd = int(curr_seconds[len(curr_seconds)-1])
	return Config.identity_keys[lsd]

def Message(target_component, data):
	component_id = Config.components[target_component]['id']
	signature = get_signature()
	return can.Message(arbitration_id=component_id, extended_id=True, data=create_payload(data, signature))


