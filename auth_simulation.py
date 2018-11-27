from adversaries.external_node import ExternalNode
from hsm.authentication import Authentication
from vehicle import Vehicle
cv = Vehicle(ExternalNode, Authentication)
cv.ignition()
