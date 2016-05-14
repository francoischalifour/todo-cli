CSI = '\033['


def code_to_chars(code):
    return CSI + str(code) + 'm'


class AnsiCodes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    LIGHTWHITE_EX   = 97

    FAIL   = 31
    WARNING   = 33
    INFO   = 90


class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    LIGHTBLACK_EX   = 100
    LIGHTWHITE_EX   = 107


class AnsiStyle(AnsiCodes):
    BOLD    = 1
    NORMAL    = 22
    RESET_ALL = 0


Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
