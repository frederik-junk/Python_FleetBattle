import os
import outputmanager
import selectoperations
import player
import oponent
import circularImportFixing
import shootingfunction

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# setting current Player to 0 to define it afterwards in function below
#currentPlayer = 1
gameMode = 0

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    outputmanager.welcomeUser()
    gameMode = selectoperations.gameModeSelection()
    # Call function to randomly select starting player
    currentPlayer = selectoperations.selectStartingPlayer()
    winningID = shootingfunction.shooting(gameMode, currentPlayer)
    #player.playerAction(currentPlayer,gameMode)
    outputmanager.battleEnd(winningID, gameMode)

if __name__ == "__main__":
    main()




        
