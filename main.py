import os
import outputmanager
import selectoperations
import player
import oponent
import circularImportFixing

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# setting current Player to 0 to define it afterwards in function below
currentPlayer = 1
gameMode = 0

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    outputmanager.welcomeUser()
    gameMode = selectoperations.gameModeSelection()
    player.playerAction(currentPlayer,gameMode)
    outputmanager.battleEnd(2, gameMode)

if __name__ == "__main__":
    main()

# Switches the current player after each action
def nextPlayer():
    global currentPlayer
    global gameMode
    print(currentPlayer)

    if currentPlayer == 1:
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        player.playerAction(currentPlayer, gameMode)
        
    else:
        currentPlayer = 1
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        print(gameMode)
        if gameMode == 1:
            oponent.oponentAction()
        else:
            player.playerAction(currentPlayer, gameMode)

        
