# Import required modules
import outputmanager
import python_game
import random
import circularImportFixing
import shipmanager

# Function to select the game mode. Prints message if input is not 1 or 2 and calls itself.
def gameModeSelection():
    while True:
        try:
            # Ask user for game mode input
            gameMode = int(input("Bitte wähle die gewünschte Spielart: \n [1] Spiel gegen den Computer \n [2] 2 Spieler\n"))
            # Use match statement to determine the game mode
            match gameMode:
                case 1:
                    # Print game mode message
                    print("__________________________________\n")
                    print("1-Spieler Modus.\n")
                    # Print game rules message
                    print(outputmanager.gameRules)
                    # Set computer as user 1 and ask for user 2 name
                    outputmanager.user1.setName("Der Computer")
                    userName2 = input("Bitte geben Sie ihren Namen an: \n")
                    outputmanager.user2.setName(userName2)
                    # Print welcome message for user 2 and ask to place ships
                    print (f"Hallo {outputmanager.user2.getName()}, bitte platzieren Sie nun Ihre Schiffe")
                    # Call function placeShip to give user the opportunity to select the ship positions
                    placeShip(python_game.leakedBoard1, python_game.shipLength)
                    # Print message for computer to place ships
                    print("Der Computer plaziert nun seine Schiffe. Dies kann einige Sekunden dauern")
                    # Call function cpuPlaceShip to let the computer randomly place ships
                    #cpuPlaceShip(leakedBoard2, shipLength) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    print("")
                    # Print message indicating start of the game
                    print("Das Spiel beginnt.")
                    # Call function to randomly select starting player
                    selectStartingPlayer(gameMode)
                    # Return the game mode
                    return gameMode
                case 2:
                    # Print game mode message
                    print("__________________________________\n")
                    print("2-Spieler Modus.\n")
                    # Print game rules message
                    print(outputmanager.gameRules)
                    # Ask for user 1 name and welcome message
                    userName1 = input("Spieler 1, bitte geben Sie ihren Namen an: \n")
                    # Set user name 1 
                    outputmanager.user1.setName(userName1)
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print (f"Hallo {outputmanager.user1.getName()}, bitte platzieren Sie nun Ihre Schiffe")
                    print ("!!WICHTIG!! Der andere Spieler sollte diesen Vorgang nicht sehen, bitte weggucken!")
                    # Call function placeShip for user 1 to place ships
                    counter = 1
                    for ship in circularImportFixing.playerShips:
                        ship.classPlaceShip(python_game.leakedBoard1, ship, counter)
                        counter = counter+1
                    counter = 1
                    # Ask for user 2 name and welcome message
                    userName2 = input("Spieler 2 bitte geben Sie ihren Namen an: \n")
                    # Set user name 2
                    outputmanager.user2.setName(userName2)
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    print (f"Hallo {outputmanager.user2.getName()}, bitte platzieren Sie nun Ihre Schiffe")
                    print ("!!WICHTIG!! Der andere Spieler sollte diesen Vorgang nicht sehen, bitte weggucken!")
                    # Call function for user 2 to place ships
                    for ship in circularImportFixing.opponentShips:
                        ship.classPlaceShip(python_game.leakedBoard2, ship, counter)
                        counter = counter+1
                    counter = 1
                    # Print message indicating start of the game
                    print("Das Spiel beginnt.")
                    # Call function to randomly select starting player
                    selectStartingPlayer(gameMode)
                    # Return the game mode
                    return gameMode
                case _:
                    # Raise value error if input is not 1 or 2
                    raise ValueError("Ihre Eingabe ist falsch.")
        except ValueError as e:
            # Print error message and ask for correct input
            print(str(e))
            print("Bitte wähle sie entweder [1] für singleplayer oder [2] für multiplayer.")
            continue

# Random selection which player starts the game 
def selectStartingPlayer(mode):
    global currentPlayer
    playerOne = 1
    playerTwo = 2
    print("Es wird zufällig bestimmt wer beginnt...")
    startingPlayer = random.randint(1,2)
    if(startingPlayer == 2):
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} darf das Spiel beginnen und ist an der Reihe!")
        return currentPlayer
    elif(startingPlayer == 1):
        if(mode == "1"):
            print(f"{outputmanager.user1.getName()}ccccccc darf das Spiel beginnen und ist an der Reihe!") #cccc ist als Kontrolltext mit drin um zu zeigen, dass hier der Computer spielt
            currentPlayer = 1
            return currentPlayer
        else:
            print(f"{outputmanager.user1.getName()} darf das Spiel beginnen und ist an der Reihe!")
            currentPlayer = 1
            return currentPlayer
        


                    

