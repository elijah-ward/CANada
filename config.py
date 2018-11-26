# config.py

class Config:

	"""
	General Config

	critical_bus - specifies the id of the bus linked to critical ECUs
	security_algorithm - specifies the 
	"""

	general = {
		'channels': {
			'critical_bus': 'vcan0',
			'non_critical_bus': 'vcan1'
		}
	}

	hsm = {
		'security_module': 'FrequencyAnalyzer'
	}

	driver_behaviour = {
		'action_delay_factor': 0.2
	}

	frequency_analyzer = {
		'allowed_variance': 0.5,
		'seconds_training_time': 10
	}

	"""
	Each component in this configuration represents an ECU within a CV

	It currently contains 3 parts:
	id - arbitration id the component filters for to act on messages it cares about
	can_channel - the identifier indicating which CAN bus the component belongs to
	dedicated_hsm - Boolean indicating whether it has a dedicated HSM monitoring its behaviour
	"""

	components = {
		'brakes': {
			'id': 0x1,
			'can_channel': 'vcan0',
			'dedicated_hsm': 'false'
		},
		'fuel': {
			'id': 0x4,
			'can_channel': 'vcan0',
			'dedicated_hsm': 'false'
		},
		'steering': {
			'id': 0x5,
			'can_channel': 'vcan0',
			'dedicated_hsm': 'false'
		},
		'infotainment': {
			'id': 0x40,
			'can_channel': 'vcan1',
			'dedicated_hsm': 'false',
			'diagnostic_delay_factor': 2.0
		},
		'climate_control': {
			'id': 0x41,
			'can_channel': 'vcan1',
			'dedicated_hsm': 'false'
		}
	}

	id_assignment = {
		0x1: 'brakes',
		0x4: 'fuel',
		0x5: 'steering',
		0x40: 'infotainment',
		0x41: 'climate_control'
	}

	"""
	ADVERSARIES
	Following is the configuration for each of the adversaries
	"""

	adversaries = {
		'ddos_infotainment': {
			'injection_delay': 0.2,
			'start_delay': 20
		}
	}