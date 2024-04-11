# Connect 4
#### Video Demo:  https://youtu.be/CTNKIxYwL9o
#### Description: Connect 4 in Python for the terminal.

#### board.py
board.py contains the Board class, which is representative of a connect 4 board. The constructor takes two arguments, the number of rows (with a default value of 6), and the number of columns (with a default value of 7). If the user decides to create a custom board size, they can do so as long as there are at least 5 rows or columns and at most 10 rows or columns. A ValueError will be raised by their respective setters if either the number of rows or columns does not follow these rules. In addition to having rows and columns, the Board class also has a 2D array to represent the board. The board is used to display the current game state to the terminal with each player's pieces (colors) every time a player makes a move. board.py also contains several methods(vertical_winner, horizontal_winner, right_diagonal_winner, and left_diagonal_winner) that use iteration to check for wins every time a player makes a move. Lastly, there is a col_is_full function that checks whether a certain column is full so that a player cannot place a piece in that column.

#### game.py
game.py contains the Game class, which is representative of a Connect 4 game. When a game is initialized, the Game class gets the players' names and their pieces(colors), as well as the chosen dimensions of the board. The game then creates the board and allows the players to play until the end(a win or a tie). Optionally, players have the option to "quick start" and skip over the prompts for player names and colors and board dimensions. Instead, players are given default names of Player 1 and Player 2, default colors of Red(🔴) and Yellow(🟡), and a default 6x7 board.

#### player.py
player.py contains the Player class, which is representative of a player. The constructor takes three arguments, a player number, a player name, and a player color. In player.py also exists a global colors variable which contains a dictionary of colors (names) and pieces(emoji representations). If the player chooses not to enter a name when not in quick start, a default name of P1 or P2 (depending on their number). On the other hand, if the player enters an invalid color, the color setter will raise a ValueError. Lastly, there is a class method that returns available colors (have not been chosen yet).

#### project.py
project.py is relatively simple and only has one main function. project.py  first imports the Game class from game.py. In the main function, the user is prompted for whether they want to quickly start, and then a game is initiated with their choice.

#### test_project.py
test_project.py contains the TestBoard class, which contains a series of tests for different winning conditions. Tests are included to ensure all four win cases (vertical, horizontal, right diagonal, and left diagonal) can be detected. Lastly, test_project.py tests col_is_full so that players won't be able to drop pieces in full columns as well as is_full to detect ties.

