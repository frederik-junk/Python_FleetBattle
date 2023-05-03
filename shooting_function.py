"""Module handles player and cpu actions

Raises:
    Exception: Prints an error messsage to inform the user
"""
import os
import random
from termcolor import colored
from colorama import init
import ship_initializer
import converter_functions
import python_game
import output_manager

cpu_memory = 0

init()

direction_lock = 0
hit_status = 0
i = 0


def clear_console():
    """Function to clear the console for better game experience
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def shooting(
    data, game_mode, current_player
):  # I would remove game_mode and current_player and would call the functions with other board wenn Spielverlauf
    # used for CPU
    """Function to process shots of the user

    Args:
        data (_type_): _description_
        game_mode (int): The game mode to indicate if there's another human player or the CPU
        current_player (int): The current player to keep track on which boards should be printed etc.

    Returns:
        winningID(int): An int value to indicate which player won the game
    """
    if game_mode == 1:
        if current_player == 1:
            shooting_iq = output_manager.user1.get_shooting_iq()
            match cpu_manager1(
                data,
                game_mode,
                current_player,
                shooting_iq,
                python_game.leaked_board_2,
                python_game.hidden_board_1,
            ):
                case 11:
                    return 1
                case None:
                    return 1
                case _:
                    next_player(data, game_mode, 1)

        elif current_player == 2:
            match playermanager(
                data,
                output_manager.user2,
                python_game.leaked_board_1,
                python_game.hidden_board_2,
                ship_initializer.opponentShips,
            ):  # has to change with number of ships
                case "won":
                    return 2  # is the winningID which should be returned to the main.
                case None:
                    return 2
                case _:
                    next_player(data, game_mode, 2)

        else:
            print("Shit")
    elif game_mode == 2:
        match current_player:
            case 1:
                if (
                    playermanager(
                        data,
                        output_manager.user1,
                        python_game.leaked_board_2,
                        python_game.hidden_board_1,
                        ship_initializer.opponentShips,
                    )
                    == "won"
                ):  # has to change with number of ships
                    winning_id = 1
                    return winning_id  # is the winningID which should be returned to the main
                next_player(data, game_mode, 1)
            case 2:
                if (
                    playermanager(
                        data,
                        output_manager.user2,
                        python_game.leaked_board_1,
                        python_game.hidden_board_2,
                        ship_initializer.playerShips,
                    )
                    == "won"
                ):  # has to change with number of ships
                    winning_id = 2
                    return winning_id  # is the winningID which should be returned to the main.
                next_player(data, game_mode, 2)
            case _:
                print("something went wrong")
    else:
        print("Shit")


def playermanager(current_player, leaked_board, hidden_board, ship_list):
    """Function that handles the shots of the player

    Args:
        data (_type_): _description_
        current_player (int): Indicates which player is currently allowed to take shots
        leaked_board (list): The visible board for the player to place shots
        hidden_board (list): The non visible board were the opponent ships are placed
        ship_list (list): The list of available ships

    Raises:
        Exception: Prints an error message on the screen

    Returns:
        String: Indication that the game is won
    """
    shooting_repeater = True
    python_game.print_hidden_board(hidden_board)
    while shooting_repeater is True:
        shooting_position = input(
            f"{current_player.get_name()} geben Sie eine Koordinate an, auf die sie schießen wollen: \n"
        )
        try:
            row = converter_functions.split_row(shooting_position)
            if row == 11:
                raise Exception("Ihre Angabe ist fehlerhaft")
            column = converter_functions.split_column_converter(shooting_position)
            if column == 11:
                raise Exception("Ihre Angabe ist fehlerhaft")
        except Exception:
            print(
                colored(
                    "Ihre Eingabe enthaelt Fehler.\n Bitte geben Sie Buchstaben zwischen A und J ein.\nBitte geben Sie eine Zahl zwischen 1 und 10 ein.",
                    "red",
                )
            )
            print("Bitte geben Sie die Anfangskoordinaten erneut ein (z.B.: A3).")
            continue
        clear_console()
        print(colored(f"Volle Feuerkraft auf {shooting_position}!", "cyan"))
        match leaked_board[row][column]:
            case 1:
                shooting_tupel = (row, column)
                for ship in ship_list:
                    name = ship.get_name()
                    print(name)
                    positions = ship.get_position()
                    position_memory = ship.get_position_memory()
                    if shooting_tupel in positions:
                        print(colored("Das war ein Treffer! Weiter so!", "green"))
                        hidden_board[row][column] = 3
                        leaked_board[row][column] = 3
                        position_memory.append(shooting_tupel)
                        ship.set_position_memory(position_memory)
                        positions.remove(shooting_tupel)
                        if len(positions) == 0:
                            current_player.increase_left_ships()
                            position_memory = ship.get_position_memory()
                            for tupel in position_memory:
                                row, column = tupel
                                hidden_board[row][column] = 4
                                # two times the same row?
                                # hidden_board[row][column] = 4
                            print(
                                colored("\nSchiff versenkt\n", "green", attrs=["blink"])
                            )
                            print(current_player.get_left_ships())
                            if current_player.get_left_ships() == 1:
                                shooting_repeater = False
                                python_game.print_hidden_board(hidden_board)
                                return "won"
                        else:
                            pass
                    else:
                        pass
                print("Sie erhalten einen weiteren Schuss\n")
                shooting_repeater = True
            case 2:
                print(
                    "Sie hatten dieses Feld bereits beschossen und einen Wassertreffer erzielt!\n"
                )
                print(
                    "Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!"
                )
                shooting_repeater = False
            case 3:
                print(
                    "Sie hatten dieses Feld bereits beschossen und sogar einen Treffer erzielt!\nIhr Schuss liefert allerdings keine neue Erkenntnis!"
                )
                print(
                    "Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!"
                )
                shooting_repeater = False
            case 4:
                print(
                    "Blubb blubb Schuss verweigert, denn hier herrscht Totenstille, Sie hatten dieses Feld bereits beschossen!\nDas Schiff an dieser Stelle ist bereits versenkt, lassen wir den Toten besser ihre verdiente Ruhe.\n"
                )
                print(
                    "Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!"
                )
                shooting_repeater = False
            case 0:
                print(colored("Das war leider ein Wassertreffer", "cyan"))
                hidden_board[row][column] = 2
                leaked_board[row][column] = 2
                python_game.print_hidden_board
                shooting_repeater = False
            case 6:
                print(colored("Das war leider ein Wassertreffer", "cyan"))
                hidden_board[row][column] = 2
                leaked_board[row][column] = 2
                python_game.print_hidden_board
                shooting_repeater = False
            case _:
                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
        python_game.print_hidden_board(hidden_board)


def random_direction():
    """Generates a random directino value for the CPU to shoot at

    Returns:
        int: The direction as an int value
    """
    direction = random.randint(0,3)
    return direction


def check_hit(hidden_board, leaked_board, cpu_memory):
    """Checks whether water or a ship was hit with the last shot

    Args:
        hidden_board (list): The non visible board where the opponent ships are placed 
        leaked_board (list): The visible board for the player to take shots
        cpu_memory (tuple): The memorized coordinates of the CPU player

    Returns:
        int: A coordinate which has been shot at
    """
    row, column = cpu_memory
    match leaked_board[row][column]:
        case 0:
            print(colored("Der Computer erzielt einen Wassertreffer", "cyan"))
            hidden_board[row][column] = 2
            return leaked_board[row][column]

        case 6:
            print(colored("Der Computer erzielt einen Wassertreffer", "cyan"))
            hidden_board[row][column] = 2
            leaked_board[row][column] = 0
            return leaked_board[row][column]

        case 1:
            shooting_tupel = cpu_memory
            for ship in ship_initializer.playerShips:
                position_memory = ship.get_position_memory()
                postitions = ship.get_position()
                if shooting_tupel in postitions:
                    print(
                        colored("Der Computer hat eines Ihrer Schiffe getroffen", "red")
                    )
                    hidden_board[row][column] = 3
                    position_memory.append(shooting_tupel)
                    ship.set_position_memory(position_memory)
                    postitions.remove(shooting_tupel)
                    # ship is sunk
                    if len(postitions) == 0:
                        position_memory = ship.get_position_memory()
                        for tupel in position_memory:
                            row, column = tupel
                            hidden_board[row][column] = 4
                        shooting_iq = 0
                        output_manager.user1.set_shooting_iq(shooting_iq)
                        print(colored("Der Computer hat ein Schiff versenkt", "red"))
                        output_manager.user1.increase_left_ships()
                        if output_manager.user1.get_left_ships() == 1:
                            all_hit = 11  # 11 is the number which determines that the cpu won (for the winning ID)
                            return all_hit
                    else:
                        return leaked_board[row][column]
        case _:
            print("something went terribly wrong")


def first_position(board):
    """Decides which coordinates are not hit currently

    Args:
        board (list): The game board on which the ships are placed

    Returns:
        int: _description_
    """
    while True: #get correct shooting coordinates on which he didnt shot
        row = random.randint(0,9)
        column = random.randint(0,9)
        if board[row][column] == 0:
            shooting_tuple = (row, column)
            first_cpu_memory = shooting_tuple
            break
    return first_cpu_memory


def cpu_manager1(data, game_mode, current_player, shooting_iq, leaked_board, hidden_board):
    """Handles the actions of the CPU

    Args:
        data (_type_): _description_
        game_mode (int): The chosen game mode to indicate if the CPU player is envolved
        current_player (int): An int value to indicate which player is in turn to take a shot
        shooting_iq (_type_): _description_
        leaked_board (list): The visible board for the player to take a shot
        hidden_board (_type_): The non visible board on which the opponent ships are placed

    Returns:
        bool: Indication that shows that all ships are hit and sunk
    """
    global cpu_memory

    direction = output_manager.user1.get_direction()
    cpu_memory = output_manager.user1.get_cpu_memory()
    while True:
        match shooting_iq:
            case 0:
                # unecessary if already replaced elsewhere
                row, column = cpu_memory
                if leaked_board[row][column] == 6:
                    leaked_board[row][column] = 0
                firstShootingPosition = first_position(hidden_board)
                output_manager.user1.set_first_cpu_memory(firstShootingPosition)

                shooting_iq = 1
                output_manager.user1.set_shooting_iq(shooting_iq)
                continue

            case 1:
                cpu_memory = output_manager.user1.get_first_cpu_memory()
                row, column = cpu_memory
                while True:
                    # check if it is a hit
                    match check_hit(hidden_board, leaked_board, cpu_memory):
                        case 0:  # if the random shot is a non-hit -> still shooting_iq = 0
                            print(
                                colored(
                                    "Der Computer erzielt einen Wassertreffer", "cyan"
                                )
                            )
                            hidden_board[row][column] = 2
                            shooting_iq = 0
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                            next_player(data, game_mode, current_player)
                            break
                        case 1:  # if the random shot is a hit -> get a random direction
                            shooting_iq = 1
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            direction = random_direction()
                            output_manager.user1.set_direction(direction)
                            match direction:
                                case 0:
                                    row = row + 1
                                case 1:
                                    column = column - 1
                                case 2:
                                    column = column + 1
                                case 3:
                                    row = row - 1
                                case _:
                                    print("something went wrong")
                            output_manager.user1.set_direction(direction)
                            python_game.print_hidden_board(hidden_board)
                            cpu_memory = (row, column)
                            output_manager.user1.set_cpu_memory(cpu_memory)
                            while True:
                                match check_hit(hidden_board, leaked_board, cpu_memory):
                                    case 0:  # the first shot in the new direction is a non-hit -> shooting_iq = 2 (go opposite direction)
                                        print(
                                            colored(
                                                "Der Computer erzielt einen Wassertreffer",
                                                "cyan",
                                            )
                                        )
                                        hidden_board[row][column] = 2
                                        shooting_iq = 2
                                        output_manager.user1.set_shooting_iq(shooting_iq)
                                        python_game.print_hidden_board(hidden_board)
                                        next_player(data, game_mode, current_player)
                                        break

                                    case 1:  # the first shot in the new direction is a hit -> shooting_iq = 1 until the first non-hit
                                        shooting_iq = 1
                                        output_manager.user1.set_shooting_iq(shooting_iq)
                                        match direction:
                                            case 0:
                                                row = row + 1
                                            case 1:
                                                column = column - 1
                                            case 2:
                                                column = column + 1
                                            case 3:
                                                row = row - 1
                                            case _:
                                                print("something went wrong")

                                        cpu_memory = (row, column)
                                        output_manager.user1.set_cpu_memory(cpu_memory)
                                        python_game.print_hidden_board(hidden_board)
                                        continue
                                    case 11:  # the cpu killed the last ship
                                        all_hit = 11
                                        return all_hit

                        case _:
                            print("something went wrong")
                    break

            case 2:
                cpu_memory = output_manager.user1.get_first_cpu_memory()
                row, column = cpu_memory
                while True:
                    match direction:
                        case 0:
                            row = row - 1
                        case 1:
                            column = column + 1
                        case 2:
                            column = column - 1
                        case 3:
                            row = row + 1
                        case _:
                            print("something went wrong")
                    cpu_memory = (row, column)
                    output_manager.user1.set_cpu_memory(cpu_memory)

                    match check_hit(hidden_board, leaked_board, cpu_memory):
                        case 0:
                            print(
                                colored(
                                    "Der Computer erzielt einen Wassertreffer", "cyan"
                                )
                            )
                            hidden_board[row][column] = 2
                            shooting_iq = 3
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                            next_player(data, game_mode, current_player)
                            break
                        case 1:
                            shooting_iq = 2
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                        case 11:  # the cpu killed the last ship
                            all_hit = 11
                            return all_hit
                        case _:
                            print("something went wrong")
                    continue

            case 3:
                cpu_memory = output_manager.user1.get_first_cpu_memory()
                row, column = cpu_memory
                while True:
                    match direction:
                        case 0:
                            column = column + 1
                        case 1:
                            row = row + 1
                        case 2:
                            row = row - 1
                        case 3:
                            column = column - 1
                        case _:
                            print("something went wrong")
                    cpu_memory = (row, column)
                    output_manager.user1.set_cpu_memory(cpu_memory)

                    match check_hit(hidden_board, leaked_board, cpu_memory):
                        case 0:
                            print(
                                colored(
                                    "Der Computer erzielt einen Wassertreffer", "cyan"
                                )
                            )
                            hidden_board[row][column] = 2
                            shooting_iq = 4
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                            next_player(data, game_mode, current_player)
                            break
                        case 1:
                            shooting_iq = 3
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                        case 11:  # the cpu killed the last ship
                            all_hit = 11
                            return all_hit
                        case _:
                            print("something went wrong")

                    continue

            case 4:
                cpu_memory = output_manager.user1.get_first_cpu_memory()
                row, column = cpu_memory
                while True:
                    match direction:
                        case 0:
                            column = column - 1
                        case 1:
                            row = row - 1
                        case 2:
                            row = row + 1
                        case 3:
                            column = column + 1
                        case _:
                            print("something went wrong")
                    cpu_memory = (row, column)
                    output_manager.user1.set_cpu_memory(cpu_memory)

                    match check_hit(hidden_board, leaked_board, cpu_memory):
                        case 0:
                            print(
                                colored(
                                    "Der Computer erzielt einen Wassertreffer", "cyan"
                                )
                            )
                            hidden_board[row][column] = 2
                            shooting_iq = 5
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                            next_player(data, game_mode, current_player)
                            break
                        case 1:
                            shooting_iq = 4
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                        case 11:  # the cpu killed the last ship
                            all_hit = 11
                            return all_hit
                        case _:
                            print("something went wrong")

                    continue

            case 5:
                cpu_memory = output_manager.user1.get_first_cpu_memory()
                row, column = cpu_memory
                while True:
                    match direction:
                        case 0:
                            column = column + 1
                        case 1:
                            row = row + 1
                        case 2:
                            row = row - 1
                        case 3:
                            column = column - 1
                        case _:
                            print("something went wrong")
                    cpu_memory = (row, column)
                    output_manager.user1.set_cpu_memory(cpu_memory)

                    match check_hit(hidden_board, leaked_board, cpu_memory):
                        case 0:
                            print(
                                colored(
                                    "Der Computer erzielt einen Wassertreffer", "cyan"
                                )
                            )
                            hidden_board[row][column] = 2
                            shooting_iq = 0
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                            next_player(data, game_mode, current_player)
                            break
                        case 1:
                            shooting_iq = 5
                            output_manager.user1.set_shooting_iq(shooting_iq)
                            python_game.print_hidden_board(hidden_board)
                        case 11:  # the cpu killed the last ship
                            all_hit = 11
                            return all_hit
                        case _:
                            print("something went wrong")

                    continue
            case _:
                print("something went wrong")


# Switches the current player after each action
def next_player(data, game_mode, current_player):
    """Is responsible for changing the current_player value after a player hit water with a shot

    Args:
        data (_type_): _description_
        game_mode (int): The game mode to indicate if CPU player is envolved or two humans
        current_player (int): The int value that indicates the current player
    """
    if current_player == 1:
        current_player = 2
        data["current_player"] = current_player
        print("__________________________________\n")
        print(f"{output_manager.user2.get_name()} ist nun an der Reihe.")
        print("__________________________________\n")
        continue_request = input(
            f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {output_manager.user2.get_name()}  \n"
        )

    elif current_player == 2:
        current_player = 1
        data["current_player"] = current_player
        print("__________________________________\n")
        print(f"{output_manager.user1.get_name()} ist nun an der Reihe.")
        print("__________________________________\n")
        continue_request = input(
            f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {output_manager.user1.get_name()}  \n"
        )
    else:
        print("Irgendwas ist hier schief gelaufen!")

    clear_console()
    shooting(data, game_mode, current_player)
