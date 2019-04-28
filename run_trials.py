import argparse
import pandas as pd
import logging

from adversaries.ddos_infotainment import DDOSInfotainment
from hsm.frequency_analyzer import FrequencyAnalyzer

from adversaries.external_node import ExternalNode
from hsm.authentication import Authentication

from adversaries.intrusion_infotainment import IntrusionInfotainment
from hsm.noop import Noop

from vehicle import Vehicle
from utils.trial_journal import TrialJournal, TrialCollection

parser = argparse.ArgumentParser(description='entrypoint for running trials against the CANada demo')
parser.add_argument('n_trials', type=int, help='the number of trials to run')
parser.add_argument('trial_length', type=int, help='the length of each trial in seconds')
args = parser.parse_args()

logging.basicConfig(level=logging.WARNING)

col_names = ['id', 'innocent_generated', 'hostile_generated', 'innocent_blocked',
	'innocent_forwarded', 'hostile_blocked', 'hostile_forwarded']

freq_collection = []
auth_collection = []
intr_collection = []

# Run trials for frequency analysis method
for i in range(args.n_trials):
	journal = TrialJournal(i)
	cv = Vehicle(DDOSInfotainment, FrequencyAnalyzer, journal)
	cv.ignition(args.trial_length)
	freq_collection.append({ 
		'id': journal.idx, 
		'innocent_generated': journal.innocent_messages, 
		'hostile_generated': journal.hostile_messages, 
		'innocent_blocked': journal.innocent_blocked, 
		'innocent_forwarded': journal.innocent_forwarded, 
		'hostile_blocked': journal.hostile_blocked, 
		'hostile_forwarded': journal.hostile_forwarded 
		})

print(freq_collection)
freq_df = pd.DataFrame(freq_collection)

# Run trials for authentication method
for i in range(args.n_trials):
	journal = TrialJournal(i)
	cv = Vehicle(ExternalNode, Authentication, journal)
	cv.ignition(args.trial_length)
	auth_collection.append({ 
		'id': journal.idx, 
		'innocent_generated': journal.innocent_messages, 
		'hostile_generated': journal.hostile_messages, 
		'innocent_blocked': journal.innocent_blocked, 
		'innocent_forwarded': journal.innocent_forwarded, 
		'hostile_blocked': journal.hostile_blocked, 
		'hostile_forwarded': journal.hostile_forwarded 
		})

print(auth_collection)
auth_df = pd.DataFrame(auth_collection)

# Run trials for intrusion detection method
for i in range(args.n_trials):
	journal = TrialJournal(i)
	cv = Vehicle(IntrusionInfotainment, Noop, journal)
	cv.ignition(args.trial_length)
	intr_collection.append({ 
		'id': journal.idx, 
		'innocent_generated': journal.innocent_messages, 
		'hostile_generated': journal.hostile_messages, 
		'innocent_blocked': journal.innocent_blocked, 
		'innocent_forwarded': journal.innocent_forwarded, 
		'hostile_blocked': journal.hostile_blocked, 
		'hostile_forwarded': journal.hostile_forwarded 
		})

print(intr_collection)
intr_df = pd.DataFrame(intr_collection)

freq_df.to_csv('./freq_analysis_stats.csv', header=True, index=False)
auth_df.to_csv('./authentication_stats.csv', header=True, index=False)
intr_df.to_csv('./intrusion_detection_stats.csv', header=True, index=False)
