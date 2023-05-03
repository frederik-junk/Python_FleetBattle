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
        first_cpu_memory = [tuple(item) for item in data["first_cpu_memory"]]
        output_manager.user1.set_first_cpu_memory(first_cpu_memory)
        # cpu status (diffrent steps until final ship finish)
        output_manager.user1.set_shooting_iq(data["shootingIq"])
        # direction for next hits after succesful first hit
        output_manager.user1.set_direction(data["direction"])
    # loads name of Player 1
    output_manager.user1.set_name(data["playerName1"])
    # loads name of Player 2
    output_manager.user2.set_name(data["playerName2"])
    # loads amount of sunken ships (player 1)
    output_manager.user1.set_left_ships(data["playerShips"])
    # loads amount of sunken ships (player 2)
    output_manager.user1.set_left_ships(data["opponentShips"])

    # initalize all player 1 (player) ships with memory data of postion and hitted spots
    # variable explanation: p-(code letter for player 1)- Schlachtschiff1 -(unique ship name)- p/m -
    # (p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)

    p_schlachtschiff_p_list = [tuple(item) for item in data["pSchlachtschiff1p"]]
    p_schlachtschiff_m_list = [tuple(item) for item in data["pSchlachtschiff1m"]]
    ship_initializer.pSchlachtschiff1.set_position_memory(p_schlachtschiff_m_list)
    ship_initializer.pSchlachtschiff1.setPosition(p_schlachtschiff_p_list)
    """
    pKreuzer1pList = [tuple(item) for item in data["pKreuzer1p"]]
    pKreuzer1mList = [tuple(item) for item in data["pKreuzer1m"]] 
    shipinitializer.pKreuzer1.set_position_memory(pKreuzer1mList)
    shipinitializer.pKreuzer1.setPosition(pKreuzer1pList)

    pKreuzer2pList = [tuple(item) for item in data["pKreuzer2p"]]
    pKreuzer2mList = [tuple(item) for item in data["pKreuzer2m"]] 
    shipinitializer.pKreuzer2.set_position_memory(pKreuzer2mList)
    shipinitializer.pKreuzer2.setPosition(pKreuzer2pList)

    pZerstoerer1pList = [tuple(item) for item in data["pZerstoerer1p"]]
    pZerstoerer1mList = [tuple(item) for item in data["pZerstoerer1m"]] 
    shipinitializer.pZerstoerer1.set_position_memory(pZerstoerer1mList)
    shipinitializer.pZerstoerer1.setPosition(pZerstoerer1pList)

    pZerstoerer2pList = [tuple(item) for item in data["pZerstoerer2p"]]
    pZerstoerer2mList = [tuple(item) for item in data["pZerstoerer2m"]] 
    shipinitializer.pZerstoerer2.set_position_memory(pZerstoerer2mList)
    shipinitializer.pZerstoerer2.setPosition(pZerstoerer2pList)

    pZerstoerer3pList = [tuple(item) for item in data["pZerstoerer3p"]]
    pZerstoerer3mList = [tuple(item) for item in data["pZerstoerer3m"]] 
    shipinitializer.pZerstoerer3.set_position_memory(pZerstoerer3mList)
    shipinitializer.pZerstoerer3.setPosition(pZerstoerer3pList)

    pUboot1pList = [tuple(item) for item in data["pUboot1p"]]
    pUboot1mList = [tuple(item) for item in data["pUboot1m"]] 
    shipinitializer.pUboot1.set_position_memory(pUboot1mList)
    shipinitializer.pUboot1.setPosition(pUboot1pList)

    pUboot2pList = [tuple(item) for item in data["pUboot2p"]]
    pUboot2mList = [tuple(item) for item in data["pUboot2m"]] 
    shipinitializer.pUboot2.set_position_memory(pUboot2mList)
    shipinitializer.pUboot2.setPosition(pUboot2pList)

    pUboot3pList = [tuple(item) for item in data["pUboot3p"]]
    pUboot3mList = [tuple(item) for item in data["pUboot3m"]] 
    shipinitializer.pUboot3.set_position_memory(pUboot3mList)
    shipinitializer.pUboot3.setPosition(pUboot3pList)

    pUboot4pList = [tuple(item) for item in data["pUboot4p"]]
    pUboot4mList = [tuple(item) for item in data["pUboot4m"]] 
    shipinitializer.pUboot4.set_position_memory(pUboot4mList)
    shipinitializer.pUboot4.setPosition(pUboot4pList)

    """

    # initalize all player 2 (opponent) ships with memory data of postion and hitted spots
    # variable explanation: o-(code letter for player 2)- Schlachtschiff1 -(unique ship name)- p/m -
    # (p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)

    o_schlachtschiff_1_p_list = [tuple(item) for item in data["oSchlachtschiff1p"]]
    o_schlachtschiff_1_m_list = [tuple(item) for item in data["oSchlachtschiff1m"]]
    ship_initializer.oSchlachtschiff1.set_position_memory(o_schlachtschiff_1_m_list)
    ship_initializer.oSchlachtschiff1.setPosition(o_schlachtschiff_1_p_list)
    """
    oKreuzer1pList = [tuple(item) for item in data["oKreuzer1p"]]
    oKreuzer1mList = [tuple(item) for item in data["oKreuzer1m"]] 
    shipinitializer.oKreuzer1.set_position_memory(oKreuzer1mList)
    shipinitializer.oKreuzer1.setPosition(oKreuzer1pList)

    oKreuzer2pList = [tuple(item) for item in data["oKreuzer2p"]]
    oKreuzer2mList = [tuple(item) for item in data["oKreuzer2m"]] 
    shipinitializer.oKreuzer2.set_position_memory(oKreuzer2mList)
    shipinitializer.oKreuzer2.setPosition(oKreuzer2pList)

    oZerstoerer1pList = [tuple(item) for item in data["oZerstoerer1p"]]
    oZerstoerer1mList = [tuple(item) for item in data["oZerstoerer1m"]] 
    shipinitializer.oZerstoerer1.set_position_memory(oZerstoerer1mList)
    shipinitializer.oZerstoerer1.setPosition(oZerstoerer1pList)

    oZerstoerer2pList = [tuple(item) for item in data["oZerstoerer2p"]]
    oZerstoerer2mList = [tuple(item) for item in data["oZerstoerer2m"]] 
    shipinitializer.oZerstoerer2.set_position_memory(oZerstoerer2mList)
    shipinitializer.oZerstoerer2.setPosition(oZerstoerer2pList)

    oZerstoerer3pList = [tuple(item) for item in data["oZerstoerer3p"]]
    oZerstoerer3mList = [tuple(item) for item in data["oZerstoerer3m"]] 
    shipinitializer.oZerstoerer3.set_position_memory(oZerstoerer3mList)
    shipinitializer.oZerstoerer3.setPosition(oZerstoerer3pList)

    oUboot1pList = [tuple(item) for item in data["oUboot1p"]]
    oUboot1mList = [tuple(item) for item in data["oUboot1m"]] 
    shipinitializer.oUboot1.set_position_memory(oUboot1mList)
    shipinitializer.oUboot1.setPosition(oUboot1pList)

    oUboot2pList = [tuple(item) for item in data["oUboot2p"]]
    oUboot2mList = [tuple(item) for item in data["oUboot2m"]] 
    shipinitializer.oUboot2.set_position_memory(oUboot2mList)
    shipinitializer.oUboot2.setPosition(oUboot2pList)

    oUboot3pList = [tuple(item) for item in data["oUboot3p"]]
    oUboot3mList = [tuple(item) for item in data["oUboot3m"]] 
    shipinitializer.oUboot3.set_position_memory(oUboot3mList)
    shipinitializer.oUboot3.setPosition(oUboot3pList)

    oUboot4pList = [tuple(item) for item in data["oUboot4p"]]
    oUboot4mList = [tuple(item) for item in data["oUboot4m"]] 
    shipinitializer.oUboot4.set_position_memory(oUboot4mList)
    shipinitializer.oUboot4.setPosition(oUboot4pList)

    """


