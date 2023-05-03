"""Module that is responsible for different game logic actions like loading saved data 

Raises:
    ValueError: Prints an error message on the screen
"""
import os
import random
from termcolor import colored
from colorama import init
import output_manager
import python_game
import ship_initializer

global currentPlayer

init()


def clearConsole():
    """Function that clears the console for better user interface
    """
    os.system("cls" if os.name == "nt" else "clear")


def loadrequest(data):
    """Function to check if the player wants to load an existing score or start a new game

    Args:
        data (_type_): _description_

    Raises:
        ValueError: Prints an error message if wrong input is provided

    Returns:
        _type_: Returns True or False, depending on the branch of the function
    """
    while True:
        try:
            # Ask user for game mode input
            loadstorage = input(
                "Wollen Sie einen alten Spielstand laden ja[j] / nein[n]?\n"
            )
            match loadstorage:
                case "j":
                    storageAvailable = data["storage_available"]
                    if storageAvailable == 1:
                        load = True
                        clearConsole()
                        print(
                            "Willkommen zurück, Ihre Daten konnten erfolgreich geladen werden.\nDas Spiel geht an gespeicherter Stelle weiter!"
                        )

                    elif storageAvailable == 0:
                        load = False
                        clearConsole()
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
                    clearConsole()
                    print("Alles klar, das Spiel wird ohne Speicherdaten gestartet!")
                    return load
                case _:
                    # Raise value error if input is not 1 or 2
                    raise ValueError("Ihre Eingabe ist falsch.")
        except ValueError as valueError:
            print(str(valueError))
            print(
                "Bitte wählen Sie entweder [j] für die Moeglichkeit einen Spielstand zu laden oder [n] um das Spiel normal zu starten."
            )
            continue


# Function to select the game mode. Prints message if input is not 1 or 2 and calls itself.
def gameModeSelection(data):
    """Function to choose one or two player mode before starting a game

    Args:
        data (int):

    Raises:
        ValueError: Prints an error message if wrong input is provided by a user

    Returns:
        gameMode(int): An int value that indicates the chosen game mode
    """
    while True:
        try:
            # Ask user for game mode input
            gameMode = int(
                input(
                    "Bitte wählen Sie die gewünschte Spielart: \n [1] Spiel gegen den Computer \n [2] 2 Spieler\n"
                )
            )
            data["gameMode"] = gameMode
            # Use match statement to determine the game mode
            match gameMode:
                case 1:
                    # Print game mode message
                    print("__________________________________\n")
                    print(colored("1-Spieler Modus.\n", "cyan", attrs=["reverse"]))
                    # Print game rules message
                    print(output_manager.GAME_RULES)
                    # Set computer as user 1 and ask for user 2 name
                    output_manager.user1.set_name("Der Computer")
                    userName2 = input("Bitte geben Sie Ihren Namen ein: \n")
                    output_manager.user2.set_name(userName2)
                    # Print welcome message for user 2 and ask to place ships
                    print(
                        f"Hallo {output_manager.user2.get_name()}, bitte platzieren Sie nun Ihre Schiffe"
                    )
                    # Call function placeShip to give user the opportunity to select the ship positions
                    counter = 1
                    for ship in ship_initializer.playerShips:
                        ship.class_place_ship(python_game.leakedBoard2, ship, counter)
                        counter = counter + 1
                    counter = 1
                    # Print message for computer to place ships
                    print(
                        "Der Computer platziert nun seine Schiffe. Dies kann einige Sekunden dauern"
                    )
                    # Call function cpuPlaceShip to let the computer randomly place ships
                    for ship in ship_initializer.opponentShips:
                        ship.class_cpu_place_ship(python_game.leakedBoard1, ship)
                    print("")
                    # Print message indicating start of the game
                    print("Das Spiel beginnt.")
                    # Return the game mode
                    return gameMode
                case 2:
                    # Print game mode message
                    print("__________________________________\n")
                    print(colored("2-Spieler Modus.\n", "cyan", attrs=["reverse"]))
                    # Print game rules message
                    print(output_manager.GAME_RULES)
                    # Ask for user 1 name and welcome message
                    userName1 = input("Spieler 1, bitte geben Sie Ihren Namen ein: \n")
                    # Set user name 1
                    output_manager.user1.set_name(userName1)
                    clearConsole()
                    print(
                        f"Hallo {output_manager.user1.get_name()}, bitte platzieren Sie nun Ihre Schiffe"
                    )
                    print(
                        colored(
                            "\nDer andere Spieler sollte diesen Vorgang nicht sehen, bitte wegschauen!\n",
                            "white","on_red",
                        )
                    )
                    # Call function placeShip for user 1 to place ships
                    counter = 1
                    for ship in ship_initializer.playerShips:
                        ship.class_place_ship(python_game.leakedBoard1, ship, counter)
                        counter = counter + 1
                    counter = 1
                    # Ask for user 2 name and welcome message
                    continueRequest = input(
                        "Enter drücken um Chat zu leeren und Spieler 2 seine Schiffe platzieren zu lassen: \n"
                    )
                    clearConsole()
                    userName2 = input("Spieler 2 bitte geben Sie Ihren Namen an: \n")
                    # Set user name 2
                    output_manager.user2.set_name(userName2)
                    print(
                        f"Hallo {output_manager.user2.get_name()}, bitte platzieren Sie nun Ihre Schiffe"
                    )
                    print(
                        colored(
                            "\nDer andere Spieler sollte diesen Vorgang nicht sehen, bitte wegschauen!\n",
                            "white","on_red",
                        )
                    )
                    # Call function for user 2 to place ships
                    for ship in ship_initializer.opponentShips:
                        ship.class_place_ship(python_game.leakedBoard2, ship, counter)
                        counter = counter + 1
                    counter = 1
                    continueRequest = input(
                        "Enter drücken um Chat zu leeren und das Spiel zu starten: \n"
                    )
                    # Print messaSge indicating start of the game
                    clearConsole()
                    print("Das Spiel beginnt.")
                    # Return the game mode
                    return gameMode
                case _:
                    # Raise value error if input is not 1 or 2
                    raise ValueError("Ihre Eingabe ist falsch.")
        except ValueError as valueError:
            # Print error message and ask for correct input
            print(str(valueError))
            print(
                "Bitte wählen Sie entweder [1] für den Einspieler-Modus oder [2] für den Mehrspieler-Modus."
            )
            continue


def selectStartingPlayer(data):
    """Function to randomly select a player to start the game

    Args:
        data (_type_): _description_

    Returns:
        currentPlayer(int): An int value that indicates the current player
    """

    # playerOne = 1
    # playerTwo = 2
    print("Es wird zufällig bestimmt wer beginnt...")
    startingPlayer = random.randint(1, 2)
    data["currentPlayer"] = startingPlayer
    if startingPlayer == 2:
        print(
            colored(
                f"{output_manager.user2.get_name()} darf das Spiel beginnen und ist an der Reihe!",
                "cyan",
            )
        )
        currentPlayer = 2
        return currentPlayer
    if startingPlayer == 1:
        # if mode == "1":
        # cccc ist als Kontrolltext mit drin um zu zeigen, dass hier der Computer spielt
        # print(f"{outputmanager.user1.get_name()} darf das Spiel beginnen und ist an der Reihe!")
        # currentPlayer = 1
        # return currentPlayer
        print(
            colored(
                f"{output_manager.user1.get_name()} darf das Spiel beginnen und ist an der Reihe!",
                "cyan",
            )
        )
        currentPlayer = 1
        return currentPlayer
