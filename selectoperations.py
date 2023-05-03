import os
import random
from termcolor import colored
from colorama import init
import outputmanager
import pythonGame
import shipinitializer

global current_player

init()


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def load_request(data):
    """Function to check if the player wants to load an existing score or start a new game

    Args:
        data (_type_): _description_

    Raises:
        value_error: Prints an error message if wrong input is provided

    Returns:
        _type_: Returns True or False, depending on the branch of the function
    """
    while True:
        try:
            # Ask user for game mode input
            load_storage = input(
                "Wollen Sie einen alten Spielstand laden ja[j] / nein[n]?\n"
            )
            match load_storage:
                case "j":
                    storage_available = data["storage_available"]
                    if storage_available == 1:
                        load = True
                        clear_console()
                        print(
                            "Willkommen zurück, Ihre Daten konnten erfolgreich geladen werden.\nDas Spiel geht an gespeicherter Stelle weiter!"
                        )

                    elif storage_available == 0:
                        load = False
                        clear_console()
                        print(
                            "Leider ist kein Spielstand vorhanden!\nDas Spiel startet daher ohne Spielstand!"
                        )

                    else:
                        print(
                            "Ein Speicherfehler ist aufgetreten. Wir versuchen dieses Problem zu beheben bitte starte das Spiel erneut und gebe [n] an!"
                        )
                        load = False
                    return load

                case "n":
                    load = False
                    clear_console()
                    print("Alles klar, das Spiel wird ohne Speicherdaten gestartet!")
                    return load
                case _:
                    # Raise value error if input is not 1 or 2
                    raise value_error("Ihre Eingabe ist falsch.")
        except value_error as value_error:
            print(str(value_error))
            print(
                "Bitte wählen Sie entweder [j] für die Moeglichkeit einen Spielstand zu laden oder [n] um das Spiel normal zu starten."
            )
            continue


