
MANAGEMENT_FRAMES = 0
CONTROL_FRAMS = 1
DATA_FRAMES = 2

ASSOCIATION_REQUEST = 0
ASSOCIATION_RESPONSE = 1
REASSOCIATION_REQUEST = 2
REASSOCIATION_RESPONSE = 3
PROBE_REQUEST = 4
PROBE_RESPONSE = 5
BEACON = 8
ATIM = 9
DISASSOCIATE = 10
AUTHENTICATION = 11
DEAUTHENTICATION = 12
ACTION_FRAMES = 13

BLOCK_ACK_REQUEST = 24
BLOCK_ACK = 25
POWER_SAVE_POLL = 26
REQUEST_TO_SEND = 27
CLEAR_TO_SEND = 28
ACK = 29

# TODO: ADD MORE CONSTANTS
QOS_DATA = 40

SOLO3DR_CONTROLLER_ADDR = '8a:dc:96'
SOLO3DR_DRONE_ADDR = '88:dc:96'

INTEL_DRONE_ADDR = 'b0:48:7a'

ADDR_WITHE_LIST = (SOLO3DR_CONTROLLER_ADDR, SOLO3DR_DRONE_ADDR, INTEL_DRONE_ADDR)
ADDR_BLACK_LIST = ()
