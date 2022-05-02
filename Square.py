class Square:
    closed = "\u25a0"
    bomb = "\U0001F4A3"
    blank = "\u25a1"
    flag = "\u2691"

    def __init__(self):
        self.open = False
        self.adjacent_mines = 0
        self.mine = False
        self.flagged = False
        self.set_value()

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

    def set_mine(self, mine: bool) -> None:
        self.mine = mine

    def set_flagged(self, flagged: bool) -> None:
        self.flagged = flagged

    def increase_adjacent_mines(self) -> None:
        self.adjacent_mines += 1

    def set_value(self):
        if not self.open:
            self.value = self.closed
        elif self.flagged:
            self.value = self.flag
        elif self.mine:
            self.value = self.bomb
        elif self.adjacent_mines > 0:
            self.value = str(self.adjacent_mines)
        else:
            self.value = self.blank

    def get_value(self) -> str:
        return self.value
