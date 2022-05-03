class Square:
    closed = "\u25a0"
    bomb = "\u002a"  # "\U0001F4A3"
    blank = "\u25a1"
    flag = "\u2691"

    def __init__(self):
        self.open = False
        self.adjacent_mines = 0
        self.mine = False
        self.flagged = False
        self.value = self.closed

    def get_open(self) -> bool:
        return self.open

    def get_mine(self) -> bool:
        return self.mine

    def get_adjacent_mines(self) -> int:
        return self.adjacent_mines

    def get_flagged(self) -> bool:
        return self.flagged

    def set_open(self, status: bool) -> None:
        self.open = status
        self.set_value(self.blank)

    def set_mine(self, mine: bool) -> None:
        self.mine = mine
        self.set_value(self.bomb)

    def set_flagged(self, flagged: bool) -> None:
        self.flagged = flagged
        self.set_value(self.flag)

    def increase_adjacent_mines(self) -> None:
        self.adjacent_mines += 1
        self.set_value(self.adjacent_mines)

    def set_value(self, value):
        self.value = value

    def get_value(self) -> str:
        return self.value
