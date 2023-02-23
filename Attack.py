from constants import *
from errorconstants import *
import sys

class Attack:
    def __init__(self):
        pass

    def port_scan(self, target_ip, min_port, max_port):
        if min_port == ZERO:
            sys.exit(MIN_PORT_NOT_SPECIFIED_MSG)
        elif max_port == ZERO:
            sys.exit(MAX_PORT_NOT_SPECIFIED_MSG)


