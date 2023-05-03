"""Module contains functions to define the ship placement on the board"""
from termcolor import colored
from colorama import init
import blocker_functions

init()


# own exception class
class WrongPlacement(Exception):
    """Used in case of wrong ship placement"""

def direction_converter(
    board, ship_length, starting_row_number, starting_column_char, direction, game_mode, ship
):
    """defines direction of placed ship, based on the tip of the ship/user input"""

    j = 0  # count variable for later use
    position_tupel_list = (
        []
    )  # saves tupels with position of object
    match direction:
        case "w":
            try:  # exception in case that the ship is placed out of bounce in the given direction
                between_starting_row_number = starting_row_number - ship_length
                if between_starting_row_number <= 0:
                    if game_mode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                # changes every index of the placed ship to 1 on board
                while j < ship_length:
                    if board[starting_row_number][starting_column_char] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[starting_row_number][starting_column_char] == 6:
                        raise WrongPlacement("laeuft in Blocker")
                    position_tupel = (starting_row_number, starting_column_char)
                    # stores ship position by adding all position tuples to position_tupel_list
                    position_tupel_list.append(position_tupel)
                    starting_row_number = starting_row_number - 1
                    j += 1
                    if j == ship_length:
                        for tupel in position_tupel_list:
                            row_number, column_number = tupel
                            board[row_number][column_number] = 1
                blocker_functions.add_placement_blocker(board, position_tupel_list)
                ship.set_position(position_tupel_list)
                return False
            except WrongPlacement as placement_error:
                if game_mode == 2:
                    if str(placement_error) == "laeuft aus Spielfeld":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff aus dem Spielfeld",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in anderes Schiff":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in eine anderes Schiff.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in Blocker":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in einen verbotenen Bereich.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    else:
                        print(str(placement_error))
                        position_tupel_list.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.", "cyan"))
                    print(
                        colored(
                            "Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und eine neue Ausrichtung.",
                            "cyan",
                        )
                    )
                    return True
                return True
        case "a":
            try:  # exception in case that the ship is placed out of bounce in the given direction
                between_starting_column_char = starting_column_char - ship_length
                if between_starting_column_char < 0:
                    if game_mode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                while j < ship_length:
                    if board[starting_row_number][starting_column_char] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[starting_row_number][starting_column_char] == 6:
                        raise WrongPlacement("laeuft in Blocker")
                    position_tupel = (starting_row_number, starting_column_char)
                    # stores ship position by adding all position tuples to position_tupel_list
                    position_tupel_list.append(position_tupel)
                    starting_column_char -= 1
                    j += 1
                    # changes every index of the placed ship to 1 on board
                    if j == ship_length:
                        for tupel in position_tupel_list:
                            row_number, column_number = tupel
                            board[row_number][column_number] = 1
                blocker_functions.add_placement_blocker(board, position_tupel_list)
                ship.set_position(position_tupel_list)
                return False
            except WrongPlacement as placement_error:
                if game_mode == 2:
                    if str(placement_error) == "laeuft aus Spielfeld":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff aus dem Spielfeld",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in anderes Schiff":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in eine anderes Schiff.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in Blocker":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in einen verbotenen Bereich.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    else:
                        print(str(placement_error))
                        position_tupel_list.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.", "cyan"))
                    print(
                        colored(
                            "Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und eine neue Ausrichtung.",
                            "cyan",
                        )
                    )
                    return True
                return True
        case "s":
            try:  # exception in case that the ship is placed out of bounce in the given direction
                between_starting_row_number = starting_row_number + ship_length
                if between_starting_row_number > 10:
                    if game_mode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                while j < ship_length:
                    if board[starting_row_number][starting_column_char] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[starting_row_number][starting_column_char] == 6:
                        raise WrongPlacement("laeuft in Blocker")
                    position_tupel = (starting_row_number, starting_column_char)
                    # stores ship position by adding all position tuples to position_tupel_list
                    position_tupel_list.append(position_tupel)
                    starting_row_number += 1
                    j += 1
                    # changes every index of the placed ship to 1 on board
                    if j == ship_length:
                        for tupel in position_tupel_list:
                            row_number, column_number = tupel
                            board[row_number][column_number] = 1
                blocker_functions.add_placement_blocker(board, position_tupel_list)
                ship.set_position(position_tupel_list)
                return False
            except WrongPlacement as placement_error:
                if game_mode == 2:
                    if str(placement_error) == "laeuft aus Spielfeld":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff aus dem Spielfeld",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in anderes Schiff":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in eine anderes Schiff.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in Blocker":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in einen verbotenen Bereich.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    else:
                        print(str(placement_error))
                        position_tupel_list.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.", "cyan"))
                    print(
                        colored(
                            "Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und eine neue Ausrichtung.",
                            "cyan",
                        )
                    )
                    return True
                return True
        case "d":
            try:  # exception in case that the ship is placed out of bounce in the given direction
                between_starting_row_number = starting_column_char + ship_length
                if between_starting_row_number > 10:
                    if game_mode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                while j < ship_length:
                    if board[starting_row_number][starting_column_char] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[starting_row_number][starting_column_char] == 6:
                        raise WrongPlacement("laeuft in Blocker")
                    position_tupel = (starting_row_number, starting_column_char)
                    # stores ship position by adding all position tuples to position_tupel_list
                    position_tupel_list.append(position_tupel)
                    starting_column_char += 1
                    j += 1
                    # changes every index of the placed ship to 1 on board
                    if j == ship_length:
                        for tupel in position_tupel_list:
                            row_number, column_number = tupel
                            board[row_number][column_number] = 1
                ship.set_position(position_tupel_list)
                blocker_functions.add_placement_blocker(board, position_tupel_list)
                return False
            except WrongPlacement as placement_error:
                if game_mode == 2:
                    if str(placement_error) == "laeuft aus Spielfeld":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff aus dem Spielfeld",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in anderes Schiff":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in eine anderes Schiff.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    elif str(placement_error) == "laeuft in Blocker":
                        print(
                            colored(
                                "In dieser Richtung laeuft das Schiff in einen verbotenen Bereich.",
                                "red",
                            )
                        )
                        position_tupel_list.clear()
                    else:
                        print(str(placement_error))
                        position_tupel_list.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.", "cyan"))
                    print(
                        colored(
                            "Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und eine neue Ausrichtung.",
                            "cyan",
                        )
                    )
                    return True
                return True
        case _:
            if game_mode == 2:
                print(
                    "Bitte bestimmen Sie mithilfe der Tasten [w][a][s][d] die Ausrichtung des Schiffes."
                )
                return True
            return True
    # setting of the ship position
    # ship.set_position(position_tupel_list)


