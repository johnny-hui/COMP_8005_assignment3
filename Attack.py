from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sr1
from scapy.volatile import RandIP
from constants import *
from errorconstants import *
import sys


class Attack:
    def __init__(self):
        pass

    @staticmethod
    def port_scan(target_ip, src_ip, min_port, max_port):
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


# Helper Functions
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


if __name__ == '__main__':
    Attack.port_scan(target_ip="10.0.0.153", src_ip="10.0.0.231", min_port=1, max_port=9000)
