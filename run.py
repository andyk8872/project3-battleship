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
    print(LOGO)
    print("*-----Intstructions-----*")
    print("It's you againest the computer.")
    print("Who can sink the others ships.")
    print("First choose the number of ships for the battle.\n")
    print('Welcome to Battleship\n')


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
    while True:
        no_of_ships = input("Enter the number here of ships \
(between 10 an 15) :\nExample: 11\n")
        if validate_ship_data(no_of_ships):
            print("Data is valid")
            break
    return no_of_ships


def validate_ship_data(no_of_ships):
    """
    A function to validate player input
    """
    try:
        no_of_ships = int(no_of_ships)
        if no_of_ships not in range(11, 15):
            raise ValueError(f"A number between 10 and 15 required, \
you provided {no_of_ships}")
    except ValueError as e_e:
        print(f"Invalid data: {e_e}, please try again.\n")
        return False
    return True


def setup():
    """
    A function to set game parameters
    """
    clear()
    introduction()
    ships = get_no_of_ships()
    # NO_OF_SHIPS = int(ships)


setup()
