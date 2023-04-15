import os
from python_game import *
from random import *

class User:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

user1 = User("Spieler 1")
user2 = User("Spieler 2")

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))
print("Aktueller Pfad: ", path)

def welcomeUser():
    print("______________________________________________________\n")
    print(" ______ _           _     ____        _   _   _        ")
    print("|  ____| |         | |   |  _ \      | | | | | |       ")
    print("| |__  | | ___  ___| |_  | |_) | __ _| |_| |_| | ___   ")
    print("|  __| | |/ _ \/ _ \ __| |  _ < / _` | __| __| |/ _ \  ")
    print("| |    | |  __/  __/ |_  | |_) | (_| | |_| |_| |  __/  ")
    print("|_|    |_|\___|\___|\__| |____/ \__,_|\__|\__|_|\___|  ")
    print("______________________________________________________\n")

# variable that holds the game rules to print when starting the game
gameRules = "Spielregeln:\n 1. Schiffe dürfen nur vertikal oder horizontal platziert werden\n 2. Schiffe dürfen sich nicht berühren \n 3. Schiffe dürfen nicht über den Rand des Spielfelds hinausgehen \n 4. Schiffe dürfen nicht übereinander platziert werden\n 5. Die Schiffe dürfen nicht über Eck gebaut sein oder Ausbuchtungen besitzen\n 6. Jeder Spieler hat 10 Schiffe\n"
# setting current Player to 0 to define it afterwards in function below
currentPlayer = 0

# Function to select the game mode. Prints message if input is not 1 or 2 and calls itself.
def gameModeSelection():
    userInput = input("Bitte wähle die gewünschte Spielart: \n [1] Spiel gegen den Computer \n [2] 2 Spieler\n")
    match userInput:
        case "1":
            print("__________________________________\n")
            print("1-Spieler Modus.\n")
            print(gameRules)
            userName1 = input("Bitte geben Sie ihren Namen an: \n")
            user1.setName(userName1)
            print (f"Hallo {user1.getName()}, bitte platzieren Sie nun Ihre Schiffe")
            placeShip(leakedBoard1, shipLength)
            print("Der Computer plaziert nun seine Schiffe. Dies kann einige Sekunden dauern")
            cpuPlaceShip(leakedBoard2, shipLength)
            print("")
            print("Das Spiel beginnt.")
            user2.setName("Computer")
            selectStartingPlayer(userInput, userName1)
        case "2":
            print("__________________________________\n")
            print("2-Spieler Modus.\n")
            print(gameRules)
            userName1 = input("Spieler 1, bitte geben Sie ihren Namen an: \n")
            user1.setName(userName1)
            print (f"Hallo {user1.getName()}, bitte platzieren Sie nun Ihre Schiffe")
            print ("!!WICHTIG!! Der andere Spieler sollte diesen Vorgang nicht sehen, bitte weggucken!")
            placeShip(leakedBoard1, shipLength)
            userName2 = input("Spieler 2 bitte geben Sie ihren Namen an: \n")
            user2.setName(userName2)
            print (f"Hallo {user2.getName()}, bitte platzieren Sie nun Ihre Schiffe")
            print ("!!WICHTIG!! Der andere Spieler sollte diesen Vorgang nicht sehen, bitte weggucken!")
            placeShip(leakedBoard2, shipLength)
            print("Das Spiel beginnt.")
            selectStartingPlayer(userInput)
        case _: 
            print("Ungültige Eingabe.\n")
            gameModeSelection()

# Random selection which player starts the game 
def selectStartingPlayer(mode):
    global currentPlayer
    playerOne = 1
    playerTwo = 2
    print("Es wird zufällig bestimmt wer beginnt...")
    startingPlayer = randint(1,2)
    if(startingPlayer == 1):
        currentPlayer = 1
        print(f"{user1.getName()} darf das Spiel beginnen und ist an der Reihe")
        return currentPlayer
    elif(startingPlayer == 2):
        if(mode == "1"):
            print(f"{user2.getName()}ccccccc darf das Spiel beginnen und ist an der Reihe") #cccc ist als Kontrolltext mit drin um zu zeigen, dass hier der Computer spielt
            currentPlayer = 2
            return currentPlayer
        else:
            print(f"{user2.getName()} darf das Spiel beginnen und ist an der Reihe")
            currentPlayer = 2
            return currentPlayer


# Switches the current player after each action
def nextPlayer():
    global currentPlayer
    if(currentPlayer == 1):
        currentPlayer = 2
        print(f"{user2.getName()} ist nun an der Reihe.")
    else:
        currentPlayer = 1
        print(f"{user1.getName()} ist nun an der Reihe.")
    return currentPlayer

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    welcomeUser()
    gameModeSelection()

if __name__ == "__main__":
    main()
