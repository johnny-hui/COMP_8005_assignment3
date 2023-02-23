NO_ARG_ERROR = "[+] NO_ARG_ERROR: No arguments were passed in!"
NO_ATTACK_SPECIFIED_MSG = "[+] ARG_ERROR (--attack=): The type of attack was not specified!\n" \
                          "[+] Please refer to --help option for list of possible attacks."

NO_TARGET_IP_MSG = "[+] ARG_ERROR: The target IP (-d) option was not specified!"
INVALID_ATTACK_MSG = "[+] ARG_ERROR (--attack=): An invalid attack was provided!\n" \
                     "[+] Please refer to --help option for list of possible attacks."
INVALID_PORT_NUMBER_MSG = "[+] ARG_ERROR: Port number cannot be negative or exceed 65536!"
INVALID_MIN_PORT_NUMBER_MSG = "[+] ARG_ERROR: Min port number (--min_port) cannot be negative or exceed 65536!"
INVALID_MAX_PORT_NUMBER_MSG = "[+] ARG_ERROR: Max port number (--max_port) cannot be negative or exceed 65536!"
PORT_NUMBER_NOT_INT_MSG = "[+] ValueError: Port (-p option) is not an integer!"
MIN_PORT_NUMBER_NOT_INT_MSG = "[+] ValueError: Min Port (--min_port option) is not an integer!"
MAX_PORT_NUMBER_NOT_INT_MSG = "[+] ValueError: Max Port (--max_port option) is not an integer!"
NUM_OF_PACKETS_ERROR_MSG = "[+] ValueError: Number of packets (-c option) is not an integer!"
NUM_OF_PACKETS_NEGATIVE_ERROR_MSG = "[+] ARG_ERROR: Number of packets (-c option) cannot be a negative integer!"
MIN_PORT_NOT_SPECIFIED_MSG = "[+] PORT_SCAN_ERROR: The --min_port option was not specified!"
MAX_PORT_NOT_SPECIFIED_MSG = "[+] PORT_SCAN_ERROR: The --max_port option was not specified!"
MAX_PORT_LESS_THAN_MIN_ERROR_MSG = "[+] PORT_SCAN_ERROR: The --max_port cannot be less than --min_port!"
