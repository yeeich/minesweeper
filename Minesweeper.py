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

    def play_round(self):
        self.board.print_board()
        while True:
            square_chosen = input("Choose a square: ")
            if len(square_chosen) == 2:
                positions = square_chosen.split()
                if positions[0]
