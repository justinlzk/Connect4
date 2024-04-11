from itertools import cycle
from random import shuffle
import os

from board import Board
from player import Player


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self, quick_start=False):
        clear()
        self.quick_start = quick_start
        self.player1, self.player2 = self.get_players()
        self.players = [self.player1, self.player2]
        self.rows, self.cols = self.get_dimensions()
        self.board = Board(self.rows, self.cols)

    def get_players(self):
        if self.quick_start:
            return Player(1, "Player 1", "RED"), Player(2, "Player 2", "YELLOW")

        p1_name = input("Player 1's Name: ").strip()
        while True:
            print(Player.colors())
            p1_color = input("Player 1's Color: ").upper().strip()
            try:
                p1 = Player(1, p1_name, p1_color)
            except ValueError as ve:
                print(ve)
            else:
                break

        clear()

        p2_name = input("Player 2's Name: ").strip()
        while p2_name and p1_name == p2_name:
            print("Player 2's name cannot be the same as Player 1's name")
            p2_name = input("Player 2's Name: ").strip()

        while True:
            print(Player.colors())
            p2_color = input("Player 2's Color: ").upper().strip()
            while p1_color == p2_color:
                print("Player 2's color cannot be the same as Player 1's color")
                print(Player.colors())
                p2_color = input("Player 2's Color: ").upper().strip()
            try:
                p2 = Player(2, p2_name, p2_color)
            except ValueError as ve:
                print(ve)
            else:
                break
        clear()
        return p1, p2

    def get_dimensions(self):
        if self.quick_start:
            return 6, 7

        while True:
            rows = input("Number of Rows: ")
            cols = input("Number of Columns: ")
            try:
                rows = int(rows)
                cols = int(cols)
                Board(rows, cols)
            except ValueError as ve:
                print(ve)
            else:
                clear()
                return rows, cols

    def move(self, player):
        while True:
            col = input(f"{player}'s move\nColumn: ").strip()
            try:
                col = int(col) - 1
                if col < 0 or col >= self.cols or self.board.col_is_full(col):
                    raise ValueError
            except ValueError:
                print("Invalid Column")
            else:
                break
        clear()
        self.board.drop_piece(player, col)
        print(self.board)

    def winner_exists(self):
        return self.board.win(self.player1) or self.board.win(self.player2)

    def player_order(self):
        players = cycle(iter(self.players))
        while True:
            yield next(players)

    def play(self):
        shuffle(self.players)
        order = self.player_order()

        starting_player = next(order)
        print(starting_player, "starts!")
        print(self.board)
        self.move(starting_player)

        while not self.board.is_full():
            current_player = next(order)
            self.move(current_player)
            if self.winner_exists():
                break
        else:
            print(f"It's a Tie!")
            return None


        if self.board.win(self.player1):
            print(f"{self.player1} wins!")
        elif self.board.win(self.player2):
            print(f"{self.player2} wins!")

