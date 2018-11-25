import can
from config import Config

def Message(target_component, payload):
	component_id = Config.components[target_component]['id']
	return can.Message(arbitration_id=component_id, extended_id=True, data=payload)


