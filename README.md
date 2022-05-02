# Minesweeper Game

- There are 2 levels called Easy and Hard.
- Easy level has 8x8 squares with 10 mines and Hard has 16x16 squares with 40 mines.
- The goal of Minesweeper is to uncover all the squares on a grid that do not contain mines without being "blown up" by choosing a square with a mine underneath.
- You will be prompted to select the level of the game, then you will start playing by choosing a board's square with the following syntax: '<column><row>'. So choosing B4 means the square on column B and row 4.
- The first square chosen will be always blank, and then mines are assigned randomly to other squares. The game starts at this point.
- After choosing a square you will be given the option to select an action.
- There are only two actions: open or flag the square.
- If you choose to open the square and it has a mine underneath, you will automatically lose and all the mines will be shown.
- Otherwise, it will be open and show how many adjacent mines that square has, if there are no adjacent mines the square will be blank (a large number of blank squares [bordering 0 mines] may be revealed in one go if they are adjacent to each other).
- On the other hand, in order to help the player avoid hitting a mine, the location of a suspected mine can be marked y flagging it.
- The game is won once all blank or numbered squares have been uncovered by the player without hitting a mine; any remaining mines not identified by flags are automatically flagged.
- However, in the event that a game is lost and the player had mistakenly flagged a safe square, that square will appear with an X (denoting the square as safe).