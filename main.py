import os
import outputmanager
import selectoperations
import shootingfunction
import json
import python_game

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# setting current Player to 0 to define it afterwards in function below
#currentPlayer = 1
gameMode = 0
with open("shipstorage.json", "r") as read_file:
    data = json.load(read_file)

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    outputmanager.welcomeUser()
    load = selectoperations.loadrequest()

    if load == True:
        python_game.boardloader()
        winningID = shootingfunction.shooting(data["gameMode"], data["currentPlayer"])
        outputmanager.battleEnd(winningID, data["gameMode"])
    elif load == False:
        gameMode = selectoperations.gameModeSelection()
        # Call function to randomly select starting player
        startingPlayer = selectoperations.selectStartingPlayer()
        data["storage_available"] = 1 
        winningID = shootingfunction.shooting(gameMode, startingPlayer, load)
        outputmanager.battleEnd(winningID, gameMode)
    else:
        print("Ein Fehler")
    #player.playerAction(currentPlayer,gameMode)
 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        data["leakedBoard1"] = python_game.leakedBoard1
        data["leakedBoard2"] = python_game.leakedBoard2
        data["hiddenBoard1"] = python_game.hiddenBoard1
        data["hiddenBoard2"] = python_game.hiddenBoard2
        with open("shipstorage.json", "w") as write_file:
            json.dump(data, write_file, indent=2)
        print("Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n")





        
