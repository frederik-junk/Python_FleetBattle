"""Module that contains functions to show the board, place ships etc.

Raises:
    Exception: Prints an error message depending on case, for example wrong input on coordinates
"""
import os
import random
from termcolor import colored
from colorama import init
import converter_functions

init()


def clear_console():
    """Function to clear the console for better user interface while playing"""
    os.system("cls" if os.name == "nt" else "clear")


# letterrow to show user the name of each column
letterRow = [
    "\\\\",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
]  # creating the playgroup column


def initialize_board(board):
    """Initializes the board to place ships on

    Args:
        board (List): The list of each coordinates of the board for placing ships
    """
    for i in range(10):
        row = []
        for j in range(10):
            row.append(0)
        board.append(row)


def board_loader(data, load_available):
    """Function that loads the board with its values

    Args:
        data (_type_): _description_
        load_available (int): Indicates if there is a score that can be loaded
    """
    # setting all boards as globals to allow access in all functions
    global leaked_board_1
    leaked_board_1 = []
    global leaked_board_2
    leaked_board_2 = []
    global hidden_board_1
    hidden_board_1 = []
    global hidden_board_2
    hidden_board_2 = []
    if load_available is False:
        # creating board with leaked ships for player 1 ship placing
        initialize_board(leaked_board_1)
        # creating board with leaked ships for player 2 ship placing
        initialize_board(leaked_board_2)
        # creating board with hidden ships from player 1 for game of player 2
        initialize_board(hidden_board_1)
        # creating board with hidden ships from player 2 for game of player 1
        initialize_board(hidden_board_2)
    elif load_available is True:
        # loading the boards from stored data
        leaked_board_1 = data["leaked_board_1"]
        leaked_board_2 = data["leaked_board_2"]
        hidden_board_1 = data["hidden_board_1"]
        hidden_board_2 = data["hidden_board_2"]
    else:
        print("Beim Laden des Boards ist ein Fehler aufgetreten")


def board_reset(data):
    """Function to reset the board to initial values

    Args:
        data (_type_): _description_
    """
    # reseting all boards with default values
    data["leaked_board_1"] = data["reset_board"]
    data["leaked_board_2"] = data["reset_board"]
    data["hidden_board_1"] = data["reset_board"]
    data["hidden_board_2"] = data["reset_board"]


# function to print the hole board while player is playing the game
def print_leaked_board(board):
    """
    function to print the board with visible ships
    Args:
        board (List): The board on which the ships are placed
    """
    # creates the first row with letters to locate the ship positon (horizontal)
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        # creates the first column with letters to locate the ship positon (vertical)
        print(str(i + 1).zfill(2), end="  ")  # zfill to format number  (0digit)
        # replace function to optical replace 1 = ship position, 0 = free space (water), 6 = placement blocker for following player ships
        print(
            "  ".join(
                str(elem).replace("1", "\033[37m#").replace("0", "\033[34m~").replace("6", "\033[31mX")
                for elem in row
            )
        )


# function to print the hole board while player is placing the ships
def print_hidden_board(board):
    """Function to print the board without showing the ships, so the opponent cannot see the ships of the other player

    Args:
        board (List): The board on which the ships are placed
    """
    # creates the first row with letters to locate the ship positon (horizontal)
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        # creates the first column with letters to locate the ship positon (vertical)
        print(str(i + 1).zfill(2), end="  ")  # zfill to format number  (0digit)
        # replace function to optical replace
        # 1 = ship filed but hidden (shown as water),
        # 2 = free space (water),
        # 2 = shot spot without hit,
        # 3 = shot spot with hit, 4 = eleminated ship (complete)
        print(
            "  ".join(
                str(elem).replace("1", "~").replace("0", "~").replace("2", "O").replace("3", "x").replace("4", "#")
                for elem in row
            )
        )


