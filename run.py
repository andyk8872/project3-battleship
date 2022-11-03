'''Import python libraries'''
from random import randint
import os
# import pyfiglet
from battleship_art import LOGO, WIN, LOSE, DRAW


COMP_UNSEEN_GRID = [['.']*5 for x in range(5)]
COMP_SEEN_GRID = [['.']*5 for x in range(5)]
PLAYER_SEEN_GRID = [['.']*5 for x in range(5)]
NO_OF_SHIPS = 0
COMP_SCORE = 0


def clear():
    """
    A function to clear the screen
    """
    os.system('clear')


def introduction():
    """
    Description of the game and instructions
    """
    pass


def battle_zone(board):
    """
    Create function to create game area
    """
    print('    C o l u m n')
    print('    1   2   3   4   5')
    print('   * * * * * * * * *')
    row_legend = 1
    row_text = [' ', 'R', 'O', 'W', ' ']
    for x_row, row in zip(row_text, board):
        print(x_row, row_legend,  " | ".join(row))
        row_legend += 1


def create__ships(board, NO_OF_SHIPS):
    """
    Function that creates the ships and
    places them in the game area, but not in the
    same location
    """
    pass


def find_ship_location():
    """
    A function to locate the ships
    """
    pass


def validate_location_data(input):
    """
    A function to validate player location input
    """
    pass


def get_player_location():
    """
    A function to locate players ships
    """
    pass


def comp_turn():
    """
    A function to for the computer to choose
    """
    pass


def play_again():
    """
    A function to enable a replay
    """
    pass


def main():
    """
    The main game function
    """
    pass


def get_no_of_ships():
    """
    A function to choose the number of ships
    """
    pass


def validate_ship_data(No_Of):
    """
    A function to validate player input
    """
    pass


def setup():
    """
    A function to set game parameters
    """
    pass


clear()
battle_zone(COMP_UNSEEN_GRID)
