# Author
AUTHOR = "Johnny Hui"
AUTHOR_ID = "A00973103"

# Init Constants
WELCOME_MSG = f"A program demonstrating common TCP attacks (using Scapy) \nBy {AUTHOR} ({AUTHOR_ID})"
WELCOME_DECORATION = "=============================================================================================" \
                     "=============="
NUMBER_OF_PACKETS = "Number of Packets"
PORT_NUMBER = "Port Number"
TYPE_ATTACK = "Type of Attack"
MIN_PORT_STR = "Minimum Port"
MAX_PORT_STR = "Maximum Port"
DEST_IP_STR = "Destination/Target IP"
SRC_IP_STR = "Source IP"
INITIAL_TABLE_DATA = [["-d", DEST_IP_STR], ["-p", PORT_NUMBER], ["-s", SRC_IP_STR], ["-c", NUMBER_OF_PACKETS],
                      ["--attack", TYPE_ATTACK], ["--min_port", MIN_PORT_STR], ["--max_port", MAX_PORT_STR]]
TABLE_HEADER = ["Flag", "Option", "Value Set"]
NOT_PROVIDED_STR = "N/A"

# TCP Config
LONG_OPTS = ['attack=', 'help', 'min_port=', 'max_port=']
PORT_SCAN = "port_scan"
PORT_SCAN_STR = "Port Scanning"
SYN_FLOOD = "syn_flood"
SYN_FLOOD_STR = "SYN Flood"
XMAS_TREE = "xmas"
XMAS_TREE_STR = "Christmas Tree"
ICMP_FLOOD = "icmp"
ICMP_FLOOD_STR = "ICMP Flood"
MAX_PORT = 65536
MIN_PORT = 1
MAX_PAYLOAD_SIZE = 1024
ZERO = 0
RESPONSE_TIMEOUT = 0.5
SYN_ACK_HEX = 0x12

# TCP Flags
SYN = 'S'
RST = 'R'
FIN = 'F'
PSH = 'P'
ACK = 'A'
CWR = 'C'
ECE = 'E'
URG = 'U'
ALL_FLAGS = f'{SYN}{RST}{FIN}{PSH}{ACK}{CWR}{ECE}{URG}'

# Attack Messages
ICMP_FLOOD_INIT_MSG = "[+] ICMP FLOOD: Launching ICMP flood on "
ICMP_FLOOD_STOP_MSG = "[+] ICMP FLOOD: Press CTRL+C to stop the attack..."
ICMP_FLOOD_COMPLETE_MSG = "[+] ICMP FLOOD COMPLETE!"
ICMP_FLOOD_COMPLETE_FORCE_MSG = "[+] ICMP FLOOD COMPLETE: Forced Stop (CTRL+C was pressed)"
PORT_SCAN_INIT_MSG = "[+] PORT SCAN: Launching port scanner..."
SYN_FLOOD_INIT_MSG = "[+] SYN FLOOD: Launching syn flood attack on "
SYN_FLOOD_STOP_MSG = "[+] SYN FLOOD: Press CTRL+C to stop the attack..."
SYN_FLOOD_COMPLETE_MSG = "[+] SYN FLOOD COMPLETE!"
SYN_FLOOD_COMPLETE_FORCE_MSG = "[+] SYN FLOOD COMPLETE: Forced Stop (CTRL+C was pressed)"
XMAS_TREE_INIT_MSG = "[+] CHRISTMAS TREE: Launching christmas tree attack on "
XMAS_TREE_STOP_MSG = "[+] CHRISTMAS TREE: Press CTRL+C to stop the attack..."
XMAS_TREE_COMPLETE_MSG = "[+] CHRISTMAS TREE COMPLETE!"
XMAS_TREE_COMPLETE_FORCE_MSG = "[+] CHRISTMAS TREE COMPLETE: Forced Stop (CTRL+C was pressed)"
SPOOF_SOURCE_IP_MSG = "[+] SPOOF: Source IP (-s) argument was not provided.\n" \
                      "[+] SPOOF: Now spoofing your source IP..."
SPOOF_SOURCE_IP_FINAL_MSG = "[+] SPOOF COMPLETE: Your IP is now "
RANDOMIZE_PORT_MSG = "[+] PORT NUMBER: Port number (-p) argument was not provided.\n" \
                     "[+] PORT NUMBER: Now generating a random port for attack..."
RANDOMIZE_FINAL_MSG = "[+] GENERATE COMPLETE: The port to attack is now "


# Help Messages
HELP_PROGRAM_TERMINATE_MSG = "[+] PROGRAM TERMINATE: Program has been terminated!"
BOLD_START = "\033[1m"
BOLD_END = "\033[0m"
UNDERLINE_START = "\033[4m"
UNDERLINE_END = "\033[0m"
