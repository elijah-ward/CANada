import argparse
import pandas

from adversaries.ddos_infotainment import DDOSInfotainment
from hsm.frequency_analyzer import FrequencyAnalyzer

from adversaries.external_node import ExternalNode
from hsm.authentication import Authentication

from adversaries.intrusion_infotainment import IntrusionInfotainment
from hsm.intrusion_detection import Noop

from vehicle import Vehicle
from utils.trial_journal import TrialJournal, TrialCollection

parser = argparse.ArgumentParser(description='entrypoint for running trials against the CANada demo')
parser.add_argument('n_trials', type=int, help='the number of trials to run')
parser.add_argument('trial_length', type=int, help='the length of each trial in seconds')

args = parser.parse_args()

# Run trials for frequency analysis method
journal = TrialJournal(1)
cv = Vehicle(DDOSInfotainment, FrequencyAnalyzer, journal)
cv.ignition(args.trial_length)

print(str(journal))

# Run trials for authentication method


# Run trials for intrusion detection method
