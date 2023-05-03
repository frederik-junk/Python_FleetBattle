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


def board_loader(data, loadavailable):
    """Function that loads the board with its values

    Args:
        data (_type_): _description_
        loadavailable (int): Indicates if there is a score that can be loaded
    """
    # setting all boards as globals to allow access in all functions
    global leakedBoard1
    leakedBoard1 = []
    global leakedBoard2
    leakedBoard2 = []
    global hiddenBoard1
    hiddenBoard1 = []
    global hiddenBoard2
    hiddenBoard2 = []
    if loadavailable is False:
        # creating board with leaked ships for player 1 ship placing
        initialize_board(leakedBoard1)
        # creating board with leaked ships for player 2 ship placing
        initialize_board(leakedBoard2)
        # creating board with hidden ships from player 1 for game of player 2
        initialize_board(hiddenBoard1)
        # creating board with hidden ships from player 2 for game of player 1
        initialize_board(hiddenBoard2)
    elif loadavailable is True:
        # loading the boards from stored data
        leakedBoard1 = data["leakedBoard1"]
        leakedBoard2 = data["leakedBoard2"]
        hiddenBoard1 = data["hiddenBoard1"]
        hiddenBoard2 = data["hiddenBoard2"]
    else:
        print("Beim Laden des Boards ist ein Fehler aufgetreten")


def board_reset(data):
    """Function to reset the board to initial values

    Args:
        data (_type_): _description_
    """
    # reseting all boards with default values
    data["leakedBoard1"] = data["resetBoard"]
    data["leakedBoard2"] = data["resetBoard"]
    data["hiddenBoard1"] = data["resetBoard"]
    data["hiddenBoard2"] = data["resetBoard"]


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
                str(elem).replace("1", "#").replace("0", "~").replace("6", "X")
                for elem in row
            )
        )


# function to print the hole board while player is placing the ships
def print_hidden_Board(board):
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
                str(elem)
                .replace("1", "~")
                .replace("0", "~")
                .replace("2", "O")
                .replace("3", "x")
                .replace("4", "#")
                for elem in row
            )
        )


# function to place a ship in the right position with the right length and the right direction
def placeShip(board, shipLength, ship, shipName, counter):
    """Function to place ships on the game board

    Args:
        board (List): The board on which the ships are placed
        shipLength (int): The length of each ship
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
        placementInput = input(
            f"Geben Sie eine Koordinate an, auf die die Spitze Ihres {counter}. Schiffs ({shipName}) platziert werden soll. Schiffslänge: {shipLength}.\n"
        )
        # try to find the input postion in the board (checking if it exists)
        try:
            startingColumnChar = converter_functions.splitColumnConverter(placementInput)
            if (
                startingColumnChar == 11
            ):  # eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
            startingRowNumber = converter_functions.splitRow(placementInput)
            if (
                startingRowNumber == 11
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
        startingRowNumber = int(startingRowNumber)
        startingColumnChar = int(startingColumnChar)

        # checking if position is already filled with a ship and asking user to replace the ship
        if board[startingRowNumber][startingColumnChar] == 1:
            print(
                colored(
                    f"Sie können an dieser Stelle {placementInput} kein Schiff platzieren, da dort schon ein Schiff liegt.",
                    "red",
                )
            )
            continue
        # chcking if wished ship position is already blocked because of another nearby ship and asking user to replacer the ship
        if board[startingRowNumber][startingColumnChar] == 6:
            print(
                colored(
                    f"Sie können hier {placementInput} kein Schiff platzieren, da es zu nah an einem anderen Schiff liegt.",
                    "red",
                )
            )
            continue
        # if all rules are checked then confirming the chosen position
        print(colored(f"Die Spitze des Schiffes liegt auf {placementInput}", "cyan"))
        # placing the ship in the right direction
        if (
            shipDirection(
                board, shipLength, startingRowNumber, startingColumnChar, ship
            )
            is True
        ):
            continue
        break
    # print_leaked_board(board)
    # DELETE if Positions for ships are available
    # placing the ship in the right direction
    # shipDirection(board, shipLength, startingRowNumber, startingColumnChar)


# user function to choose the direction of the current ship
def shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship):
    """Function to set the direction of the ship that is to be placed

    Args:
        board (List): The board on which ships are being placed
        shipLength (int): The individual ship length
        startingRowNumber (int): A number to indicate the current row
        startingColumnChar (char): A char to indicate the current column
        ship (Class): The class of each ships to provide inital values

    Returns:
        Boolean: Returns a True or False value
    """
    gameMode = 2
    directionInput = input(
        "Geben Sie über die Tasten [w][a][s][d] die Ausrichtung des Schiffes an.\n"
    )
    if (
        converter_functions.directionConverter(
            board,
            shipLength,
            startingRowNumber,
            startingColumnChar,
            directionInput,
            gameMode,
            ship,
        )
        is True
    ):
        return True  # is send back to set another coordinate
    clear_console()
    print(colored("Ihr Schiff wurde platziert!", "green"))
    print_leaked_board(board)
    return False


def cpuShipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship):
    """Function to set the direction of the ship that is to be placed for the computer opponent

    Args:
        board (List): The board on which ships are being placed
        shipLength (int): The individual ship length
        startingRowNumber (int): A number to indicate the current row
        startingColumnChar (char): A char to indicate the current column
        ship (Class): The class of each ships to provide inital values

    Returns:
        Boolean: Returns a True or False value
    """
    gameMode = 1
    # get a random direction for the ship to be placed in
    while True:
        cpuDirection = random.randint(0, 3)
        match cpuDirection:
            case 0:
                cpuDirection = "w"
            case 1:
                cpuDirection = "a"
            case 2:
                cpuDirection = "s"
            case 3:
                cpuDirection = "d"
            case _:
                print(
                    "oh something went wrong"
                )  # eventuelle Schleife neue Zahl generieren
        possiblePositions = converter_functions.directionConverter(
            board,
            shipLength,
            startingRowNumber,
            startingColumnChar,
            cpuDirection,
            gameMode,
            ship,
        )
        if possiblePositions is True:
            return 11
        break


# function to add the blockers so that ships cant be placed next to the ship


# function for the cpu opponent to place the a ship
def cpuPlaceShip(board, shipLength, ship):
    """Function that is responsible for placing the CPU ships

    Args:
        board (List): The board on which ships are being placed
        shipLength (int): The individual ship length
        ship (Class): The class of each ships to provide inital values
    """
    while True:
        startingRowNumber = random.randint(0, 9)
        startingColoumnChar = random.randint(0, 9)
        # cpu places the ship with the random startig coordinates
        if (
            cpuShipDirection(
                board, shipLength, startingRowNumber, startingColoumnChar, ship
            )
            == 11
        ):
            continue
        print_leaked_board(board)
        break
