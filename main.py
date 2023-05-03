"""Main module for game logic"""
import os
import json
import output_manager
import select_operations
import shootingfunction
import python_game
import memory_manager

# extracts current path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# sets current player to 0 to define it afterwards in function below
# currentPlayer = 1
with open("shipstorage.json", "r", encoding="utf-8") as readFile:
    data = json.load(readFile)


# game_mode = 2
def main():
    """Main function that provides the game logic and calls the other modules"""
    # prints a welcome message
    output_manager.welcome_user()
    # asks player if he likes to load a previous game
    load = select_operations.loadrequest(data)
    # if load is true it will reload the old data if load is false it will delete the old data
    if load is True:
        # initializes all boards with their old vaules
        python_game.boardloader(data, load)
        # initializes all ships with ther attributes like damage oder hitted positions
        memory_manager.loadData(data, data["game_mode"])
        # starts game engine to run the main game, returns the number of the winning player at the end
        winning_id = shootingfunction.shooting(
            data, data["game_mode"], data["currentPlayer"]
        )
        # sets storage availibility to 0 to block reloading the finished game
        data["storage_available"] = 0
        # resets all boards to default value (filled with 0) using a default resset board
        python_game.boardReset(data)
        # writes the changed data into json file
        with open("shipstorage.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2)
        # prints winning / losing message using the returned winning_id and the current game_mode
        output_manager.battle_end(winning_id, data["game_mode"])
    elif load is False:
        # initializes new boards with default values
        python_game.boardloader(data, load)
        # gives user the opportunity to choose the game Mode (single player/ multiple players)
        game_mode = select_operations.game_mode_selection(data)
        # calls function to randomly select starting player
        starting_player = select_operations.select_starting_player(data)
        # starts game engine to run the main game, returns the number of the winning player at the end
        winning_id = shootingfunction.shooting(data, game_mode, starting_player)
        # sets storage availibility to 0 to block reloading the finished game
        data["storage_available"] = 0
        # resets all boards to default value (filled with 0) using a default reset board
        python_game.boardReset(data)
        # writes the changed data into json file
        with open("shipstorage.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2)
        # prints winning / losing message using the returned winning_id and the current game_mode
        output_manager.battle_end(winning_id, game_mode)
    else:
        print(
            "Ein Fehler beim erfassen Ihrer Eingabe ist entstanden. Die Daten konnten daher nicht geladen werden."
        )
    # player.playerAction(currentPlayer,game_mode)


if __name__ == "__main__":
    try:
        # tries to run the game
        main()
    # catches error if game is stopt by user
    except KeyboardInterrupt:
        # calls function to store all necessary data to restore the game in future sessions
        memory_manager.storeData(data)
        # writes the changed data into json file
        with open("shipstorage.json", "w", encoding="utf-8") as write_fileEnd:
            json.dump(data, write_fileEnd, indent=2)
        # prints message to confirm the saving process and tells the user how to restore the game
        print(
            "Wir bedanken uns fürs Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim naechsten mal mit [j] laden!\n"
        )
