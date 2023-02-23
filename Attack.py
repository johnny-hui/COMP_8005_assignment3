from constants import *
from errorconstants import *
import sys


class Attack:
    def __init__(self):
        pass

    @staticmethod
    def port_scan(target_ip, min_port, max_port):
        min_port, max_port = _port_scan_helper(min_port, max_port)

        print(f"[+] Now scanning target IP: {target_ip} [from ports {min_port}-{max_port}]...")


def _port_scan_helper(min_port, max_port):
    if min_port == ZERO:
        sys.exit(MIN_PORT_NOT_SPECIFIED_MSG)
    if max_port == ZERO:
        sys.exit(MAX_PORT_NOT_SPECIFIED_MSG)
    if max_port < min_port:
        sys.exit(MAX_PORT_LESS_THAN_MIN_ERROR_MSG)
    if max_port == min_port:
        max_port += 1

    return min_port, max_port


