"""Module that is responsible for correct loading of the data
"""
import ship_initializer
import output_manager
import python_game


def load_data(data, game_mode):
    """Function that sets each value that is read from the saved file to the right variable in the game.
    """
    #checking if cpu data is necessary (gamemode 1)
    if game_mode == 1:
        # coordinates of tupel with succesful hit
        first_cpu_memory = tuple(data["first_cpu_memory"])
        output_manager.user_1.set_first_cpu_memory(first_cpu_memory)
        # cpu status (diffrent steps until final ship finish)
        output_manager.user_1.set_shooting_iq(data["shooting_iq"])
        # direction for next hits after succesful first hit
        output_manager.user_1.set_direction(data["direction"])
    # loads name of Player 1
    output_manager.user_1.set_name(data["player_name_1"])
    # loads name of Player 2
    output_manager.user_2.set_name(data["player_name_2"])
    # loads amount of sunken ships (player 1)
    output_manager.user_1.set_left_ships(data["player_ships"])
    # loads amount of sunken ships (player 2)
    output_manager.user_1.set_left_ships(data["opponent_ships"])

    # initalize all player 1 (player) ships with memory data of postion and hitted spots
    # variable explanation: p-(code letter for player 1)- Schlachtschiff1 -(unique ship name)- p/m -
    # (p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)

    p_schlachtschiff_p_list = [tuple(item) for item in data["p_schlachtschiff_1_p"]]
    p_schlachtschiff_m_list = [tuple(item) for item in data["p_schlachtschiff_1_m"]]
    ship_initializer.p_schlachtschiff_1.set_position_memory(p_schlachtschiff_m_list)
    ship_initializer.p_schlachtschiff_1.set_position(p_schlachtschiff_p_list)

    p_kreuzer_1_p_list = [tuple(item) for item in data["p_kreuzer_1_p"]]
    p_kreuzer_1_m_list = [tuple(item) for item in data["p_kreuzer_1_m"]] 
    ship_initializer.p_kreuzer_1.set_position_memory(p_kreuzer_1_m_list)
    ship_initializer.p_kreuzer_1.set_position(p_kreuzer_1_p_list)

    p_kreuzer_2_p_list = [tuple(item) for item in data["p_kreuzer_2_p"]]
    p_kreuzer_2_m_list = [tuple(item) for item in data["p_kreuzer_2_m"]] 
    ship_initializer.p_kreuzer_2.set_position_memory(p_kreuzer_2_m_list)
    ship_initializer.p_kreuzer_2.set_position(p_kreuzer_2_p_list)

    p_zerstoerer_1_p_list = [tuple(item) for item in data["p_zerstoerer_1_p"]]
    p_zerstoerer_1_m_list = [tuple(item) for item in data["p_zerstoerer_1_m"]] 
    ship_initializer.p_zerstoerer_1.set_position_memory(p_zerstoerer_1_m_list)
    ship_initializer.p_zerstoerer_1.set_position(p_zerstoerer_1_p_list)

    p_zerstoerer_2_p_list = [tuple(item) for item in data["p_zerstoerer_2_p"]]
    p_zerstoerer_2_m_list = [tuple(item) for item in data["p_zerstoerer_2_m"]] 
    ship_initializer.p_zerstoerer_2.set_position_memory(p_zerstoerer_2_m_list)
    ship_initializer.p_zerstoerer_2.set_position(p_zerstoerer_2_p_list)

    p_zerstoerer_3_p_list = [tuple(item) for item in data["p_zerstoerer_3_p"]]
    p_zerstoerer_3_m_list = [tuple(item) for item in data["p_zerstoerer_3_m"]] 
    ship_initializer.p_zerstoerer_3.set_position_memory(p_zerstoerer_3_m_list)
    ship_initializer.p_zerstoerer_3.set_position(p_zerstoerer_3_p_list)

    p_uboot_1p_list = [tuple(item) for item in data["p_uboot_1p"]]
    p_uboot_1m_list = [tuple(item) for item in data["p_uboot_1m"]] 
    ship_initializer.p_uboot_1.set_position_memory(p_uboot_1m_list)
    ship_initializer.p_uboot_1.set_position(p_uboot_1p_list)

    p_uboot_2_p_list = [tuple(item) for item in data["p_uboot_2_p"]]
    p_uboot_2_m_list = [tuple(item) for item in data["p_uboot_2_m"]] 
    ship_initializer.p_uboot_2.set_position_memory(p_uboot_2_m_list)
    ship_initializer.p_uboot_2.set_position(p_uboot_2_p_list)

    p_uboot_3_p_list = [tuple(item) for item in data["p_uboot_3_p"]]
    p_uboot_3_m_list = [tuple(item) for item in data["p_uboot_3_m"]] 
    ship_initializer.p_uboot_3.set_position_memory(p_uboot_3_m_list)
    ship_initializer.p_uboot_3.set_position(p_uboot_3_p_list)

    p_uboot_4_p_list = [tuple(item) for item in data["p_uboot_4_p"]]
    p_uboot_4_m_list = [tuple(item) for item in data["p_uboot_4_m"]] 
    ship_initializer.p_uboot_4.set_position_memory(p_uboot_4_m_list)
    ship_initializer.p_uboot_4.set_position(p_uboot_4_p_list)



    # initalize all player 2 (opponent) ships with memory data of postion and hitted spots
    # variable explanation: o-(code letter for player 2)- Schlachtschiff1 -(unique ship name)- p/m -
    # (p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)

    o_schlachtschiff_1_p_list = [tuple(item) for item in data["o_schlachtschiff_1_p"]]
    o_schlachtschiff_1_m_list = [tuple(item) for item in data["o_schlachtschiff_1_m"]]
    ship_initializer.o_schlachtschiff_1.set_position_memory(o_schlachtschiff_1_m_list)
    ship_initializer.o_schlachtschiff_1.set_position(o_schlachtschiff_1_p_list)

    o_kreuzer_1_p_list = [tuple(item) for item in data["o_kreuzer_1_p"]]
    o_kreuzer_1_m_list = [tuple(item) for item in data["o_kreuzer_1_m"]] 
    ship_initializer.o_kreuzer_1.set_position_memory(o_kreuzer_1_m_list)
    ship_initializer.o_kreuzer_1.set_position(o_kreuzer_1_p_list)

    o_kreuzer_2_p_list = [tuple(item) for item in data["o_kreuzer_2_p"]]
    o_kreuzer_2_m_list = [tuple(item) for item in data["o_kreuzer_2_m"]] 
    ship_initializer.o_kreuzer_2.set_position_memory(o_kreuzer_2_m_list)
    ship_initializer.o_kreuzer_2.set_position(o_kreuzer_2_p_list)

    o_zerstoerer_1_p_list = [tuple(item) for item in data["o_zerstoerer_1_p"]]
    o_zerstoerer_1_m_list = [tuple(item) for item in data["o_zerstoerer_1_m"]] 
    ship_initializer.o_zerstoerer_1.set_position_memory(o_zerstoerer_1_m_list)
    ship_initializer.o_zerstoerer_1.set_position(o_zerstoerer_1_p_list)

    o_zerstoerer_2_p_list = [tuple(item) for item in data["o_zerstoerer_2_p"]]
    o_zerstoerer_2_m_list = [tuple(item) for item in data["o_zerstoerer_2_m"]] 
    ship_initializer.o_zerstoerer_2.set_position_memory(o_zerstoerer_2_m_list)
    ship_initializer.o_zerstoerer_2.set_position(o_zerstoerer_2_p_list)

    o_zerstoerer_3_p_list = [tuple(item) for item in data["o_zerstoerer_3_p"]]
    o_zerstoerer_3_m_list = [tuple(item) for item in data["o_zerstoerer_3_m"]] 
    ship_initializer.o_zerstoerer_3.set_position_memory(o_zerstoerer_3_m_list)
    ship_initializer.o_zerstoerer_3.set_position(o_zerstoerer_3_p_list)

    o_uboot_1_p_list = [tuple(item) for item in data["o_uboot_1_p"]]
    o_uboot_1_m_list = [tuple(item) for item in data["o_uboot_1_m"]] 
    ship_initializer.o_uboot_1.set_position_memory(o_uboot_1_m_list)
    ship_initializer.o_uboot_1.set_position(o_uboot_1_p_list)

    o_uboot_2_p_list = [tuple(item) for item in data["o_uboot_2_p"]]
    o_uboot_2_m_list = [tuple(item) for item in data["o_uboot_2_m"]] 
    ship_initializer.o_uboot_2.set_position_memory(o_uboot_2_m_list)
    ship_initializer.o_uboot_2.set_position(o_uboot_2_p_list)

    o_uboot_3_p_list = [tuple(item) for item in data["o_uboot_3_p"]]
    o_uboot_3_m_list = [tuple(item) for item in data["o_uboot_3_m"]] 
    ship_initializer.o_uboot_3.set_position_memory(o_uboot_3_m_list)
    ship_initializer.o_uboot_3.set_position(o_uboot_3_p_list)

    o_uboot_4_p_list = [tuple(item) for item in data["o_uboot_4_p"]]
    o_uboot_4_m_list = [tuple(item) for item in data["o_uboot_4_m"]] 
    ship_initializer.o_uboot_4.set_position_memory(o_uboot_4_m_list)
    ship_initializer.o_uboot_4.set_position(o_uboot_4_p_list)




