import os
from python_game import *
from random import *

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))
print("Aktueller Pfad: ", path)

# variable that holds the game rules to print when starting the game
gameRules = "Spielregeln:\n 1. Schiffe dürfen nur vertikal oder horizontal platziert werden\n 2. Schiffe dürfen sich nicht berühren \n 3. Schiffe dürfen nicht über den Rand des Spielfelds hinausgehen \n 4. Schiffe dürfen nicht übereinander platziert werden 5. Die Schiffe dürfen nicht über Eck gebaut sein oder Ausbuchtungen besitzen 6. Jeder Spieler hat 10 Schiffe\n"
currentPlayer = 0

# Random selection which player starts the game 
def selectStartingPlayer(mode):
    global currentPlayer
    playerOne = 1
    playerTwo = 2
    startingPlayer = 0
    randint(1,2)
    if(mode == "1"):
        if(randint == "onePlayer"):
            print("Spieler 1 beginnt.")
            startingPlayer = 1
            currentPlayer = 1
        else:
            print("Der Computer beginnt.")
            startingPlayer = 2
            currentPlayer = 2
    elif(mode == "2"):
        if(randint == playerOne):
            print("Spieler 1 beginnt.")
            startingPlayer = 1
            currentPlayer = 1
        else:
            print("Spieler 2 beginnt.")
            startingPlayer = 2
            currentPlayer = 2
    return currentPlayer

# Switches the current player after each action
def nextPlayer():
    global currentPlayer
    if(currentPlayer == 1):
        currentPlayer = 2
    else:
        currentPlayer = 1
    return currentPlayer

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    print("______________________________________________________\n")
    print(" ______ _           _     ____        _   _   _        ")
    print("|  ____| |         | |   |  _ \      | | | | | |       ")
    print("| |__  | | ___  ___| |_  | |_) | __ _| |_| |_| | ___   ")
    print("|  __| | |/ _ \/ _ \ __| |  _ < / _` | __| __| |/ _ \  ")
    print("| |    | |  __/  __/ |_  | |_) | (_| | |_| |_| |  __/  ")
    print("|_|    |_|\___|\___|\__| |____/ \__,_|\__|\__|_|\___|  ")
    print("______________________________________________________\n")
    userInput = input("Bitte wähle die gewünschte Spielart: \n [1] Spiel gegen den Computer \n [2] 2 Spieler\n")
    if(userInput == "1"):
        print("__________________________________\n")
        print("Spiel gegen den Computer.\n")
        print(gameRules)
        placeShip(placementBoard, shipLength)
        cpuPlaceShip(placementBoard, shipLength)
        print("Das Spiel beginnt.")
        selectStartingPlayer(userInput)
    elif(userInput == "2"):
        print("__________________________________\n")
        print("2 Spieler an diesem Computer.\n")
        print(gameRules)
        placeShip(placementBoard, shipLength)
        cpuPlaceShip(placementBoard, shipLength)
        print("Das Spiel beginnt.")
        selectStartingPlayer(userInput)        

if __name__ == "__main__":
    main()

