from constants import *
from errorconstants import *
import getopt
from scapy.layers.inet import IP, TCP
from scapy.layers.l2 import Ether
import sys


def _check_args(opts):
    if len(opts) == ZERO:
        sys.exit("[+] NO_ARG_ERROR: No arguments were passed in!")


def _parse_arguments():
    dst_ip = ""
    src_ip = ""
    type_of_attack = ""
    num_of_packets_to_send = ZERO
    port_num = ZERO

    # Remove file name from argument list
    arguments = sys.argv[1:]

    # Getting the file directory from (-f flag) and users (as args)
    opts, user_list_args = getopt.getopt(arguments, 'c:d:p:s:', ['help'])

    # Check if empty parameters
    _check_args(opts)

    # Parsing command-line args (Create options for port scanner, SYN Flood,
    # XMAS tree attack, another attk.)
    for opt, argument in opts:
        if opt == '-c':
            try:
                num_of_packets_to_send = int(argument)
            except ValueError:
                sys.exit(f"[+] ValueError: Number of packets (-c option) is not an integer!")
        if opt == '-d':
            dst_ip = argument
        if opt == '-p':
            try:
                port_num = int(argument)
                if port_num < ZERO or port_num > MAX_PORT:
                    sys.exit(f"[+] ARG_ERROR: Port number cannot be negative or exceed 65536!")
            except ValueError:
                sys.exit(f"[+] ValueError: Port (-p option) is not an integer!")
        if opt == '-s':
            src_ip = argument
        if opt == '--attack':
            type_of_attack = argument
        if opt == '--help':
            print("HELP")

    if type_of_attack == "":
        sys.exit(NO_ATTACK_SPECIFIED_MSG)

    if dst_ip == "":
        sys.exit(NO_TARGET_IP_MSG)

    return dst_ip, port_num, src_ip, num_of_packets_to_send, type_of_attack


if __name__ == '__main__':
    dest_ip, port, source_ip, number_of_packets, attack_type = _parse_arguments()

    # Layer2 = Ether()
    # Layer2.show()

    Layer3 = IP()
    Layer3.show()

    Layer4 = TCP()
    Layer4.show()

