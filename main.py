"""Main module for game logic
"""
import os
import json
import outputmanager
import selectoperations
import shootingfunction
import pythonGame
import memorymanager

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# setting current Player to 0 to define it afterwards in function below
#currentPlayer = 1
gameMode = 0
with open("shipstorage.json", "r") as readFile:
    data = json.load(readFile)

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    """Main function that provides the game logic and calls the other modules
    """
    outputmanager.welcomeUser()
    load = selectoperations.loadrequest(data)
    if load is True:
        pythonGame.boardloader(data, load)
        memorymanager.loadData(data, data["gameMode"])
        winningID = shootingfunction.shooting(data, data["gameMode"], data["currentPlayer"])
        data["storage_available"] = 0
        pythonGame.boardReset(data)
        with open("shipstorage.json", "w") as writeFile:
            json.dump(data, writeFile, indent=2)
        outputmanager.battleEnd(winningID, data["gameMode"])
    elif load is False:
        pythonGame.boardloader(data, load)
        gameMode = selectoperations.gameModeSelection(data)
        # Call function to randomly select starting player
        startingPlayer = selectoperations.selectStartingPlayer(data)
        winningID = shootingfunction.shooting(data, gameMode, startingPlayer)
        data["storage_available"] = 0
        pythonGame.boardReset(data)
        with open("shipstorage.json", "w") as writeFile:
            json.dump(data, writeFile, indent=2)
        outputmanager.battleEnd(winningID, gameMode)
    else:
        print("Ein Fehler")
    #player.playerAction(currentPlayer,gameMode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        memorymanager.storeData(data)
        with open("shipstorage.json", "w") as writeFile:
            json.dump(data, writeFile, indent=2)
        print("Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n")
