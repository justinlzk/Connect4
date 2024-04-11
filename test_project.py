from board import Board
from player import Player


class TestBoard:
    board = Board()
    p1 = Player(1, "Player 1", "RED")
    p2 = Player(2, "Player 2", "YELLOW")

    def test_vertical_winner(self):
        board1 = [["", "",  "",    "",  "",  "",   ""],
                  ["", "",  "🔴",  "",   "",  "",   ""],
                  ["", "",  "🔴",  "",   "",  "",   ""],
                  ["", "",  "🔴",  "🔴", "",   "",  ""],
                  ["", "",  "🔴",  "🟡", "🟡", "🟡", ""],
                  ["", "🔴", "🟡", "🟡", "🟡", "🔴", ""]]
        TestBoard.board.set_board(board1)
        assert TestBoard.board.vertical_winner(TestBoard.p1) == True

        board2 = [["",  "",   "",   "",  "", "", "", ""],
                  ["",  "",   "🔴", "",  "", "", "", ""],
                  ["",  "",   "🟡", "🟡",  "🔴", "", "", ""],
                  ["",  "🟡", "🟡",  "🔴", "🟡", "🔴", "", ""],
                  ["🔴", "🔴", "🟡", "🟡", "🟡", "🔴", "🔴", ""]]
        TestBoard.board.set_board(board2)
        assert TestBoard.board.vertical_winner(TestBoard.p2) == False

    def test_horizontal_winner(self):
        board1 = [["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "🟡", "🟡", "", "", "", ""],
                  ["🔴", "🔴", "🔴", "🔴", "🟡", "", ""]]
        TestBoard.board.set_board(board1)
        assert TestBoard.board.horizontal_winner(TestBoard.p1) == True

    def test_right_diagonal_win(self):
        board1 = [["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "🔴", ""],
                  ["", "", "", "", "🔴", "🟡", "🔴"],
                  ["", "", "", "🔴", "🔴", "🟡", "🟡"],
                  ["", "", "🔴", "🟡", "🟡", "🟡", "🔴"]]
        TestBoard.board.set_board(board1)
        assert TestBoard.board.right_diagonal_win(TestBoard.p1) == True

        board2 = [["", "", "", "", "", "", "", ""],
                  ["🟡", "", "", "", "", "", "", ""],
                  ["🔴", "🟡", "🔴", "", "", "", "", ""],
                  ["🟡", "🔴", "🟡", "🔴", "", "", "", ""],
                  ["🔴", "🟡", "🔴", "🟡", "", "", "", ""]]
        TestBoard.board.set_board(board2)
        assert TestBoard.board.right_diagonal_win(TestBoard.p2) == False

        board3 = [["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "🔴", "", "", "", "", ""],
                  ["", "🔴", "🔴", "", "🟡", "", ""],
                  ["", "🟡", "🔴", "🔴", "🟡", "", ""],
                  ["", "🟡", "🟡", "🔴", "🔴", "🟡", ""]]
        TestBoard.board.set_board(board3)
        assert TestBoard.board.right_diagonal_win(TestBoard.p1) == False


    def test_left_diagonal_win(self):
        board1 = [["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "🔴", "", "", "", "", ""],
                  ["", "🔴", "🔴", "", "🟡", "", ""],
                  ["", "🟡", "🔴", "🔴", "🟡", "", ""],
                  ["", "🟡", "🟡", "🔴", "🔴", "🟡", ""]]
        TestBoard.board.set_board(board1)
        assert TestBoard.board.left_diagonal_win(TestBoard.p1) == True

        board2 = [["", "", "", "", "", "", "", ""],
                  ["🟡", "", "", "", "", "", "", ""],
                  ["🔴", "🟡", "🔴", "", "", "", "", ""],
                  ["🟡", "🔴", "🟡", "🔴", "", "", "", ""],
                  ["🔴", "🟡", "🔴", "🟡", "", "", "", ""]]
        TestBoard.board.set_board(board2)
        assert TestBoard.board.left_diagonal_win(TestBoard.p2) == True

        board3 = [["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "", ""],
                  ["", "", "", "", "", "🔴", ""],
                  ["", "", "", "", "🔴", "🟡", "🔴"],
                  ["", "", "", "🔴", "🔴", "🟡", "🟡"],
                  ["", "", "🔴", "🟡", "🟡", "🟡", "🔴"]]
        TestBoard.board.set_board(board3)
        assert TestBoard.board.left_diagonal_win(TestBoard.p1) == False


    def test_is_full(self):
        board1 = [["" for _ in range(self.board.cols)] for _ in range(self.board.rows)]
        TestBoard.board.set_board(board1)
        assert TestBoard.board.is_full() == False

        board2 = [["🟡", "🔴", "🟡", "🔴", "🟡", "🔴", "🟡"],
                  ["🔴", "🟡", "🔴", "🟡", "🔴", "🟡", "🔴"],
                  ["🟡", "🔴", "🟡", "🔴", "🟡", "🔴", "🟡"],
                  ["🔴", "🟡", "🔴", "🟡", "🔴", "🟡", "🔴"],
                  ["🟡", "🔴", "🟡", "🔴", "🟡", "🔴", "🟡"],
                  ["🔴", "🟡", "🔴", "🟡", "🔴", "🟡", "🔴"]]
        TestBoard.board.set_board(board2)
        assert TestBoard.board.is_full() == True

        board3 = [["", "🔴", "🟡", "🔴", "🟡", "🔴", "🟡"],
                  ["🔴", "🟡", "🔴", "🟡", "🔴", "🟡", "🔴"],
                  ["🟡", "🔴", "🟡", "🔴", "🟡", "🔴", "🟡"],
                  ["🔴", "🟡", "🔴", "🟡", "🔴", "🟡", "🔴"],
                  ["🟡", "🔴", "🟡", "🔴", "🟡", "🔴", "🟡"],
                  ["🔴", "🟡", "🔴", "🟡", "🔴", "🟡", "🔴"]]
        TestBoard.board.set_board(board3)
        assert TestBoard.board.is_full() == False


    def test_col_is_full(self):
        board1 = [["", "", "🔴", "", "", "", ""],
                  ["", "", "🟡", "", "", "", ""],
                  ["", "", "🔴", "", "🟡", "", ""],
                  ["", "", "🔴", "🟡", "🔴", "🟡", ""],
                  ["", "🔴", "🟡", "🟡", "🟡", "🔴", ""],
                  ["", "🟡", "🔴", "🔴", "🔴", "🟡", "🔴"]]
        TestBoard.board.set_board(board1)
        assert TestBoard.board.col_is_full(0) == False
        assert TestBoard.board.col_is_full(1) == False
        assert TestBoard.board.col_is_full(2) == True
        assert TestBoard.board.col_is_full(3) == False
        assert TestBoard.board.col_is_full(4) == False
        assert TestBoard.board.col_is_full(5) == False
        assert TestBoard.board.col_is_full(6) == False
