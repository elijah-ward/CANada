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
		'action_delay_factor': 0.5
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

	message_structure = {
		'data' : 3,
		'signature': 128
	}

	identity_keys = [
		'5LK5CPk363GkA7e9PCZONL4HWZuv6xwFZzjbB7i97Nz4btaSwzsmL5bUL0DOoOLl7EGDUDpCdcpiqqo0Poy0GF7qpXCRIpF5tLzUpaulKGNfBLLUD9KdES1AbKlA28Mo',
		'cfhxtTL6pXq0HNfhs1pXzzJ6N6k7vz7lSVupJpGz2YsH97hWTyNtUkMDDI6lmSUN3LiAH03v0MHH5wDsGKwBAEpMosqVob76m8ZC2wVjPQAkgkRqO6JQqQfKk6S1nqrP',
		'1fp83khmM4h2BvZsAq6bfpNJJTp2EJuJCYYHWiF6LtSVlSnnWAgG9GukKVarBSl6GnaxxpGt6aJCE0MFJjHpdSngpApdLMsJbbXq9wNg6F9g7CJ7pkJ2znl7iBAYkMdH',
		'q9Os2cdIMSbUltuvcWsUCrDe9NDe2K1mw0PR2smLqts2jOSFvg6AiaEeVt0Q4KB4hQsrh3qAHw90UQBiIrkW3cKm6ivmSa0CJn9w8puGXBeR98e5sJGk9qWL93Ds7Yr9',
		'RoxlCbC342IyFoIFezw0lxo77FRMjdTz6jjSopLhnQ7MqViyISgOg3Qa7UwiPjrD3AtfG9w6JbWykep6EIiZ8MNVYEkb5fLHEvwptvmxHGkiv8JE92IClF1HC1LBJ8oO',
		'4hahd3M1BaOOyUOUh4lYbpRadGmPRLkFymtKyxVk6NznDoCx6plXCVP9xyEE9yIOtApZrHS0e3N0Fl8D2IVUKfGT1VxM5lrOGqle5BuQwjFQHfWCaGtqwvMiwV55QAZA',
		'7xlws7sOPpbVuo2dScSZtJHpDG7EXI4iHPwFecvFH3uvzXxe89haBX9H9DRP8gWmHzTxP5VzNFrJs5YBBsiZjLkLx012UFero8EPPcNpnF8w0g3paDvHrG3PAz5mOhHP',
		'0liyf4A7CvIYkzOm5m0wSInbL9qh1shqobiIOT1bovyUE2HiJk0DPjTLRzuOexw6r52x5P1ryjqmz3rWPvFb1x9IixCgBWl1fVUSxMUxBasJ0nKKQv9Vh8dxPgbLyaMf',
		'TYIRhhcKBHvJFLrELjhqCkC6n9ny5VWITkCLZ1TTJx0NeLdY1E1LD3jK3Guipx9WdNdWX28lRUvaGplzioBX8B6Iae0C5ZTu5m5wweeFeiqhKi4UTlRkcOefYw7MQSHa',
		'S72bYzK6L8Mc45XERwMpOo7XZrGbaYjH075GjKjymZWkz7mwVmY63YSfHr563X2vbZ1B05dH87teFr5kDXFQUbqGEDYgCzWJwgld8g2C8zENds5WBdOtW0R2hkuCpnyJ'
	]

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
			'injection_delay': 0.1,
			'start_delay': 20
		}
	}