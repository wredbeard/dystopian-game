# custom class to manage console colors, probably doesn't work for windows
class GameColors:
    def __init__(self):
        self.RED = '\u001b[31m'
        self.GREEN = '\u001b[32m'
        self.YELLOW = '\u001b[33m'
        self.BLUE = '\u001b[34m'
        self.MAGENTA = '\u001b[35m'
        self.CYAN = '\u001b[36m'
        self.WHITE = '\u001b[37m'
        self.RESET = '\u001b[0m'