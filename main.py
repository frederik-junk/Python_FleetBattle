#pylint disable=C
import os
import json
import output_manager
import select_operations
import shooting_function
import python_game
import memory_manager

SHIP_STORAGE_FILE = "ship_storage.json"

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))

# sets current player to 0 to define it afterwards in function below
# current_player = 1
with open("ship_storage.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)
# setting current Player to 0 to define it afterwards in function below
# currentPlayer = 1
with open(SHIP_STORAGE_FILE, "r") as file:
    data = json.load(file)


# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def play_game():
    """Main function that provides the game logic and calls the other modules"""
    output_manager.welcomeUser()
    should_load_game = select_operations.load_request(data)
    if should_load_game:
        python_game.board_loader(data, should_load_game)
        memory_manager.load_data(data, data["game_mode"])
        winning_player_id = shooting_function.shooting(
            data, data["game_mode"], data["current_player"]
        )
        data["storage_available"] = 0
        # resets all boards to default value (filled with 0) using a default resset board
        python_game.board_reset(data)
        # writes the changed data into json file
        with open("ship_storage.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2)
        # prints winning / losing message using the returned winning_id and the current game_mode
        output_manager.battle_end(winning_id, data["game_mode"])
    elif load is False:
        # initializes new boards with default values
        python_game.board_loader(data, load)
        # gives user the opportunity to choose the game Mode (single player/ multiple players)
        game_mode = select_operations.game_mode_selection(data)
        # calls function to randomly select starting player
        starting_player = select_operations.select_starting_player(data)
        # starts game engine to run the main game, returns the number of the winning player at the end
        winning_id = shooting_function.shooting(data, game_mode, starting_player)
        # sets storage availibility to 0 to block reloading the finished game
        data["storage_available"] = 0
        # resets all boards to default value (filled with 0) using a default reset board
        python_game.board_reset(data)
        # writes the changed data into json file
        with open("ship_storage.json", "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=2)
        # prints winning / losing message using the returned winning_id and the current game_mode
        output_manager.battle_end(winning_id, game_mode)
    else:
        python_game.board_loader(data, should_load_game)
        selected_game_mode = select_operations.game_mode_selection(data)
        # Call function to randomly select starting player
        starting_player = select_operations.select_starting_player(data)
        winning_player_id = shooting_function.shooting(
            data, selected_game_mode, starting_player

        )
        data["storage_available"] = 0
        python_game.board_reset(data)
        with open(SHIP_STORAGE_FILE, "w") as file:
            json.dump(data, file, indent=2)
        output_manager.battle_end(winning_player_id, selected_game_mode)

    # player.playerAction(currentPlayer, selected_game_mode)


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        memory_manager.storeData(data)
        with open(SHIP_STORAGE_FILE, "w") as file:
            json.dump(data, file, indent=2)
        print(
            "Wir bedanken uns fürs Spielen bis zum nächsten Mal!\nDein Spiel wurde gespeichert und lässt sich beim nächsten Mal mit [j] laden!\n")