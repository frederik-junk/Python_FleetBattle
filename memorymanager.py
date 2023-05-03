import shipinitializer
import outputmanager
import pythonGame


# function to load all data elements after game restart
def loadData(data, gameMode):
    # checking if cpu data is necessary (gamemode 1)
    if gameMode == 1:
        # cordinates of tupel with succesful hit
        firstCpuMemory = [tuple(item) for item in data["firstCpuMemory"]]
        outputmanager.user1.setFirstCpuMemory(firstCpuMemory)
        # cpu status (diffrent steps until final ship finish)
        outputmanager.user1.setShootingIq(data["shootingIq"])
        # direction for next hits after succesful first hit
        outputmanager.user1.setDirection(data["direction"])
    # load name of Player 1
    outputmanager.user1.setName(data["playerName1"])
    # load name of Player 2
    outputmanager.user2.setName(data["playerName2"])
    # loading amount of sunken ships (player 1)
    outputmanager.user1.setLeftShips(data["playerShips"])
    # loading amount of sunken ships (player 2)
    outputmanager.user1.setLeftShips(data["opponentShips"])

    # initalize all player 1 (player) ships with memory data of postion and hitted spots
    # variable explanation: p-(code letter for player 1)- Schlachtschiff1 -(unique ship name)- p/m -(p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)

    pSchlachtschiffpList = [tuple(item) for item in data["pSchlachtschiff1p"]]
    pSchlachtschiffmList = [tuple(item) for item in data["pSchlachtschiff1m"]]
    shipinitializer.pSchlachtschiff1.setPositionMemory(pSchlachtschiffmList)
    shipinitializer.pSchlachtschiff1.setPosition(pSchlachtschiffpList)

    """
        pKreuzer1pList = [tuple(item) for item in data["pKreuzer1p"]]
        pKreuzer1mList = [tuple(item) for item in data["pKreuzer1m"]] 
        shipinitializer.pKreuzer1.setPositionMemory(pKreuzer1mList)
        shipinitializer.pKreuzer1.setPosition(pKreuzer1pList)

        pKreuzer2pList = [tuple(item) for item in data["pKreuzer2p"]]
        pKreuzer2mList = [tuple(item) for item in data["pKreuzer2m"]] 
        shipinitializer.pKreuzer2.setPositionMemory(pKreuzer2mList)
        shipinitializer.pKreuzer2.setPosition(pKreuzer2pList)

        pZerstoerer1pList = [tuple(item) for item in data["pZerstoerer1p"]]
        pZerstoerer1mList = [tuple(item) for item in data["pZerstoerer1m"]] 
        shipinitializer.pZerstoerer1.setPositionMemory(pZerstoerer1mList)
        shipinitializer.pZerstoerer1.setPosition(pZerstoerer1pList)

        pZerstoerer2pList = [tuple(item) for item in data["pZerstoerer2p"]]
        pZerstoerer2mList = [tuple(item) for item in data["pZerstoerer2m"]] 
        shipinitializer.pZerstoerer2.setPositionMemory(pZerstoerer2mList)
        shipinitializer.pZerstoerer2.setPosition(pZerstoerer2pList)

        pZerstoerer3pList = [tuple(item) for item in data["pZerstoerer3p"]]
        pZerstoerer3mList = [tuple(item) for item in data["pZerstoerer3m"]] 
        shipinitializer.pZerstoerer3.setPositionMemory(pZerstoerer3mList)
        shipinitializer.pZerstoerer3.setPosition(pZerstoerer3pList)

        pUboot1pList = [tuple(item) for item in data["pUboot1p"]]
        pUboot1mList = [tuple(item) for item in data["pUboot1m"]] 
        shipinitializer.pUboot1.setPositionMemory(pUboot1mList)
        shipinitializer.pUboot1.setPosition(pUboot1pList)

        pUboot2pList = [tuple(item) for item in data["pUboot2p"]]
        pUboot2mList = [tuple(item) for item in data["pUboot2m"]] 
        shipinitializer.pUboot2.setPositionMemory(pUboot2mList)
        shipinitializer.pUboot2.setPosition(pUboot2pList)

        pUboot3pList = [tuple(item) for item in data["pUboot3p"]]
        pUboot3mList = [tuple(item) for item in data["pUboot3m"]] 
        shipinitializer.pUboot3.setPositionMemory(pUboot3mList)
        shipinitializer.pUboot3.setPosition(pUboot3pList)

        pUboot4pList = [tuple(item) for item in data["pUboot4p"]]
        pUboot4mList = [tuple(item) for item in data["pUboot4m"]] 
        shipinitializer.pUboot4.setPositionMemory(pUboot4mList)
        shipinitializer.pUboot4.setPosition(pUboot4pList)

        """

    # initalize all player 2 (opponent) ships with memory data of postion and hitted spots
    # variable explanation: o-(code letter for player 2)- Schlachtschiff1 -(unique ship name)- p/m -(p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)

    oSchlachtschiff1pList = [tuple(item) for item in data["oSchlachtschiff1p"]]
    oSchlachtschiff1mList = [tuple(item) for item in data["oSchlachtschiff1m"]]
    shipinitializer.oSchlachtschiff1.setPositionMemory(oSchlachtschiff1mList)
    shipinitializer.oSchlachtschiff1.setPosition(oSchlachtschiff1pList)

    """
        oKreuzer1pList = [tuple(item) for item in data["oKreuzer1p"]]
        oKreuzer1mList = [tuple(item) for item in data["oKreuzer1m"]] 
        shipinitializer.oKreuzer1.setPositionMemory(oKreuzer1mList)
        shipinitializer.oKreuzer1.setPosition(oKreuzer1pList)

        oKreuzer2pList = [tuple(item) for item in data["oKreuzer2p"]]
        oKreuzer2mList = [tuple(item) for item in data["oKreuzer2m"]] 
        shipinitializer.oKreuzer2.setPositionMemory(oKreuzer2mList)
        shipinitializer.oKreuzer2.setPosition(oKreuzer2pList)

        oZerstoerer1pList = [tuple(item) for item in data["oZerstoerer1p"]]
        oZerstoerer1mList = [tuple(item) for item in data["oZerstoerer1m"]] 
        shipinitializer.oZerstoerer1.setPositionMemory(oZerstoerer1mList)
        shipinitializer.oZerstoerer1.setPosition(oZerstoerer1pList)

        oZerstoerer2pList = [tuple(item) for item in data["oZerstoerer2p"]]
        oZerstoerer2mList = [tuple(item) for item in data["oZerstoerer2m"]] 
        shipinitializer.oZerstoerer2.setPositionMemory(oZerstoerer2mList)
        shipinitializer.oZerstoerer2.setPosition(oZerstoerer2pList)

        oZerstoerer3pList = [tuple(item) for item in data["oZerstoerer3p"]]
        oZerstoerer3mList = [tuple(item) for item in data["oZerstoerer3m"]] 
        shipinitializer.oZerstoerer3.setPositionMemory(oZerstoerer3mList)
        shipinitializer.oZerstoerer3.setPosition(oZerstoerer3pList)

        oUboot1pList = [tuple(item) for item in data["oUboot1p"]]
        oUboot1mList = [tuple(item) for item in data["oUboot1m"]] 
        shipinitializer.oUboot1.setPositionMemory(oUboot1mList)
        shipinitializer.oUboot1.setPosition(oUboot1pList)

        oUboot2pList = [tuple(item) for item in data["oUboot2p"]]
        oUboot2mList = [tuple(item) for item in data["oUboot2m"]] 
        shipinitializer.oUboot2.setPositionMemory(oUboot2mList)
        shipinitializer.oUboot2.setPosition(oUboot2pList)

        oUboot3pList = [tuple(item) for item in data["oUboot3p"]]
        oUboot3mList = [tuple(item) for item in data["oUboot3m"]] 
        shipinitializer.oUboot3.setPositionMemory(oUboot3mList)
        shipinitializer.oUboot3.setPosition(oUboot3pList)

        oUboot4pList = [tuple(item) for item in data["oUboot4p"]]
        oUboot4mList = [tuple(item) for item in data["oUboot4m"]] 
        shipinitializer.oUboot4.setPositionMemory(oUboot4mList)
        shipinitializer.oUboot4.setPosition(oUboot4pList)

        """


