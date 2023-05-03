"""main.py starts game, provides game logic, calls other modules"""
import os
import json
import output_manager
import select_operations
import shooting_function
import python_game
import memory_manager
SHIP_STORAGE_FILE = "ship_storage.json"


# extracts current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# sets current player to 0 to define it afterwards in function below
# current_player = 1
with open(SHIP_STORAGE_FILE, "r", encoding="utf-8") as read_file:
    data = json.load(read_file)
# sets current Player to 0 to define it afterwards in function below
# currentPlayer = 1

# Holds the logic of the game, welcomes user, asks for game mode selection and navigates through the game
def main():
    """Main function that provides game logic and calls other modules"""
    output_manager.welcome_user()
    should_load_game = select_operations.load_request(data)
    if should_load_game is True:
        python_game.board_loader(data, should_load_game)
        memory_manager.load_data(data, data["game_mode"])
        current_player = data["current_player"]
        game_mode = data["game_mode"]

        while True:
            winning_player_id = shooting_function.shooting(game_mode , current_player)
            if winning_player_id is None:
                current_player = shooting_function.next_player(data, current_player)
                continue
            break

        data["storage_available"] = 0
        # resets all boards to default value (filled with 0) using a default reset board
        python_game.board_reset(data)
        # writes the changed data into json file
        with open("ship_storage.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2)
        # prints winning/losing message using returned winning_id and current game_mode
        output_manager.battle_end(winning_player_id, data["game_mode"])
    elif should_load_game is False:
        # initializes new boards with default values
        python_game.board_loader(data, should_load_game)
        # gives the user the opportunity to choose the game mode (single player/ multiple players)
        game_mode = select_operations.game_mode_selection(data)
        # calls function to randomly select starting player
        current_player = select_operations.select_starting_player(data)
        # starts game engine to run the main game, returns number of the winning player at the end

        while True:
            winning_player_id = shooting_function.shooting(game_mode, current_player)
            if winning_player_id is None:
                current_player = shooting_function.next_player(data, current_player)
                continue
            break

        # sets storage availability to 0 to block reloading the finished game
        data["storage_available"] = 0
        # resets all boards to default value (filled with 0) using a default reset board
        python_game.board_reset(data)
        # writes the changed data into json file
        with open("ship_storage.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2)
        # prints winning/losing message using the returned winning_id and the current game_mode
        output_manager.battle_end(winning_player_id, game_mode)
    else:
        print("Bei der Abfrage der gespeicherten Daten ist ein Fehler aufgetreten")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        memory_manager.store_data(data)
        with open(SHIP_STORAGE_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        print(
            "Wir bedanken uns fuers Spielen bis zum naechsten Mal!\nDein Spiel wurde gespeichert und laesst sich beim nächsten Mal mit [j] laden!\n")
