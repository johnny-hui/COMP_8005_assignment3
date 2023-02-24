from constants import *
import os
import sys


class Init:
    def __init__(self):
        pass

    @staticmethod
    def initialize():
        _check_if_root_user()
        _display_welcome()


def _display_welcome():
    print(WELCOME_MSG)
    print(WELCOME_DECORATION)


def _check_if_root_user():
    if not os.geteuid() == 0:
        sys.exit("[+] ERROR: Only the 'root' user can run this script "
                 "[Please run this script again using sudo command].")


