# Results class

class TrialJournal:

	def __init__(self, idx):
		self.idx = idx
		self.innocent_messages = 0
		self.hostile_messages = 0
		self.innocent_blocked = 0
		self.innocent_forwarded = 0
		self.hostile_blocked = 0
		self.hostile_forwarded = 0

	def incr_innocent(self):
		self.innocent_messages += 1

	def incr_hostile(self):
		self.hostile_messages += 1

	def incr_innocent_blocked(self):
		self.innocent_blocked += 1

	def incr_hostile_blocked(self):
		self.hostile_blocked += 1

	def incr_innocent_forwarded(self):
		self.innocent_forwarded += 1

	def incr_hostile_forwarded(self):
		self.hostile_forwarded += 1

	def __str__(self):
		table = '''
		----- Trial #{} -----\n
		innocent messages sent: {}\n
		hostile messages sent: {}\n
		innocent messages blocked: {}\n
		innocent messages forwarded: {}\n
		hostile messages blocked: {}\n
		hostile messages forwarded: {}\n
		'''.format(self.idx, self.innocent_messages, self.hostile_messages,
				self.innocent_blocked, self.innocent_forwarded, self.hostile_blocked, 
				self.hostile_forwarded)

		return table



class TrialCollection:

	def __init__(self):
		self.trials = []

	def add_trial(self, trial):
		self.trials.append(trial)
