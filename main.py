"""Main module for game logic
"""
import os
import json
import outputmanager
import selectoperations
import shootingfunction
import pythonGame
import circularImportFixing

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
        outputmanager.user1.setName(data["playerName1"])
        outputmanager.user2.setName(data["playerName2"])
        circularImportFixing.pSchlachtschiff1.setPositionMemory(data["pSchlachtschiff1"])

        circularImportFixing.pKreuzer1.setPositionMemory(data["pKreuzer1"])
        circularImportFixing.pKreuzer2.setPositionMemory(data["pKreuzer2"])
        circularImportFixing.pZerstoerer1.setPositionMemory(data["pKreuzer1"])
        circularImportFixing.pZerstoerer2.setPositionMemory(data["pKreuzer2"])
        circularImportFixing.pZerstoerer3.setPositionMemory(data["pKreuzer3"])
        circularImportFixing.pUboot1.setPositionMemory(data["pUboot1"])
        circularImportFixing.pUboot2.setPositionMemory(data["pUboot2"])
        circularImportFixing.pUboot3.setPositionMemory(data["pUboot3"])
        circularImportFixing.pUboot4.setPositionMemory(data["pUboot4"])

        circularImportFixing.pSchlachtschiff1.setPositionMemory(data["oSchlachtschiff1"])

        circularImportFixing.pKreuzer1.setPositionMemory(data["oKreuzer1"])
        circularImportFixing.pKreuzer2.setPositionMemory(data["oKreuzer2"])
        circularImportFixing.pZerstoerer1.setPositionMemory(data["oKreuzer1"])
        circularImportFixing.pZerstoerer2.setPositionMemory(data["oKreuzer2"])
        circularImportFixing.pZerstoerer3.setPositionMemory(data["oKreuzer3"])
        circularImportFixing.pUboot1.setPositionMemory(data["oUboot1"])
        circularImportFixing.pUboot2.setPositionMemory(data["oUboot2"])
        circularImportFixing.pUboot3.setPositionMemory(data["oUboot3"])
        circularImportFixing.pUboot4.setPositionMemory(data["oUboot4"])

        winningID = shootingfunction.shooting(data, data["gameMode"], data["currentPlayer"])
        data["storage_available"] = 0
        pythonGame.board_reset(data)
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
        pythonGame.board_reset(data)
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
        data["pSchlachtschiff1"] = circularImportFixing.pSchlachtschiff1.getPositionMemory()
        """
        data["pKreuzer1"] = circularImportFixing.pKreuzer1.getPositionMemory()
        data["pKreuzer2"] = circularImportFixing.pKreuzer2.getPositionMemory()
        data["pKreuzer1"] = circularImportFixing.pZerstoerer1.getPositionMemory()
        data["pKreuzer2"] = circularImportFixing.pZerstoerer2.getPositionMemory()
        data["pKreuzer3"] = circularImportFixing.pZerstoerer3.getPositionMemory()
        data["pUboot1"] = circularImportFixing.pUboot1.getPositionMemory()
        data["pUboot2"] = circularImportFixing.pUboot2.getPositionMemory()
        data["pUboot3"] = circularImportFixing.pUboot3.getPositionMemory()
        data["pUboot4"] = circularImportFixing.pUboot4.getPositionMemory()
        """
        data["oSchlachtschiff1"] = circularImportFixing.pSchlachtschiff1.getPositionMemory()
        """
        data["oKreuzer1"] = circularImportFixing.pKreuzer1.getPositionMemory()
        data["oKreuzer2"] = circularImportFixing.pKreuzer2.getPositionMemory()
        data["oKreuzer1"] = circularImportFixing.pZerstoerer1.getPositionMemory()
        data["oKreuzer2"] = circularImportFixing.pZerstoerer2.getPositionMemory()
        data["oKreuzer3"] = circularImportFixing.pZerstoerer3.getPositionMemory()
        data["oUboot1"] = circularImportFixing.pUboot1.getPositionMemory()
        data["oUboot2"] = circularImportFixing.pUboot2.getPositionMemory()
        data["oUboot3"] = circularImportFixing.pUboot3.getPositionMemory()
        data["oUboot4"] = circularImportFixing.pUboot4.getPositionMemory()
        """
        data["playerName1"] = outputmanager.user1.getName()
        data["playerName2"] = outputmanager.user2.getName()
        data["leakedBoard1"] = pythonGame.leakedBoard1
        data["leakedBoard2"] = pythonGame.leakedBoard2
        data["hiddenBoard1"] = pythonGame.hiddenBoard1
        data["hiddenBoard2"] = pythonGame.hiddenBoard2
        data["storage_available"] = 1
        with open("shipstorage.json", "w") as writeFile:
            json.dump(data, writeFile, indent=2)
        print("Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n")
