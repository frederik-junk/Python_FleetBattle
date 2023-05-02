import circularImportFixing
import outputmanager

def loadData(data):
        outputmanager.user1.setName(data["playerName1"])
        outputmanager.user2.setName(data["playerName2"])
        outputmanager.user1.setLeftShips(data["playerShips"])
        outputmanager.user1.setLeftShips(data["opponentShips"])

        pSchlachtschiffpList = [tuple(item) for item in data["pSchlachtschiff1p"]]
        pSchlachtschiffmList = [tuple(item) for item in data["pSchlachtschiff1m"]] 
        circularImportFixing.pSchlachtschiff1.setPositionMemory(pSchlachtschiffmList)
        circularImportFixing.pSchlachtschiff1.setPosition(pSchlachtschiffpList)
        
        """
        pKreuzer1pList = [tuple(item) for item in data["pKreuzer1p"]]
        pKreuzer1mList = [tuple(item) for item in data["pKreuzer1m"]] 
        circularImportFixing.pKreuzer1.setPositionMemory(pKreuzer1mList)
        circularImportFixing.pKreuzer1.setPosition(pKreuzer1pList)

        pKreuzer2pList = [tuple(item) for item in data["pKreuzer2p"]]
        pKreuzer2mList = [tuple(item) for item in data["pKreuzer2m"]] 
        circularImportFixing.pKreuzer2.setPositionMemory(pKreuzer2mList)
        circularImportFixing.pKreuzer2.setPosition(pKreuzer2pList)

        pZerstoerer1pList = [tuple(item) for item in data["pZerstoerer1p"]]
        pZerstoerer1mList = [tuple(item) for item in data["pZerstoerer1m"]] 
        circularImportFixing.pZerstoerer1.setPositionMemory(pZerstoerer1mList)
        circularImportFixing.pZerstoerer1.setPosition(pZerstoerer1pList)

        pZerstoerer2pList = [tuple(item) for item in data["pZerstoerer2p"]]
        pZerstoerer2mList = [tuple(item) for item in data["pZerstoerer2m"]] 
        circularImportFixing.pZerstoerer2.setPositionMemory(pZerstoerer2mList)
        circularImportFixing.pZerstoerer2.setPosition(pZerstoerer2pList)

        pZerstoerer3pList = [tuple(item) for item in data["pZerstoerer3p"]]
        pZerstoerer3mList = [tuple(item) for item in data["pZerstoerer3m"]] 
        circularImportFixing.pZerstoerer3.setPositionMemory(pZerstoerer3mList)
        circularImportFixing.pZerstoerer3.setPosition(pZerstoerer3pList)

        pUboot1pList = [tuple(item) for item in data["pUboot1p"]]
        pUboot1mList = [tuple(item) for item in data["pUboot1m"]] 
        circularImportFixing.pUboot1.setPositionMemory(pUboot1mList)
        circularImportFixing.pUboot1.setPosition(pUboot1pList)

        pUboot2pList = [tuple(item) for item in data["pUboot2p"]]
        pUboot2mList = [tuple(item) for item in data["pUboot2m"]] 
        circularImportFixing.pUboot2.setPositionMemory(pUboot2mList)
        circularImportFixing.pUboot2.setPosition(pUboot2pList)

        pUboot3pList = [tuple(item) for item in data["pUboot3p"]]
        pUboot3mList = [tuple(item) for item in data["pUboot3m"]] 
        circularImportFixing.pUboot3.setPositionMemory(pUboot3mList)
        circularImportFixing.pUboot3.setPosition(pUboot3pList)

        pUboot4pList = [tuple(item) for item in data["pUboot4p"]]
        pUboot4mList = [tuple(item) for item in data["pUboot4m"]] 
        circularImportFixing.pUboot4.setPositionMemory(pUboot4mList)
        circularImportFixing.pUboot4.setPosition(pUboot4pList)

        """

        oSchlachtschiff1pList = [tuple(item) for item in data["oSchlachtschiff1p"]]
        oSchlachtschiff1mList = [tuple(item) for item in data["oSchlachtschiff1m"]]
        circularImportFixing.oSchlachtschiff1.setPositionMemory(oSchlachtschiff1mList)
        circularImportFixing.oSchlachtschiff1.setPosition(oSchlachtschiff1pList)
        
        """
        oKreuzer1pList = [tuple(item) for item in data["oKreuzer1p"]]
        oKreuzer1mList = [tuple(item) for item in data["oKreuzer1m"]] 
        circularImportFixing.oKreuzer1.setPositionMemory(oKreuzer1mList)
        circularImportFixing.oKreuzer1.setPosition(oKreuzer1pList)

        oKreuzer2pList = [tuple(item) for item in data["oKreuzer2p"]]
        oKreuzer2mList = [tuple(item) for item in data["oKreuzer2m"]] 
        circularImportFixing.oKreuzer2.setPositionMemory(oKreuzer2mList)
        circularImportFixing.oKreuzer2.setPosition(oKreuzer2pList)

        oZerstoerer1pList = [tuple(item) for item in data["oZerstoerer1p"]]
        oZerstoerer1mList = [tuple(item) for item in data["oZerstoerer1m"]] 
        circularImportFixing.oZerstoerer1.setPositionMemory(oZerstoerer1mList)
        circularImportFixing.oZerstoerer1.setPosition(oZerstoerer1pList)

        oZerstoerer2pList = [tuple(item) for item in data["oZerstoerer2p"]]
        oZerstoerer2mList = [tuple(item) for item in data["oZerstoerer2m"]] 
        circularImportFixing.oZerstoerer2.setPositionMemory(oZerstoerer2mList)
        circularImportFixing.oZerstoerer2.setPosition(oZerstoerer2pList)

        oZerstoerer3pList = [tuple(item) for item in data["oZerstoerer3p"]]
        oZerstoerer3mList = [tuple(item) for item in data["oZerstoerer3m"]] 
        circularImportFixing.oZerstoerer3.setPositionMemory(oZerstoerer3mList)
        circularImportFixing.oZerstoerer3.setPosition(oZerstoerer3pList)

        oUboot1pList = [tuple(item) for item in data["oUboot1p"]]
        oUboot1mList = [tuple(item) for item in data["oUboot1m"]] 
        circularImportFixing.oUboot1.setPositionMemory(oUboot1mList)
        circularImportFixing.oUboot1.setPosition(oUboot1pList)

        oUboot2pList = [tuple(item) for item in data["oUboot2p"]]
        oUboot2mList = [tuple(item) for item in data["oUboot2m"]] 
        circularImportFixing.oUboot2.setPositionMemory(oUboot2mList)
        circularImportFixing.oUboot2.setPosition(oUboot2pList)

        oUboot3pList = [tuple(item) for item in data["oUboot3p"]]
        oUboot3mList = [tuple(item) for item in data["oUboot3m"]] 
        circularImportFixing.oUboot3.setPositionMemory(oUboot3mList)
        circularImportFixing.oUboot3.setPosition(oUboot3pList)

        oUboot4pList = [tuple(item) for item in data["oUboot4p"]]
        oUboot4mList = [tuple(item) for item in data["oUboot4m"]] 
        circularImportFixing.oUboot4.setPositionMemory(oUboot4mList)
        circularImportFixing.oUboot4.setPosition(oUboot4pList)

        """

def storeData(data):
        data["pSchlachtschiff1m"] = circularImportFixing.pSchlachtschiff1.getPositionMemory()
        data["pSchlachtschiff1p"] = circularImportFixing.pSchlachtschiff1.getPosition()
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
        data["oSchlachtschiff1m"] = circularImportFixing.oSchlachtschiff1.getPositionMemory()
        data["oSchlachtschiff1p"] = circularImportFixing.oSchlachtschiff1.getPosition()
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
        data["playerShips"] = outputmanager.user1.getLeftShips()
        data["opponentShips"] = outputmanager.user2.getLeftShips()
        data["leakedBoard1"] = pythonGame.leakedBoard1
        data["leakedBoard2"] = pythonGame.leakedBoard2
        data["hiddenBoard1"] = pythonGame.hiddenBoard1
        data["hiddenBoard2"] = pythonGame.hiddenBoard2
        data["storage_available"] = 1