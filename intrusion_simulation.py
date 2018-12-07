from adversaries.intrusion_infotainment import IntrusionInfotainment
from hsm.noop import Noop
from vehicle import Vehicle
cv = Vehicle(IntrusionInfotainment, Noop)
cv.ignition()
