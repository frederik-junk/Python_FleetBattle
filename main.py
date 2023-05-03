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
with open("shipstorage.json", "r", encoding = "utf-8") as readFile:
    data = json.load(readFile)
#gameMode = 2
def main():
    """Main function that provides the game logic and calls the other modules
    """
    #printing a welcome message
    outputmanager.welcomeUser()
    #asking player if he likes to load a previous game
    load = selectoperations.loadrequest(data)
    #if load is true it will reload the old data if load is false it will delete the old data
    if load is True:
        #initialize all boards with their old vaules
        pythonGame.boardloader(data, load)
        #initialize all ships with ther attributes like damage oder hitted positions
        memorymanager.loadData(data, data["gameMode"])
        #starting game engine to run the main game, returns the number of the winning player at the end
        winningID = shootingfunction.shooting(data, data["gameMode"], data["currentPlayer"])
        #setting storage availibility to 0 to block reloading the finished game
        data["storage_available"] = 0
        #reset all boards to default value (filled with 0) using a default resset board
        pythonGame.boardReset(data)
        #wirte the changed data into json file
        with open("shipstorage.json", "w", encoding = "utf-8") as writeFile:
            json.dump(data, writeFile, indent=2)
        #print winning / losing message using the returned winningID and the current gamemode
        outputmanager.battleEnd(winningID, data["gameMode"])
    elif load is False:
        #initialize new boards with default values
        pythonGame.boardloader(data, load)
        #giving the user the opportunity to choose the game Mode (single player/ multiple players)
        gameMode = selectoperations.gameModeSelection(data)
        #Call function to randomly select starting player
        startingPlayer = selectoperations.selectStartingPlayer(data)
        #starting game engine to run the main game, returns the number of the winning player at the end
        winningID = shootingfunction.shooting(data, gameMode, startingPlayer)
        #setting storage availibility to 0 to block reloading the finished game
        data["storage_available"] = 0
        #reset all boards to default value (filled with 0) using a default resset board
        pythonGame.boardReset(data)
        #wirte the changed data into json file
        with open("shipstorage.json", "w", encoding = "utf-8") as writeFile:
            json.dump(data, writeFile, indent=2)
        #print winning / losing message using the returned winningID and the current gamemode
        outputmanager.battleEnd(winningID, gameMode)
    else:
        print("Ein Fehler beim erfassen Ihrer Eingabe ist entstanden. Die Daten konnten daher nicht geladen werden.")
    #player.playerAction(currentPlayer,gameMode)

if __name__ == "__main__":
    try:
        #try to run the game
        main()
    #catching error if game is stopt by user
    except KeyboardInterrupt:
        #calling function to store all necessary data to restore the game in future sessions
        memorymanager.storeData(data)
        #write the changed data into json file
        with open("shipstorage.json", "w", encoding = "utf-8") as writeFileEnd:
            json.dump(data, writeFileEnd, indent=2)
        #printing message to confirm the saving process and tell the user how to restore the game
        print("Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n")
