import os
import json
import outputmanager
import selectoperations
import shootingfunction
import pythonGame
import memorymanager

SHIP_STORAGE_FILE = "shipstorage.json"

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# setting current Player to 0 to define it afterwards in function below
# currentPlayer = 1
with open(SHIP_STORAGE_FILE, "r") as file:
    data = json.load(file)


# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def play_game():
    """Main function that provides the game logic and calls the other modules"""
    outputmanager.welcomeUser()
    should_load_game = selectoperations.loadrequest(data)
    if should_load_game:
        pythonGame.boardloader(data, should_load_game)
        memorymanager.loadData(data, data["game_mode"])
        winning_player_id = shootingfunction.shooting(
            data, data["game_mode"], data["current_player"]
        )
        data["storage_available"] = 0
        pythonGame.boardReset(data)
        with open(SHIP_STORAGE_FILE, "w") as file:
            json.dump(data, file, indent=2)
        outputmanager.battleEnd(winning_player_id, data["game_mode"])
    else:
        pythonGame.boardloader(data, should_load_game)
        selected_game_mode = selectoperations.gameModeSelection(data)
        # Call function to randomly select starting player
        starting_player = selectoperations.selectStartingPlayer(data)
        winning_player_id = shootingfunction.shooting(
            data, selected_game_mode, starting_player

        )
        data["storage_available"] = 0
        pythonGame.boardReset(data)
        with open(SHIP_STORAGE_FILE, "w") as file:
            json.dump(data, file, indent=2)
        outputmanager.battleEnd(winning_player_id, selected_game_mode)

    # player.playerAction(currentPlayer, selected_game_mode)


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        memorymanager.storeData(data)
        with open(SHIP_STORAGE_FILE, "w") as file:
            json.dump(data, file, indent=2)
        print(
            "Wir bedanken uns fürs Spielen bis zum nächsten Mal!\nDein Spiel wurde gespeichert und lässt sich beim nächsten Mal mit [j] laden!\n")