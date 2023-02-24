import constants
from Attack import Attack
from AttackValidator import AttackValidator
from errorconstants import *
import getopt
from Init import *
import sys


def _check_args(opts):
    if len(opts) == ZERO:
        sys.exit(NO_ARG_ERROR)


def _parse_arguments():
    dst_ip = ""
    src_ip = ""
    type_of_attack = ""
    num_of_packets_to_send = ZERO
    port_num = ZERO
    min_port = ZERO
    max_port = ZERO

    # Remove file name from argument list
    arguments = sys.argv[1:]

    # Getting the file directory from (-f flag) and users (as args)
    opts, user_list_args = getopt.getopt(arguments, 'c:d:p:s:', LONG_OPTS)

    # Check if empty parameters
    _check_args(opts)

    # Parsing command-line args
    for opt, argument in opts:
        if opt == '-c':
            try:
                num_of_packets_to_send = int(argument)
                if num_of_packets_to_send < ZERO:
                    sys.exit(NUM_OF_PACKETS_NEGATIVE_ERROR_MSG)
            except ValueError:
                sys.exit(NUM_OF_PACKETS_ERROR_MSG)
        if opt == '-d':
            dst_ip = argument
        if opt == '-p':
            try:
                port_num = int(argument)
                if port_num < ZERO or port_num > MAX_PORT:
                    sys.exit(INVALID_PORT_NUMBER_MSG)
            except ValueError:
                sys.exit(PORT_NUMBER_NOT_INT_MSG)
        if opt == '-s':
            src_ip = argument
        if opt == '--attack':
            if AttackValidator.is_valid(argument):
                type_of_attack = argument
            else:
                sys.exit(INVALID_ATTACK_MSG)
        if opt == '--min_port':
            try:
                min_port = int(argument)
                if min_port < ZERO or min_port > MAX_PORT:
                    sys.exit(INVALID_MIN_PORT_NUMBER_MSG)
            except ValueError:
                sys.exit(MIN_PORT_NUMBER_NOT_INT_MSG)
        if opt == '--max_port':
            try:
                max_port = int(argument)
                if max_port < ZERO or max_port > MAX_PORT:
                    sys.exit(INVALID_MAX_PORT_NUMBER_MSG)
            except ValueError:
                sys.exit(MAX_PORT_NOT_SPECIFIED_MSG)
        if opt == '--help':
            print("HELP")

    # Critical Variables Check
    if type_of_attack == "":
        sys.exit(NO_ATTACK_SPECIFIED_MSG)

    if dst_ip == "":
        sys.exit(NO_TARGET_IP_MSG)

    return dst_ip, port_num, src_ip, num_of_packets_to_send, type_of_attack, min_port, max_port


if __name__ == '__main__':
    # Initialize Program
    Init.initialize()

    # Parse Args
    dest_ip, port, source_ip, number_of_packets, \
        attack_type, min_port, max_port = _parse_arguments()

    # Launch Attack
    match attack_type:
        case constants.PORT_SCAN:
            Attack.port_scan(target_ip=dest_ip, src_ip=source_ip,
                             min_port=min_port, max_port=max_port)
        case constants.SYN_FLOOD:
            print("SYN")
        case constants.XMAS_TREE:
            print("XMAS")