# Function to select the game mode. Prints message if input is not 1 or 2 and calls itself.
def game_mode_selection(data):
    """Function to choose one or two player mode before starting a game

    Args:
        data (int):

    Raises:
        value_error: Prints an error message if wrong input is provided by a user

    Returns:
        game_mode(int): An int value that indicates the chosen game mode
    """
    while True:
        try:
            # Ask user for game mode input
            game_mode = int(
                input(
                    "Bitte wählen Sie die gewünschte Spielart: \n [1] Spiel gegen den Computer \n [2] 2 Spieler\n"
                )
            )
            data["game_mode"] = game_mode
            # Use match statement to determine the game mode
            match game_mode:
                case 1:
                    # Print game mode message
                    print("__________________________________\n")
                    print(colored("1-Spieler Modus.\n", "cyan", attrs=["reverse"]))
                    # Print game rules message
                    print(outputmanager.GAME_RULES)
                    # Set computer as user 1 and ask for user 2 name
                    outputmanager.user1.set_name("Der Computer")
                    user_name_2 = input("Bitte geben Sie Ihren Namen ein: \n")
                    outputmanager.user2.set_name(user_name_2)
                    # Print welcome message for user 2 and ask to place ships
                    print(
                        f"Hallo {outputmanager.user2.get_name()}, bitte platzieren Sie nun Ihre Schiffe"
                    )
                    # Call function placeShip to give user the opportunity to select the ship positions
                    counter = 1
                    for ship in shipinitializer.playerShips:
                        ship.classPlaceShip(pythonGame.leakedBoard2, ship, counter)
                        counter = counter + 1
                    counter = 1
                    # Print message for computer to place ships
                    print(
                        "Der Computer platziert nun seine Schiffe. Dies kann einige Sekunden dauern"
                    )
                    # Call function cpuPlaceShip to let the computer randomly place ships
                    for ship in shipinitializer.opponentShips:
                        ship.classCpuPlaceShip(pythonGame.leakedBoard1, ship)
                    print("")
                    # Print message indicating start of the game
                    print("Das Spiel beginnt.")
                    # Return the game mode
                    return game_mode
                case 2:
                    # Print game mode message
                    print("__________________________________\n")
                    print(colored("2-Spieler Modus.\n", "cyan", attrs=["reverse"]))
                    # Print game rules message
                    print(outputmanager.GAME_RULES)
                    # Ask for user 1 name and welcome message
                    user_name_1 = input("Spieler 1, bitte geben Sie Ihren Namen ein: \n")
                    # Set user name 1
                    outputmanager.user1.set_name(user_name_1)
                    clear_console()
                    print(
                        f"Hallo {outputmanager.user1.get_name()}, bitte platzieren Sie nun Ihre Schiffe"
                    )
                    print(
                        colored(
                            "\nDer andere Spieler sollte diesen Vorgang nicht sehen, bitte wegschauen!\n",
                            "red",
                            attrs=["reverse"],
                        )
                    )
                    # Call function placeShip for user 1 to place ships
                    counter = 1
                    for ship in shipinitializer.playerShips:
                        ship.classPlaceShip(pythonGame.leakedBoard1, ship, counter)
                        counter = counter + 1
                    counter = 1
                    # Ask for user 2 name and welcome message
                    continue_request = input(
                        "Enter drücken um Chat zu leeren und Spieler 2 seine Schiffe platzieren zu lassen: \n"
                    )
                    clear_console()
                    user_name_2 = input("Spieler 2 bitte geben Sie Ihren Namen an: \n")
                    # Set user name 2
                    outputmanager.user2.set_name(user_name_2)
                    print(
                        f"Hallo {outputmanager.user2.get_name()}, bitte platzieren Sie nun Ihre Schiffe"
                    )
                    print(
                        colored(
                            "\nDer andere Spieler sollte diesen Vorgang nicht sehen, bitte wegschauen!\n",
                            "red",
                            attrs=["reverse"],
                        )
                    )
                    # Call function for user 2 to place ships
                    for ship in shipinitializer.opponentShips:
                        ship.classPlaceShip(pythonGame.leakedBoard2, ship, counter)
                        counter = counter + 1
                    counter = 1
                    continue_request = input(
                        "Enter drücken um Chat zu leeren und das Spiel zu starten: \n"
                    )
                    # Print messaSge indicating start of the game
                    clear_console()
                    print("Das Spiel beginnt.")
                    # Return the game mode
                    return game_mode
                case _:
                    # Raise value error if input is not 1 or 2
                    raise value_error("Ihre Eingabe ist falsch.")
        except value_error as value_error:
            # Print error message and ask for correct input
            print(str(value_error))
            print(
                "Bitte wählen Sie entweder [1] für den Einspieler-Modus oder [2] für den Mehrspieler-Modus."
            )
            continue


def select_starting_player(data):
    """Function to randomly select a player to start the game

    Args:
        data (_type_): _description_

    Returns:
        current_player(int): An int value that indicates the current player
    """

    # playerOne = 1
    # playerTwo = 2
    print("Es wird zufällig bestimmt wer beginnt...")
    starting_player = random.randint(1, 2)
    data["current_player"] = starting_player
    if starting_player == 2:
        print(
            colored(
                f"{outputmanager.user2.get_name()} darf das Spiel beginnen und ist an der Reihe!",
                "cyan",
            )
        )
        current_player = 2
        return current_player
    if starting_player == 1:
        # if mode == "1":
        # cccc ist als Kontrolltext mit drin um zu zeigen, dass hier der Computer spielt
        # print(f"{outputmanager.user1.get_name()} darf das Spiel beginnen und ist an der Reihe!")
        # current_player = 1
        # return current_player
        print(
            colored(
                f"{outputmanager.user1.get_name()} darf das Spiel beginnen und ist an der Reihe!",
                "cyan",
            )
        )
        current_player = 1
        return current_player
