# Author
AUTHOR = "Johnny Hui"
AUTHOR_ID = "A00973103"

# Welcome Message Constants
WELCOME_MSG = f"A program demonstrating common TCP attacks (using Scapy) \nBy {AUTHOR} ({AUTHOR_ID})"
WELCOME_DECORATION = "=============================================================================================" \
                     "=============="

# TCP Config
LONG_OPTS = ['attack=', 'help', 'min_port=', 'max_port=']
PORT_SCAN = "port_scan"
SYN_FLOOD = "syn_flood"
XMAS_TREE = "xmas"
MAX_PORT = 65536
MIN_PORT = 1
MAX_PAYLOAD_SIZE = 1024
ZERO = 0
RESPONSE_TIMEOUT = 0.5
SYN = 'S'
RST = 'R'
FIN = 'F'
PSH = 'P'
ACK = 'A'
CWR = 'C'
ECE = 'E'
URG = 'U'
SYN_ACK_HEX = 0x12

# Attack Messages
PORT_SCAN_INIT_MSG = "[+] PORT SCAN: Launching port scanner..."
SYN_FLOOD_INIT_MSG = "[+] SYN FLOOD: Launching syn flood attack on "
SYN_FLOOD_STOP_MSG = "[+] SYN FLOOD: Press CTRL+C to stop the attack..."
SYN_FLOOD_COMPLETE_MSG = "[+] SYN FLOOD COMPLETE!"
SYN_FLOOD_COMPLETE_FORCE_MSG = "[+] SYN FLOOD COMPLETE: Forced Stop (CTRL+C was pressed)"
SPOOF_SOURCE_IP_MSG = "[+] SPOOF: Source IP (-s) argument was not provided.\n" \
                      "[+] SPOOF: Now spoofing your source IP..."
SPOOF_SOURCE_IP_FINAL_MSG = "[+] SPOOF COMPLETE: Your IP is now "
RANDOMIZE_PORT_MSG = "[+] PORT NUMBER: Port number (-p) argument was not provided.\n" \
                               "[+] PORT NUMBER: Now generating a random port for attack..."
RANDOMIZE_FINAL_MSG = "[+] GENERATE COMPLETE: The port to attack is now "
