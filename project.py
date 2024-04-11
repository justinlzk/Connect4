from tabulate import tabulate
from itertools import cycle
from random import shuffle
import os

from board import Board
from player import Player
# Justin Li
# CS50P Final Project: Connect 4


def main():
    print("This is Justin's CS50P Final Project: Connect 4")
    key = input("Enter 'q' for quick start or any other key to continue. ").lower().strip()
    game = Game(quick_start=key == "q")
    game.play()

if __name__ == "__main__":
    main()
