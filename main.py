from Constants import constants
from Attack import Attack
from Init import *

if __name__ == '__main__':
    # Initialize Program
    dest_ip, port, source_ip, number_of_packets, \
        attack_type, min_port, max_port = Init.initialize()

    # Launch Attack
    Attack.launch_attack(attack_type, dest_ip, port,
                         source_ip, number_of_packets,
                         min_port, max_port)
