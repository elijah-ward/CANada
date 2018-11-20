import can

component_ids = {
		"brakes": 0x1,
		"fuel": 0x4,
		"steering": 0x5,
		"infotainment": 0x40,
		"climate_control": 0x41
	}

def Message(target_component, payload):
	component_id = component_ids[target_component]
	return can.Message(arbitration_id=component_id, extended_id=True, data=payload)


