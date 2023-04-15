import outputmanager
from python_game import *
from random import *

# Function to select the game mode. Prints message if input is not 1 or 2 and calls itself.
def gameModeSelection():
    while True:
        try:
            gameMode = int(input("Bitte wähle die gewünschte Spielart: \n [1] Spiel gegen den Computer \n [2] 2 Spieler\n"))
            match gameMode:
                case 1:
                    print("__________________________________\n")
                    print("1-Spieler Modus.\n")
                    print(outputmanager.gameRules)
                    outputmanager.user1.setName("Der Computer")
                    userName2 = input("Bitte geben Sie ihren Namen an: \n")
                    outputmanager.user2.setName(userName2)
                    print (f"Hallo {outputmanager.user2.getName()}, bitte platzieren Sie nun Ihre Schiffe")
                    placeShip(leakedBoard1, shipLength)
                    print("Der Computer plaziert nun seine Schiffe. Dies kann einige Sekunden dauern")
                    #cpuPlaceShip(leakedBoard2, shipLength)
                    print("")
                    print("Das Spiel beginnt.")
                    selectStartingPlayer(gameMode)
                    return gameMode
                case 2:
                    print("__________________________________\n")
                    print("2-Spieler Modus.\n")
                    print(outputmanager.gameRules)
                    userName1 = input("Spieler 1, bitte geben Sie ihren Namen an: \n")
                    outputmanager.user1.setName(userName1)
                    print (f"Hallo {outputmanager.user1.getName()}, bitte platzieren Sie nun Ihre Schiffe")
                    print ("!!WICHTIG!! Der andere Spieler sollte diesen Vorgang nicht sehen, bitte weggucken!")
                    placeShip(leakedBoard1, shipLength)
                    userName2 = input("Spieler 2 bitte geben Sie ihren Namen an: \n")
                    outputmanager.user2.setName(userName2)
                    print (f"Hallo {outputmanager.user2.getName()}, bitte platzieren Sie nun Ihre Schiffe")
                    print ("!!WICHTIG!! Der andere Spieler sollte diesen Vorgang nicht sehen, bitte weggucken!")
                    placeShip(leakedBoard2, shipLength)
                    print("Das Spiel beginnt.")
                    selectStartingPlayer(gameMode)
                    return gameMode
                case _:
                    raise ValueError("Ihre Eingabe ist faclsch.")
        except ValueError as e:
            print(str(e))
            print("Bitte wähle sie entweder [1] für singleplayer oder [2] für multiplayer.")
            continue

# Random selection which player starts the game 
def selectStartingPlayer(mode):
    global currentPlayer
    playerOne = 1
    playerTwo = 2
    print("Es wird zufällig bestimmt wer beginnt...")
    startingPlayer = randint(1,2)
    if(startingPlayer == 2):
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} darf das Spiel beginnen und ist an der Reihe!")
        return currentPlayer
    elif(startingPlayer == 1):
        if(mode == "1"):
            print(f"{outputmanager.user1.getName()}ccccccc darf das Spiel beginnen und ist an der Reihe!") #cccc ist als Kontrolltext mit drin um zu zeigen, dass hier der Computer spielt
            currentPlayer = 2
            return currentPlayer
        else:
            print(f"{outputmanager.user1.getName()} darf das Spiel beginnen und ist an der Reihe!")
            currentPlayer = 2
            return currentPlayer