from random import randint

closed = "\u25a0"
bomb = "\u002a"  # "\U0001F4A3"
blank = "\u25a1"
flag = "\u2691"


class Square:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.value = closed

    def __repr__(self) -> str:
        return f"Square({self.row},{self.col})"


class Board:
    column_names = list("ABCDEFGHIJKLMNOP")
    column_values = dict(zip(column_names, range(len(column_names))))

    def __init__(self, level) -> None:
        self.size = 8 if level == "easy" else 16
        self.num_mines = 10 if level == "easy" else 40
        self.columns = self.column_names[: self.size]
        self.rows = list(range(1, self.size + 1))
        self.board = [[Square(r, c) for c in range(len(self.columns))] for r in range(len(self.rows))]
        self.visible_board = [[closed for c in range(len(self.columns))] for r in range(len(self.rows))]
        self.squares_played = []
        self.squares_flagged = []

    def get_coordinates(self, location: list) -> tuple:
        return (location[1] - 1, self.column_values[location[0]])

    def get_square(self, coordinates: tuple) -> Square:
        row, col = coordinates
        return self.board[row][col]

    def adjacent_squares(self, square: Square, complete: bool) -> list:
        row, col = square.row, square.col
        squares = []
        for r in range(max(0, row - 1), min(self.size, row + 2)):
            for c in range(max(0, col - 1), min(self.size, col + 2)):
                if not complete and (r, c) == (row, col):
                    continue
                squares.append(self.board[r][c])
        return squares

    def place_mines(self, square: Square) -> None:
        square.value = blank
        mines_planted = 0
        adjacent_squares = self.adjacent_squares(square, True)
        while mines_planted < self.num_mines:
            loc = randint(0, self.size**2 - 1)
            row, col = loc // self.size, loc % self.size
            random_square = self.board[row][col]
            if random_square in adjacent_squares or random_square.value == bomb:
                continue
            random_square.value = bomb
            mines_planted += 1

    def assign_adjacent_mines(self, square: Square) -> None:
        for row in self.board:
            for sq in row:
                adjacent_mines = 0
                if (sq.row, sq.col) == (square.row, square.col) or sq.value != closed:
                    continue
                for adjacent_square in self.adjacent_squares(sq, False):
                    if adjacent_square.value == bomb:
                        adjacent_mines += 1
                sq.value = adjacent_mines if adjacent_mines > 0 else blank

    def flag_square(self, coordinates: tuple) -> None:
        row, col = coordinates
        self.visible_board[row][col] = flag
        if self.board[row][col] not in self.squares_flagged:
            self.squares_flagged.append(self.board[row][col])

    def play_square(self, coordinates: tuple) -> None:
        row, col = coordinates
        square = self.board[row][col]
        if square in self.squares_flagged:
            self.squares_flagged.remove(square)
        self.squares_played.append(square)
        if square.value == bomb:
            return False
        if isinstance(square.value, int) and square.value > 0:
            return True

        for adjacent_square in self.adjacent_squares(square, False):
            if adjacent_square in self.squares_played:
                continue
            row_col = (adjacent_square.row, adjacent_square.col)
            self.play_square(row_col)

        return True

    def __repr__(self) -> str:
        string = f"\n\t  {'  '.join(self.columns)}\n"
        i = 1
        for r in range(len(self.rows)):
            string += "\t "
            for c in range(len(self.columns)):
                if self.board[r][c] in self.squares_played:
                    string += f"|{self.board[r][c].value}|"
                else:
                    string += f"|{self.visible_board[r][c]}|"
            string += f"  {i}\n"
            i += 1
        string += "\n"
        return string

    def print_board(self, board: list) -> None:
        print(f"\n\t  {'  '.join(self.columns)}")
        i = 1
        for row in board:
            print("\t", end=" ")
            for square in row:
                print(f"|{square.value}|", end="")
            print(f"  {i}")
            i += 1
        print()


class Minesweeper:
    def __init__(self) -> None:
        level = self.ask_level()
        self.board = Board(level)
        self.round = 0

    @staticmethod
    def ask_level() -> str:
        while True:
            level = input("Choose your level [easy/hard]: ").lower()
            if level in ["easy", "hard"]:
                print(f"You chose {level}.")
                while True:
                    sure = input("Do you want to continue? [yes/no]: ").lower()
                    if sure in ["yes", "no"]:
                        break
                if sure == "yes":
                    break
        return level

    def play(self):
        keep_playing = True
        while len(self.board.squares_played) < self.board.size**2 - self.board.num_mines:
            print(self.board)
            while True:
                square_chosen = input("Choose a square (e.g. a4): ")
                if len(square_chosen) not in [2, 3]:
                    continue
                try:
                    location = [square_chosen[0].upper(), int(square_chosen[1:])]
                except ValueError:
                    continue
                valid_coord = all([location[0] in self.board.columns, location[1] in self.board.rows])
                if not valid_coord:
                    continue
                coordinates = self.board.get_coordinates(location)
                square = self.board.get_square(coordinates)
                if square not in self.board.squares_played:
                    break
                print(f"{square_chosen.upper()} is already open.")

            if self.round == 0:
                self.board.place_mines(square)
                self.board.assign_adjacent_mines(square)
                action_chosen = 1

            while self.round > 0:
                action_chosen = input("You want to open (1) or flag (2) the square? ")
                if action_chosen in "12" and len(action_chosen) == 1:
                    action_chosen = int(action_chosen)
                    break

            if action_chosen == 2:
                self.board.flag_square(coordinates)
            elif action_chosen == 1:
                play_square = "yes"
                if square in self.board.squares_flagged:
                    while True:
                        play_square = input(
                            f"Square in {square_chosen.upper()} is flagged, "
                            "you want to unflagged it and open it? [yes/no]: "
                        )
                        if play_square in ["yes", "no"]:
                            break

                if play_square == "no":
                    continue
                keep_playing = self.board.play_square(coordinates)
                if not keep_playing:
                    break
            self.round += 1

        print(self.board)
        if keep_playing:
            print("Congratulations!!! You won!")
        else:
            print("Game Over!!! You lost!")
