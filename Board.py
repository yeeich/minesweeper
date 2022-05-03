from random import randint
from Square import Square

col_positions = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
l2i = dict(zip(col_positions, range(len(col_positions))))
easy_width = 8
easy_height = 8
easy_mines = 10
hard_width = 16
hard_height = 16
hard_mines = 40


class Board:
    def __init__(self, level):
        self.level = level
        if self.level == "Easy":
            self.width, self.height, self.mines = easy_width, easy_height, easy_mines
        else:
            self.width, self.height, self.mines = hard_width, hard_height, hard_mines

        self.board = [[Square() for i in range(self.width)] for j in range(self.height)]
        self.columns = col_positions[: self.width]
        self.rows = list(range(1, self.height + 1))

    def get_columns(self) -> list:
        return self.columns

    def get_board(self) -> list:
        return self.board

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_mines(self) -> int:
        return self.mines

    def get_rows(self) -> list:
        return self.rows

    def get_square(self, position: list) -> Square:
        x = l2i[position[0]]
        y = position[1] - 1
        return self.board[y][x]

    def square_played(self, position: list, action: int) -> None:
        x = l2i[position[0]]
        y = position[1] - 1
        square = self.board[y][x]
        square.set_open(True)
        if action == 2:
            square.set_flagged(True)

    def place_mines(self, position: list) -> None:
        for _ in range(self.mines):
            while True:
                x = randint(0, self.width - 1)
                y = randint(0, self.height - 1)
                square = self.board[y][x]
                if (l2i[position[0]] != x or position[1] - 1 != y) and not square.get_mine():
                    break
            square.set_mine(True)
