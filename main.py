import os
from python_game import *
from random import *

path = os.path.dirname(os.path.abspath(__file__))
print("Aktueller Pfad: ", path)

gameRules = "Spielregeln:\n 1. Schiffe dürfen nur vertikal oder horizontal platziert werden\n 2. Schiffe dürfen sich nicht berühren \n 3. Schiffe dürfen nicht über den Rand des Spielfelds hinausgehen \n 4. Schiffe dürfen nicht übereinander platziert werden\n"

def selectStartingPlayer(mode):
    playerOne = 1
    playerTwo = 2
    startingPlayer = 0
    randint(1,2)
    if(mode == "1"):
        if(randint == "onePlayer"):
            print("Spieler 1 beginnt.")
            startingPlayer = 1
        else:
            print("Der Computer beginnt.")
            startingPlayer = 2
    elif(mode == "2"):
        if(randint == playerOne):
            print("Spieler 1 beginnt.")
            startingPlayer = 1
        else:
            print("Spieler 2 beginnt.")
            startingPlayer = 2

def main():
    print("__________________________________\n")
    print("Schiffe versenken v1.0")
    print("__________________________________\n")
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