def split_column_converter(placement_input):
    """splits input into column and row indices
    returns number of current column of the to be placed ship"""
    starting_column_char = str(
        placement_input[0]
    )  # extracts first char of the user input
    """try:
        if starting_column_char.isalpha() is False:
            raise ValueError
        starting_column_char = starting_column_char.upper()
        # match case to convert the letters into column idexes
        match starting_column_char:
            case "A":
                starting_column_char = 0
            case "B":
                starting_column_char = 1
            case "C":
                starting_column_char = 2
            case "D":
                starting_column_char = 3
            case "E":
                starting_column_char = 4
            case "F":
                starting_column_char = 5
            case "G":
                starting_column_char = 6
            case "H":
                starting_column_char = 7
            case "I":
                starting_column_char = 8
            case "J":
                starting_column_char = 9
            case _:
                print("Bitte geben Sie Buchstaben zwischen A und J ein.\n")
                print("Bitte geben Sie eine neue Startposition an.\n")
                starting_column_char = 11
                return starting_column_char
            return starting_column_char
            """
    try:
        return ord(starting_column_char) - 65
    except ValueError as value_error:
        print(str(value_error))
        print(
            colored(
                "Ihre Eingabe enthaelt Fehler. Bitte geben Sie erst den Buchstaben und dann die Zahl an.",
                "red",
            )
        )
        print("Geben Sie bitte die Anfangskoordinaten erneut an (z.B.: A3).")
        starting_column_char = 11
        return starting_column_char


def split_row(placement_input):
    """splits input into rows,
    returns number of current row of the to be placed ship"""
    try:
        starting_row_number = int(placement_input[1:])
        # extracts rest of the user input
        if 0 < starting_row_number <= 10:
            return starting_row_number - 1

        raise ValueError("Ihre Angabe liegt außerhalb vom Spielfeld")
    except ValueError:
        starting_row_number = 11
        return starting_row_number
