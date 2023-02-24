from Constants import constants


class AttackValidator:
    def __init__(self):
        pass

    @staticmethod
    def is_valid(attack):
        match attack:
            case constants.PORT_SCAN:
                return True
            case constants.SYN_FLOOD:
                return True
            case constants.XMAS_TREE:
                return True
            case _:
                return False