# function to place a ship in the right position with the right length and the right direction
def place_ship(board, ship_length, ship, shipName, counter):
    """Function to place ships on the game board

    Args:
        board (List): The board on which the ships are placed
        ship_length (int): The length of each ship
        ship (Class): The class of the ship for generating initial values depending on the type
        shipName (String): The ship name to show the user which ship has to be placed currently
        counter (int): A counter to keep track on how many ships have already been placed

    Raises:
        Exception: Prints an error message if there was a wrong input for example
    """
    if counter == 1:
        print_leaked_board(board)
    while True:
        # asking user on which position he wants to place his ship
        placement_input = input(
            f"Geben Sie eine Koordinate an, auf die die Spitze Ihres {counter}. Schiffs ({shipName}) platziert werden soll. Schiffslänge: {ship_length}.\n"
        )
        # try to find the input postion in the board (checking if it exists)
        try:
            starting_column_char = converter_functions.split_column_converter(placement_input)
            if (
                starting_column_char == 11
            ):  # eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
            starting_row_number = converter_functions.split_row(placement_input)
            if (
                starting_row_number == 11
            ):  # eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
        # if placing fails the user is asked to replace his ship
        except Exception:
            print(
                colored(
                    "Ihre Eingabe enthaelt Fehler.\n Bitte geben Sie Buchstaben zwischen A und J ein.\n Bitte geben Sie eine Zahl zwischen 1 und 10 ein.",
                    "red",
                )
            )
            print("Bitte geben Sie neue Anfangskoordinaten ein (z.B.: A3).")
            continue

        # initialize row and column number as int to avoid overflow
        starting_row_number = int(starting_row_number)
        starting_column_char = int(starting_column_char)

        # checking if position is already filled with a ship and asking user to replace the ship
        if board[starting_row_number][starting_column_char] == 1:
            print(
                colored(
                    f"Sie können an dieser Stelle {placement_input} kein Schiff platzieren, da dort schon ein Schiff liegt.",
                    "red",
                )
            )
            continue
        # chcking if wished ship position is already blocked because of another nearby ship and asking user to replacer the ship
        if board[starting_row_number][starting_column_char] == 6:
            print(
                colored(
                    f"Sie können hier {placement_input} kein Schiff platzieren, da es zu nah an einem anderen Schiff liegt.",
                    "red",
                )
            )
            continue
        # if all rules are checked then confirming the chosen position
        print(colored(f"Die Spitze des Schiffes liegt auf {placement_input}", "cyan"))
        # placing the ship in the right direction
        if (
            ship_direction(
                board, ship_length, starting_row_number, starting_column_char, ship
            )
            is True
        ):
            continue
        break
    # print_leaked_board(board)
    # DELETE if Positions for ships are available
    # placing the ship in the right direction
    # ship_direction(board, ship_length, starting_row_number, starting_column_char)


# user function to choose the direction of the current ship
def ship_direction(board, ship_length, starting_row_number, starting_column_char, ship):
    """Function to set the direction of the ship that is to be placed

    Args:
        board (List): The board on which ships are being placed
        ship_length (int): The individual ship length
        starting_row_number (int): A number to indicate the current row
        starting_column_char (char): A char to indicate the current column
        ship (Class): The class of each ships to provide inital values

    Returns:
        Boolean: Returns a True or False value
    """
    game_mode = 2
    direction_input = input(
        "Geben Sie über die Tasten [w][a][s][d] die Ausrichtung des Schiffes an.\n"
    )
    if (
        converter_functions.direction_converter(
            board,
            ship_length,
            starting_row_number,
            starting_column_char,
            direction_input,
            game_mode,
            ship,
        )
        is True
    ):
        return True  # is send back to set another coordinate
    clear_console()
    print(colored("Ihr Schiff wurde platziert!", "green"))
    print_leaked_board(board)
    return False


def cpu_ship_direction(board, ship_length, starting_row_number, starting_column_char, ship):
    """Function to set the direction of the ship that is to be placed for the computer opponent

    Args:
        board (List): The board on which ships are being placed
        ship_length (int): The individual ship length
        starting_row_number (int): A number to indicate the current row
        starting_column_char (char): A char to indicate the current column
        ship (Class): The class of each ships to provide inital values

    Returns:
        Boolean: Returns a True or False value
    """
    game_mode = 1
    # get a random direction for the ship to be placed in
    while True:
        cpu_direction = random.randint(0, 3)
        match cpu_direction:
            case 0:
                cpu_direction = "w"
            case 1:
                cpu_direction = "a"
            case 2:
                cpu_direction = "s"
            case 3:
                cpu_direction = "d"
            case _:
                print(
                    "oh something went wrong"
                )  # eventuelle Schleife neue Zahl generieren
        possible_positions = converter_functions.direction_converter(
            board,
            ship_length,
            starting_row_number,
            starting_column_char,
            cpu_direction,
            game_mode,
            ship,
        )
        if possible_positions is True:
            return 11
        break


# function to add the blockers so that ships cant be placed next to the ship


# function for the cpu opponent to place the a ship
def cpu_place_ship(board, ship_length, ship):
    """Function that is responsible for placing the CPU ships

    Args:
        board (List): The board on which ships are being placed
        ship_length (int): The individual ship length
        ship (Class): The class of each ships to provide inital values
    """
    while True:
        starting_row_number = random.randint(0, 9)
        starting_column_char = random.randint(0, 9)
        # cpu places the ship with the random startig coordinates
        if (
            cpu_ship_direction(
                board, ship_length, starting_row_number, starting_column_char, ship
            )
            == 11
        ):
            continue
        print_leaked_board(board)
        break