def store_data(data):
    """Function that saves the game data into a file for later reading and continuing the game
    """

    #getting postion data of all player 1 (player) ships and store them via tupel lists
    #variable explanation: p-(code letter for player 1)- Schlachtschiff1 -(unique ship name)- p/m -
    #(p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)
    data["p_schlachtschiff_1_m"] = ship_initializer.p_schlachtschiff_1.get_position_memory()
    data["p_schlachtschiff_1_p"] = ship_initializer.p_schlachtschiff_1.get_position()


    data["p_kreuzer_1_m"] = ship_initializer.p_kreuzer_1.get_position_memory()
    data["p_kreuzer_1_p"] = ship_initializer.p_kreuzer_1.get_position()

    data["p_kreuzer_2_m"] = ship_initializer.p_kreuzer_2.get_position_memory()
    data["p_kreuzer_2_p"] = ship_initializer.p_kreuzer_2.get_position()

    data["p_zerstoerer_1_m"] = ship_initializer.p_zerstoerer_1.get_position_memory()
    data["p_zerstoerer_1_p"] = ship_initializer.p_zerstoerer_1.get_position()

    data["p_zerstoerer_2_m"] = ship_initializer.p_zerstoerer_2.get_position_memory()
    data["p_zerstoerer_2_p"] = ship_initializer.p_zerstoerer_2.get_position()

    data["p_zerstoerer_3_m"] = ship_initializer.p_zerstoerer_3.get_position_memory()
    data["p_zerstoerer_3_p"] = ship_initializer.p_zerstoerer_3.get_position()

    data["p_uboot_1m"] = ship_initializer.p_uboot_1.get_position_memory()
    data["p_uboot_1p"] = ship_initializer.p_uboot_1.get_position()

    data["p_uboot_2_m"] = ship_initializer.p_uboot_2.get_position_memory()
    data["p_uboot_2_p"] = ship_initializer.p_uboot_2.get_position()

    data["p_uboot_3_m"] = ship_initializer.p_uboot_3.get_position_memory()
    data["p_uboot_3_p"] = ship_initializer.p_uboot_3.get_position()

    data["p_uboot_4_m"] = ship_initializer.p_uboot_4.get_position_memory()
    data["p_uboot_4_p"] = ship_initializer.p_uboot_4.get_position()

    # getting postion data of all player 2 (opponent) ships and store them via tupel lists
    # variable explanation: o-(code letter for player 2)- Schlachtschiff1 -(unique ship name)- p/m -
    # (p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)
    data["o_schlachtschiff_1_m"] = ship_initializer.o_schlachtschiff_1.get_position_memory()
    data["o_schlachtschiff_1_p"] = ship_initializer.o_schlachtschiff_1.get_position()


    data["o_kreuzer_1_m"] = ship_initializer.o_kreuzer_1.get_position_memory()
    data["o_kreuzer_1_p"] = ship_initializer.o_kreuzer_1.get_position()

    data["o_kreuzer_2_m"] = ship_initializer.o_kreuzer_2.get_position_memory()
    data["o_kreuzer_2_p"] = ship_initializer.o_kreuzer_2.get_position()

    data["o_zerstoerer_1_m"] = ship_initializer.o_zerstoerer_1.get_position_memory()
    data["o_zerstoerer_1_p"] = ship_initializer.o_zerstoerer_1.get_position()

    data["o_zerstoerer_2_m"] = ship_initializer.o_zerstoerer_2.get_position_memory()
    data["o_zerstoerer_2_p"] = ship_initializer.o_zerstoerer_2.get_position()

    data["o_zerstoerer_3_m"] = ship_initializer.o_zerstoerer_3.get_position_memory()
    data["o_zerstoerer_3_p"] = ship_initializer.o_zerstoerer_3.get_position()

    data["o_uboot_1_m"] = ship_initializer.o_uboot_1.get_position_memory()
    data["o_uboot_1_p"] = ship_initializer.o_uboot_1.get_position()

    data["o_uboot_2_m"] = ship_initializer.o_uboot_2.get_position_memory()
    data["o_uboot_2_p"] = ship_initializer.o_uboot_2.get_position()

    data["o_uboot_3_m"] = ship_initializer.o_uboot_3.get_position_memory()
    data["o_uboot_3_p"] = ship_initializer.o_uboot_3.get_position()

    data["o_uboot_4_m"] = ship_initializer.o_uboot_4.get_position_memory()
    data["o_uboot_4_p"] = ship_initializer.o_uboot_4.get_position()
    

    # saves data of first successfuly hitted postion from oponent by cpu
    data["first_cpu_memory"] = output_manager.user_1.get_first_cpu_memory()
    # saves cpu hitting status
    data["shooting_iq"] = output_manager.user_1.get_shooting_iq()
    # saves cpu direction for following hits
    data["direction"] = output_manager.user_1.get_direction()
    # saves name of player 1
    data["player_name_1"] = output_manager.user_1.get_name()
    # saves name of player 2
    data["player_name_2"] = output_manager.user_2.get_name()
    # saves amount of left unsunken ships from player 1
    data["player_ships"] = output_manager.user_1.get_left_ships()
    # saves amount of left unsunken ships from player 2
    data["opponent_ships"] = output_manager.user_2.get_left_ships()
    # saves leakedBoard 1 to restore all informations of ship position (player 1 ships)
    data["leaked_board_1"] = python_game.leaked_board_1
    # saves leakedBoard 2 to restore all informations of ship position (player 2 ships)
    data["leaked_board_2"] = python_game.leaked_board_2
    # saves hiddenBoard 1 to restore all informations of hitted positions (player 1 ships)
    data["hidden_board_1"] = python_game.hidden_board_1
    # saves hiddenBoard 2 to restore all informations of hitted positions (player 2 ships)
    data["hidden_board_2"] = python_game.hidden_board_2
    # saves information if storage data is available (1) or not (0)
    data["storage_available"] = 1
