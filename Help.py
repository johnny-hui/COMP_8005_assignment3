from Constants.constants import *


class Help:
    def __init__(self):
        pass

    @staticmethod
    def print_help_manual():
        # Title
        _print_help_title()

        # Name Section
        _print_help_name()

        # Author Section
        _print_help_author()

        # Description Section
        _print_help_description()

        # Required Options
        _print_help_required_options()

        # Optional Options
        _print_help_optional_options()

        # Full Example of Command to Run
        _print_help_examples()


def _print_help_author():
    print(f"\n{BOLD_START}AUTHOR{BOLD_END}")
    print(f"""       Johnny Hui <jhui34@my.bcit.ca> - a BCIT Network Security student""")


def _print_help_description():
    print(f"\n{BOLD_START}DESCRIPTION{BOLD_END}")
    print(f"""       This program is a simple Python implementation of a subset of hping3 that allows 
          the user to perform the following DDOS attack methods:
               - Port Scanning
               - SYN Flooding
               - ICMP (Ping) Flooding
               - Christmas Tree Attack

          DISCLAIMER: Please do not use this tool as means for unethical hacking of any sorts. 
          This program and its' author is not responsible for any repercussions that can occur 
          as a result of ill-intents.
       """)


def _print_help_examples():
    print(f"{BOLD_START}EXAMPLE COMMANDS{BOLD_END}")
    print(f"""       {UNDERLINE_START}Port Scanning{UNDERLINE_END}
                 sudo python main.py -d 10.0.0.153 --attack=port_scan --min_port=1 --max_port=1000
       """)
    print(f"""       {UNDERLINE_START}SYN Flood (Random Port){UNDERLINE_END}
                 sudo python main.py -d 10.0.0.153 --attack=syn_flood
       """)
    print(f"""       {UNDERLINE_START}SYN Flood (with Port Specified){UNDERLINE_END}
                 sudo python main.py -d 10.0.0.153 --attack=syn_flood -p 69
       """)
    print(f"""       {UNDERLINE_START}SYN Flood (with max number of packets){UNDERLINE_END}
                 sudo python main.py -d 10.0.0.153 --attack=syn_flood -p 69 -c 100
       """)
    print(f"""       {UNDERLINE_START}Christmas Tree Attack{UNDERLINE_END}
                 sudo python main.py -d 10.0.0.153 --attack=xmas -p 80
       """)
    print(f"""       {UNDERLINE_START}ICMP Flood{UNDERLINE_END}
                 sudo python main.py -d 10.0.0.153 --attack=icmp
       """)


def _print_help_name():
    print(f"{BOLD_START}NAME{BOLD_END}")
    print(f"""       Assignment 3 Network Attacker Program - Perform various DDOS attack methods""")


def _print_help_optional_options():
    print(f"{BOLD_START}OPTIONAL OPTIONS{BOLD_END}")
    print(f"""       {UNDERLINE_START}-c{UNDERLINE_END}
                 The {BOLD_START}number of packets{BOLD_END} to send to target. This option is only used in SYN FLOOD, ICMP FLOOD, and
                 CHRISTMAS TREE attacks. If this value is not specified, then this program will {BOLD_START}endlessly send
                 {BOLD_END}packets to the target. To stop this behavior and the program altogether, press the {BOLD_START}CTRL + C{BOLD_END} keys 
                 together.
       """)
    print(f"""       {UNDERLINE_START}-p{UNDERLINE_END}
                 The {BOLD_START}target's port number{BOLD_END}. This option is used only in SYN FLOOD, ICMP FLOOD, and CHRISTMAS TREE
                 attacks when you want to specifically target a port. If this value is not specified, then this 
                 program will {BOLD_START}randomly generate{BOLD_END} a port number, construct packets with it, and send them to that 
                 port based on a specific target IP.
       """)
    print(f"""       {UNDERLINE_START}-s (DEPRECATED){UNDERLINE_END}
                 Your {BOLD_START}source IP address{BOLD_END}. This option was originally designed to be used for the layer 3 (IP HEADER)
                 and when it is not, the program would have randomly generate one for you. This method is known as IP 
                 spoofing. Currently, this program automatically detects your IP and uses it as source when performing 
                 any attacks. As a result of potential unethical nature of this option, the support for it was dropped.
       """)
    print(f"""       {UNDERLINE_START}--min_port (REQUIRED FOR PORT SCANNING){UNDERLINE_END}
                 The {BOLD_START}minimum port number{BOLD_END} to start scanning from. An example of how to declare this option in the 
                 command line is as follows: {BOLD_START}sudo python main.py --attack=port_scan --min_port=1{BOLD_END}

                 NOTE: --min_port must not be a negative integer, nor be greater than --max_port option, nor exceed 
                 maximum usable port 65536!
       """)
    print(f"""       {UNDERLINE_START}--max_port (REQUIRED FOR PORT SCANNING){UNDERLINE_END}
                 The {BOLD_START}maximum port number{BOLD_END} to start scanning from. An example of how to declare this option in the 
                 command line is as follows: {BOLD_START}sudo python main.py --attack=port_scan --min_port=1 --max_port=65536{BOLD_END}

                 NOTE: --max_port must not be a negative integer, nor be less than --min_port option, nor exceed 
                 maximum usable port 65536!
       """)
    print(f"""       {UNDERLINE_START}--help{UNDERLINE_END}
                 Show the help screen on standard output.
       """)


def _print_help_required_options():
    print(f"{BOLD_START}REQUIRED OPTIONS{BOLD_END}")
    print(f"""       {UNDERLINE_START}-d{UNDERLINE_END}
                 The Target IP Address.""")
    print(f"""\n       {UNDERLINE_START}-attack{UNDERLINE_END}
                 The type of attack to perform. An {BOLD_START}example{BOLD_END} of how to specify this option is as 
                 follows: {BOLD_START}--attack=syn_flood{BOLD_END}

                 This option can take on the following values:
                       - {PORT_SCAN}
                       - {SYN_FLOOD}
                       - {XMAS_TREE}
                       - {ICMP_FLOOD}
                 """)


def _print_help_title():
    print(f"{BOLD_START}Help Manual{BOLD_END}\n".center(120))
