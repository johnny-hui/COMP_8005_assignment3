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
PORT_SCAN_INIT_MSG = "[+] PORT SCAN: Launching port scan..."
SPOOF_SOURCE_IP_MSG = "[+] SPOOF: Source IP (-s) argument was not provided.\n" \
                      "[+] SPOOF: Now spoofing your source IP..."
SPOOF_SOURCE_IP_FINAL_MSG = "[+] SPOOF COMPLETE: Your IP is now "

