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
    BLACK = 30
    GREEN = 32
    BLUE = 34
    FAIL = 31
    WARNING = 33
    INFO = 90


class AnsiBack(AnsiCodes):
    GREEN = 42
    WHITE = 47


class AnsiStyle(AnsiCodes):
    BOLD = 1
    NORMAL = 22
    RESET_ALL = 0


Fore = AnsiFore()
Back = AnsiBack()
Style = AnsiStyle()
