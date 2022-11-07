'''Import python libraries'''
import os
import sys
import time
from random import randint
from battleship_art import LOGO, WIN, LOSE, DRAW


comp_unseen_grid = [['.'] * 5 for x in range(5)]
comp_seen_grid = [['.'] * 5 for x in range(5)]
player_seen_grid = [['.'] * 5 for x in range(5)]
many_ships = 0
comp_score = 0


def clear():
    """
    A function to clear the screen
    """
    os.system('clear')


def print_slow(string):
    """
    A function to print like a typewriter
    """
    for char in string:
        time.sleep(.01)
        sys.stdout.write(char)
        sys.stdout.flush()


def introduction():
    """
    Description of the game and instructions
    """
    print_slow(LOGO)
    print_slow("*-----Instructions-----*\n")
    print_slow("It's you againest the computer.\n")
    print_slow("Who can sink the most ships.\n")
    print_slow("First choose the number of ships for the battle.\n\n")


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
        print(x_row, row_legend, " | ".join(row))
        row_legend += 1


def get_no_of_ships():
    """
    A function to choose the number of ships
    """
    while True:
        no_of_ships = input("Enter the number of ships "
                            "(between 10 an 15):\nExample: 11\n")
        if validate_ship_data(no_of_ships):
            print("Data is valid")
            clear()
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
    except ValueError as e:
        clear()
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def create_ships(board, many_ships):
    """
    Function that creates the ships and
    places them in the game area, but not in the
    same location
    """
    for ship in range(many_ships):
        ship_row, ship_col = randint(0, 4), randint(0, 4)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0, 4), randint(0, 4)
        board[ship_row][ship_col] = 'X'
    return


def find_ship_location():
    """
    A function to locate the ships
    """
    while True:
        row = input("Please enter a ship row 1 - 5:\n")
        if validate_location_data(row):
            break
    while True:
        column = input("Please enter a ship column 1 - 5\n")
        if validate_location_data(column):
            clear()
            break

    return int(row) - 1, int(column) - 1


def validate_location_data(locate):
    """
    A function to validate player location input
    """
    try:
        locate = int(locate)
        if locate not in range(1, 6):
            raise ValueError(f"A number: 1 - 5 required, you entered {locate}")
    except ValueError as e:
        clear()
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True


def get_player_location():
    """
    A function to locate players ships
    """
    player_row = randint(0, 4)
    player_column = randint(0, 4)
    return player_row, player_column


def comp_turn():
    """
    A function to for the computer to choose
    """
    global comp_score
    player_row, player_column = get_player_location()
    if player_seen_grid[player_row][player_column] == 'X':
        player_seen_grid[player_row][player_column] = 'H'
        comp_score += 1
    else:
        player_seen_grid[player_row][player_column] = 'M'


def play_again():
    """
    A function to enable a replay
    """
    global comp_seen_grid, comp_unseen_grid, player_seen_grid
    while True:
        replay = input("Type 'Y' to play again\nor 'Q' to leave:\n").upper()
        if replay == 'Y':
            comp_unseen_grid = [['.'] * 5 for x in range(5)]
            comp_seen_grid = [['.'] * 5 for x in range(5)]
            player_seen_grid = [['.'] * 5 for x in range(5)]
            clear()
            setup()
        if replay == 'Q':
            clear()
            print('Goodbye')
            break
        else:
            print("Incorrect entry, type 'Y/y' to play again or 'Q/q' to Quit")


def all_scores(player_score):
    print(f"PlayerScore: {player_score}")
    print(f"Computer Score: {comp_score}\n")


def main(player, computer):
    """
    The main game function
    """
    global comp_score
    comp_score = 0
    turns = 5
    player_score = 0
    while turns > 0:
        print("\nYou have " + str(turns) + " turns remaining\n")
        # print("Computer Arena\n")
        battle_zone(comp_seen_grid)
        print("\nPlayer Arena\n")
        battle_zone(player_seen_grid)
        comp_turn()
        row, column = find_ship_location()
        if comp_seen_grid[row][column] == 'M' or \
                comp_seen_grid[row][column] == 'X':
            print("You already guessed that\n")
        elif comp_unseen_grid[row][column] == 'X':
            print('Congratulations you have hit a battleship\n')
            comp_seen_grid[row][column] = 'X'
            turns -= 1
            player_score += 1
            print(f"PlayerScore: {player_score}")
            print(f"Computer Score: {comp_score}")
        elif comp_seen_grid[row][column] == '.':
            print('Sorry,You missed\n')
            comp_seen_grid[row][column] = 'M'
            turns -= 1
            print(f"Player Score: {player_score}")
            print(f"Comp Score: {comp_score}")
        print("You have " + str(turns) + " turns remaining\n")
        print("Waiting 3 seconds before continuing")
        time.sleep(3)
        clear()
        if turns == 0:
            clear()
            print('Game Over ')
            if player_score == comp_score:
                print_slow(DRAW)
                all_scores(player_score)
                play_again()
            elif player_score > comp_score:
                print_slow(WIN)
                all_scores(player_score)
                play_again()
            elif player_score < comp_score:
                print_slow(LOSE)
                all_scores(player_score)
                play_again()
            break


def setup():
    """
    A function to set game parameters
    """
    clear()
    introduction()
    ships = get_no_of_ships()
    many_ships = int(ships)
    computer = create_ships(comp_unseen_grid, many_ships)
    player = create_ships(player_seen_grid, many_ships)
    main(player, computer)


setup()