def store_data(data):
    """Function that saves the game data into a file for later reading and continuing the game
    """

    #getting postion data of all player 1 (player) ships and store them via tupel lists
    #variable explanation: p-(code letter for player 1)- Schlachtschiff1 -(unique ship name)- p/m -
    #(p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)
    data["pSchlachtschiff1m"] = ship_initializer.pSchlachtschiff1.getPositionMemory()
    data["pSchlachtschiff1p"] = ship_initializer.pSchlachtschiff1.getPosition()

    """
    data["pKreuzer1m"] = shipinitializer.pKreuzer1.getPositionMemory()
    data["pKreuzer1p"] = shipinitializer.pKreuzer1.getPosition()

    data["pKreuzer2m"] = shipinitializer.pKreuzer2.getPositionMemory()
    data["pKreuzer2p"] = shipinitializer.pKreuzer2.getPosition()

    data["pZerstoerer1m"] = shipinitializer.pZerstoerer1.getPositionMemory()
    data["pZerstoerer1p"] = shipinitializer.pZerstoerer1.getPosition()

    data["pZerstoerer2m"] = shipinitializer.pZerstoerer2.getPositionMemory()
    data["pZerstoerer2p"] = shipinitializer.pZerstoerer2.getPosition()

    data["pZerstoerer3m"] = shipinitializer.pZerstoerer3.getPositionMemory()
    data["pZerstoerer3p"] = shipinitializer.pZerstoerer3.getPosition()

    data["pUboot1m"] = shipinitializer.pUboot1.getPositionMemory()
    data["pUboot1p"] = shipinitializer.pUboot1.getPosition()

    data["pUboot2m"] = shipinitializer.pUboot2.getPositionMemory()
    data["pUboot2p"] = shipinitializer.pUboot2.getPosition()

    data["pUboot3m"] = shipinitializer.pUboot3.getPositionMemory()
    data["pUboot3p"] = shipinitializer.pUboot3.getPosition()

    data["pUboot4m"] = shipinitializer.pUboot4.getPositionMemory()
    data["pUboot4p"] = shipinitializer.pUboot4.getPosition()
    """
    # getting postion data of all player 2 (opponent) ships and store them via tupel lists
    # variable explanation: o-(code letter for player 2)- Schlachtschiff1 -(unique ship name)- p/m -
    # (p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)
    data["oSchlachtschiff1m"] = ship_initializer.oSchlachtschiff1.getPositionMemory()
    data["oSchlachtschiff1p"] = ship_initializer.oSchlachtschiff1.getPosition()

    """
    data["oKreuzer1m"] = shipinitializer.oKreuzer1.getPositionMemory()
    data["oKreuzer1p"] = shipinitializer.oKreuzer1.getPosition()

    data["oKreuzer2m"] = shipinitializer.oKreuzer2.getPositionMemory()
    data["oKreuzer2p"] = shipinitializer.oKreuzer2.getPosition()

    data["oZerstoerer1m"] = shipinitializer.oZerstoerer1.getPositionMemory()
    data["oZerstoerer1p"] = shipinitializer.oZerstoerer1.getPosition()

    data["oZerstoerer2m"] = shipinitializer.oZerstoerer2.getPositionMemory()
    data["oZerstoerer2p"] = shipinitializer.oZerstoerer2.getPosition()

    data["oZerstoerer3m"] = shipinitializer.oZerstoerer3.getPositionMemory()
    data["oZerstoerer3p"] = shipinitializer.oZerstoerer3.getPosition()

    data["oUboot1m"] = shipinitializer.oUboot1.getPositionMemory()
    data["oUboot1p"] = shipinitializer.oUboot1.getPosition()

    data["oUboot2m"] = shipinitializer.oUboot2.getPositionMemory()
    data["oUboot2p"] = shipinitializer.oUboot2.getPosition()

    data["oUboot3m"] = shipinitializer.oUboot3.getPositionMemory()
    data["oUboot3p"] = shipinitializer.oUboot3.getPosition()

    data["oUboot4m"] = shipinitializer.oUboot4.getPositionMemory()
    data["oUboot4p"] = shipinitializer.oUboot4.getPosition()
    """

    # saves data of first successfuly hitted postion from oponent by cpu
    data["first_cpu_memory"] = output_manager.user1.get_first_cpu_memory()
    # saves cpu hitting status
    data["shootingIq"] = output_manager.user1.get_shooting_iq()
    # saves cpu direction for following hits
    data["direction"] = output_manager.user1.get_direction()
    # saves name of player 1
    data["playerName1"] = output_manager.user1.get_name()
    # saves name of player 2
    data["playerName2"] = output_manager.user2.get_name()
    # saves amount of left unsunken ships from player 1
    data["playerShips"] = output_manager.user1.get_left_ships()
    # saves amount of left unsunken ships from player 2
    data["opponentShips"] = output_manager.user2.get_left_ships()
    # saves leakedBoard 1 to restore all informations of ship position (player 1 ships)
    data["leakedBoard1"] = python_game.leakedBoard1
    # saves leakedBoard 2 to restore all informations of ship position (player 2 ships)
    data["leakedBoard2"] = python_game.leakedBoard2
    # saves hiddenBoard 1 to restore all informations of hitted positions (player 1 ships)
    data["hiddenBoard1"] = python_game.hiddenBoard1
    # saves hiddenBoard 2 to restore all informations of hitted positions (player 2 ships)
    data["hiddenBoard2"] = python_game.hiddenBoard2
    # saves information if storage data is available (1) or not (0)
    data["storage_available"] = 1
