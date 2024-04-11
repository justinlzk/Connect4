from tabulate import tabulate

tabulate.WIDE_CHARS_MODE = True


class Board:

    CONSECUTIVE_PIECES_TO_WIN = 4

    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        self.board = [["" for _ in range(cols)] for _ in range(rows)]  # board with actual pieces
        self.board.append([f"{i}" for i in range(1, cols+1)]) # bottom row with column numbers

    def __str__(self):
        board = tabulate(self.board ,
                          tablefmt="simple_grid", stralign="center") + '\n'
        return board

    def drop_piece(self, player, col):
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][col] == "":
                break
        self.__set_piece(player, i, col)

    def __set_piece(self, player, row, col):
        self.board[row][col] = player.symbol

    def win(self, player):
        return self.vertical_winner(player) or self.horizontal_winner(player) or self.diagonal_winner(player)

    def vertical_winner(self, player):
        for i in range(self.cols):
            longest = 0
            for j in range(self.rows):
                if self.board[j][i] == player.symbol:
                    longest += 1
                else:
                    longest = 0
                if longest == Board.CONSECUTIVE_PIECES_TO_WIN:
                    return True
        return False

    def horizontal_winner(self, player):
        for i in range(self.rows):
            longest = 0
            for j in range(self.cols):
                if self.board[i][j] == player.symbol:
                    longest += 1
                else:
                    longest = 0
                if longest == Board.CONSECUTIVE_PIECES_TO_WIN:
                    return True
        return False

    def diagonal_winner(self, player):
        return self.right_diagonal_win(player) or self.left_diagonal_win(player)

    def right_diagonal_win(self, player):
        for i in range(Board.CONSECUTIVE_PIECES_TO_WIN - 1, self.rows):
            for j in range(self.cols - Board.CONSECUTIVE_PIECES_TO_WIN):
                if (self.board[i][j] == player.symbol and
                    self.board[i - 1][j + 1] == player.symbol and
                    self.board[i - 2][j + 2] == player.symbol and
                        self.board[i - 3][j + 3] == player.symbol):
                    return True
        return False

    def left_diagonal_win(self, player):
        for i in range(self.rows - Board.CONSECUTIVE_PIECES_TO_WIN + 1):
            for j in range(self.cols - Board.CONSECUTIVE_PIECES_TO_WIN + 1):
                if (self.board[i][j] == player.symbol and
                    self.board[i + 1][j + 1] == player.symbol and
                    self.board[i + 2][j + 2] == player.symbol and
                        self.board[i + 3][j + 3] == player.symbol):
                    return True
        return False

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, rows):
        if rows < 5:
            raise ValueError("There must be at least 5 rows")
        elif rows > 10:
            raise ValueError("There can be at most 10 rows")
        self._rows = rows

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, cols):
        if cols < 5:
            raise ValueError("There must be at least 5 columns")
        elif cols > 10:
            raise ValueError("There can be at most 10 columns")
        self._cols = cols


    def set_board(self, board):  # for testing purposes
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])


    def is_full(self):
        for piece in self.board[0]:
            if not piece:
                return False
        return True


    def col_is_full(self, col):
        return bool(self.board[0][col].strip())
