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
    load = selectoperations.loadrequest(data)
    if load == True:
        python_game.boardloader(data, load)
        outputmanager.user1.setName(data["playerName1"])
        outputmanager.user2.setName(data["playerName2"])
        winningID = shootingfunction.shooting(data, data["gameMode"], data["currentPlayer"])
        data["storage_available"] = 0
        python_game.board_reset(data)
        with open("shipstorage.json", "w") as write_file:
            json.dump(data, write_file, indent=2)
        outputmanager.battleEnd(winningID, data["gameMode"])
    elif load == False:
        python_game.boardloader(data, load)
        gameMode = selectoperations.gameModeSelection(data)
        # Call function to randomly select starting player
        startingPlayer = selectoperations.selectStartingPlayer(data) 
        winningID = shootingfunction.shooting(data, gameMode, startingPlayer)
        data["storage_available"] = 0
        python_game.board_reset(data)
        with open("shipstorage.json", "w") as write_file:
            json.dump(data, write_file, indent=2)
        outputmanager.battleEnd(winningID, gameMode)
    else:
        print("Ein Fehler")
    #player.playerAction(currentPlayer,gameMode)
 

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        data["playerName1"] = outputmanager.user1.getName()
        data["playerName2"] = outputmanager.user2.getName()
        data["leakedBoard1"] = python_game.leakedBoard1
        data["leakedBoard2"] = python_game.leakedBoard2
        data["hiddenBoard1"] = python_game.hiddenBoard1
        data["hiddenBoard2"] = python_game.hiddenBoard2
        data["storage_available"] = 1
        with open("shipstorage.json", "w") as write_file:
            json.dump(data, write_file, indent=2)
        print("Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n")





        
