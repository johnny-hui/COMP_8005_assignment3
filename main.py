from Constants import constants
from Attack import Attack
from Init import *

if __name__ == '__main__':
    # Initialize Program
    dest_ip, port, source_ip, number_of_packets, \
        attack_type, min_port, max_port = Init.initialize()

    # Launch Attack
    match attack_type:
        case constants.PORT_SCAN:
            Attack.port_scan(target_ip=dest_ip, src_ip=source_ip,
                             min_port=min_port, max_port=max_port)
        case constants.SYN_FLOOD:
            Attack.syn_flood(target_ip=dest_ip, port=port,
                             num_of_pkts=number_of_packets)
        case constants.XMAS_TREE:
            Attack.xmas_tree(target_ip=dest_ip, port=port,
                             num_of_pkts=number_of_packets)
