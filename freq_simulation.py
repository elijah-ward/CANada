from adversaries.ddos_infotainment import DDOSInfotainment
from hsm.frequency_analyzer import FrequencyAnalyzer
from vehicle import Vehicle
cv = Vehicle(DDOSInfotainment, FrequencyAnalyzer)
cv.ignition()
