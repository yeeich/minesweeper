from Board import Board


class Minesweeper:
    levels = {1: "Easy", 2: "Hard"}

    def __init__(self):
        print("The game has two levels: Easy (1), Hard (2)")
        while True:
            l = input("Choose your level [1/2]: ")
            l = int(l) if l in "12" else None
            if l in self.levels:
                self.level = self.levels[l]
                print(f"You chose {self.level}.")
                while True:
                    check = input("Do you want to continue? [y/n]: ")
                    if check.lower() in ["y", "n"]:
                        break
                if check == "y":
                    break

        self.board = Board(self.level)
        self.lose = False
        self.round = 0

    def print_board(self):
        print(f"\n\t {' '.join(self.board.get_columns())}")
        i = 1
        for row in self.board.get_board():
            print("\t", end=" ")
            for square in row:
                print(square.get_value(), end=" ")
            print(i)
            i += 1
        print()

    def play_round(self):
        self.print_board()
        while True:
            square_chosen = input("Choose a square: ")
            if len(square_chosen) in [2, 3]:
                position = [square_chosen[0].upper(), int(square_chosen[1:])]
                if position[0] in self.board.get_columns() and position[1] in self.board.get_rows():
                    action_chosen = 1
                    if self.board.get_square(position).get_open():
                        print(f"{square_chosen.upper()} is already open.")
                        continue
                    if self.round == 0:
                        self.board.place_mines(position)
                    while self.round > 0:
                        action_chosen = input("You want to open (1) or flag (2) the square? ")
                        if int(action_chosen) in [1, 2]:
                            break
                    self.board.square_played(position, int(action_chosen))
                    break
        self.round += 1
