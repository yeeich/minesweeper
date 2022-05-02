from Square import Square


class Board:
    easy_width = 8
    easy_height = 8
    easy_mines = 10
    hard_width = 16
    hard_height = 16
    hard_mines = 40
    col_positions = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def __init__(self, level):
        self.level = level
        if self.level == "Easy":
            self.width, self.height, self.mines = self.easy_width, self.easy_height, self.easy_mines
        else:
            self.width, self.height, self.mines = self.hard_width, self.hard_height, self.hard_mines

        self.board = [[Square()] * self.width] * self.height
        self.columns = self.col_positions[: self.width]

    def print_board(self):
        print(f"\t  {' '.join(self.columns)}")
        i = 1
        for row in self.board:
            print(f"\t{i}", end=" ")
            for square in row:
                print(square.get_value(), end=" ")
            print()
            i += 1
