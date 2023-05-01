import os
import outputmanager
import selectoperations
import shootingfunction
import json

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# setting current Player to 0 to define it afterwards in function below
#currentPlayer = 1
gameMode = 0

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    data = 0
    outputmanager.welcomeUser()
    load = selectoperations.loadrequest()
    with open("shipstorage.json", "r") as read_file:
        data = json.load(read_file)
    if load == True:
        winningID = shootingfunction.shooting(data["gameMode"], data["currentPlayer"], data)
    elif load == False:
        gameMode = selectoperations.gameModeSelection()
        # Call function to randomly select starting player
        startingPlayer = selectoperations.selectStartingPlayer() 
        winningID = shootingfunction.shooting(gameMode, startingPlayer, data)
    else:
        print("Ein Fehler")
    #player.playerAction(currentPlayer,gameMode)
    outputmanager.battleEnd(winningID, gameMode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n")





        