def storeData(data):
    # getting postion data of all player 1 (player) ships and store them via tupel lists
    # variable explanation: p-(code letter for player 1)- Schlachtschiff1 -(unique ship name)- p/m -(p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)
    data["pSchlachtschiff1m"] = shipinitializer.pSchlachtschiff1.getPositionMemory()
    data["pSchlachtschiff1p"] = shipinitializer.pSchlachtschiff1.getPosition()

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
    # variable explanation: o-(code letter for player 2)- Schlachtschiff1 -(unique ship name)- p/m -(p = tupellist with unhitted ship spots/ m = tupellist with hitted ship spots)
    data["oSchlachtschiff1m"] = shipinitializer.oSchlachtschiff1.getPositionMemory()
    data["oSchlachtschiff1p"] = shipinitializer.oSchlachtschiff1.getPosition()

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

    # saving data of first successfuly hitted postion from oponent by cpu
    data["firstCpuMemory"] = outputmanager.user1.getFirstCpuMemory()
    # saving cpu hitting status
    data["shootingIq"] = outputmanager.user1.getShootingIq()
    # saving cpu direction for following hits
    data["direction"] = outputmanager.user1.getDirection()
    # saving name of player 1
    data["playerName1"] = outputmanager.user1.getName()
    # saving name of player 2
    data["playerName2"] = outputmanager.user2.getName()
    # saving amount of left unsunken ships from player 1
    data["playerShips"] = outputmanager.user1.getLeftShips()
    # saving amount of left unsunken ships from player 2
    data["opponentShips"] = outputmanager.user2.getLeftShips()
    # saving leakedBoard 1 to restore all informations of ship position (player 1 ships)
    data["leakedBoard1"] = pythonGame.leakedBoard1
    # saving leakedBoard 2 to restore all informations of ship position (player 2 ships)
    data["leakedBoard2"] = pythonGame.leakedBoard2
    # saving hiddenBoard 1 to restore all informations of hitted positions (player 1 ships)
    data["hiddenBoard1"] = pythonGame.hiddenBoard1
    # saving hiddenBoard 2 to restore all informations of hitted positions (player 2 ships)
    data["hiddenBoard2"] = pythonGame.hiddenBoard2
    # saving information if storage data is available (1) or not (0)
    data["storage_available"] = 1
