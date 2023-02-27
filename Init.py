import ipaddress

from AttackValidator import AttackValidator
from Constants.constants import *
from Constants.errorconstants import *
from Help import Help
import getopt
import os
import sys
from tabulate import tabulate


class Init:
    def __init__(self):
        pass

    @staticmethod
    def initialize():
        _check_if_root_user()
        _display_welcome()
        return _parse_arguments()


####################################|| INIT HELPER FUNCTIONS ||####################################
def _check_if_root_user():
    if not os.geteuid() == 0:
        sys.exit(USER_NOT_ROOT_ERROR)


def _check_args(opts):
    if len(opts) == ZERO:
        sys.exit(NO_ARG_ERROR)


def _check_dst_ip(argument):
    try:
        ipaddress.ip_address(argument)
    except ValueError:
        sys.exit(INVALID_DST_IP_MSG)


def _check_src_ip(argument):
    try:
        ipaddress.ip_address(argument)
    except ValueError:
        sys.exit(INVALID_SRC_IP_MSG)


def _display_args(*args):
    data = INITIAL_TABLE_DATA
    header = TABLE_HEADER

    _display_args_helper(args, data)

    print(tabulate(data, headers=header))
    print(WELCOME_DECORATION)


def _display_args_helper(args, data):
    index = ZERO
    for arg in args:
        if arg == ZERO or arg == "":
            data[index].append(NOT_PROVIDED_STR)
        elif arg == XMAS_TREE:
            data[index].append(XMAS_TREE_STR)
        elif arg == PORT_SCAN:
            data[index].append(PORT_SCAN_STR)
        elif arg == SYN_FLOOD:
            data[index].append(SYN_FLOOD_STR)
        elif arg == ICMP_FLOOD:
            data[index].append(ICMP_FLOOD_STR)
        else:
            data[index].append(arg)
        index += 1


def _display_welcome():
    print(WELCOME_MSG)
    print(WELCOME_DECORATION)


def _help_menu():
    Help.print_help_manual()


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
            _check_dst_ip(argument)
            dst_ip = argument
        if opt == '-p':
            try:
                port_num = int(argument)
                if port_num < ZERO or port_num > MAX_PORT:
                    sys.exit(INVALID_PORT_NUMBER_MSG)
            except ValueError:
                sys.exit(PORT_NUMBER_NOT_INT_MSG)
        if opt == '-s':
            _check_src_ip(argument)
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
                sys.exit(MAX_PORT_NUMBER_NOT_INT_MSG)
        if opt == '--help':
            _help_menu()
            exit()

    # Critical Variables Check
    if type_of_attack == "":
        sys.exit(NO_ATTACK_SPECIFIED_MSG)

    if dst_ip == "":
        sys.exit(NO_TARGET_IP_MSG)

    # Display args
    _display_args(dst_ip, port_num, src_ip,
                  num_of_packets_to_send, type_of_attack,
                  min_port, max_port)

    return dst_ip, port_num, src_ip, num_of_packets_to_send, type_of_attack, min_port, max_port
