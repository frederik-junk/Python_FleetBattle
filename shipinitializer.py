"Module that initializes the ships of player and opponent"
import shipmanager

emptyTupelList = []
VARIABLE = 0

#these are the user1 ship player or cpu
pSchlachtschiff1 = shipmanager.Schlachtschiff(emptyTupelList, VARIABLE)

pKreuzer1 = shipmanager.Kreuzer(emptyTupelList, VARIABLE)
pKreuzer2 = shipmanager.Kreuzer(emptyTupelList, VARIABLE)

pZerstoerer1 = shipmanager.Zerstoerer(emptyTupelList, VARIABLE)
pZerstoerer2 = shipmanager.Zerstoerer(emptyTupelList, VARIABLE)
pZerstoerer3 = shipmanager.Zerstoerer(emptyTupelList, VARIABLE)

pUboot1 = shipmanager.Uboot(emptyTupelList, VARIABLE)
pUboot2 = shipmanager.Uboot(emptyTupelList, VARIABLE)
pUboot3 = shipmanager.Uboot(emptyTupelList, VARIABLE)
pUboot4 = shipmanager.Uboot(emptyTupelList, VARIABLE)

#playerShips = [pSchlachtschiff1, pKreuzer1, pKreuzer2, pZerstoerer1, pZerstoerer2, pZerstoerer3, pUboot1, pUboot2, pUboot3, pUboot4]
playerShips = [pSchlachtschiff1]

#these are are the user2 ships player1 or player2
oSchlachtschiff1 = shipmanager.Schlachtschiff(emptyTupelList, VARIABLE)

oKreuzer1 = shipmanager.Kreuzer(emptyTupelList, VARIABLE)
oKreuzer2 = shipmanager.Kreuzer(emptyTupelList, VARIABLE)

oZerstoerer1 = shipmanager.Zerstoerer(emptyTupelList, VARIABLE)
oZerstoerer2 = shipmanager.Zerstoerer(emptyTupelList, VARIABLE)
oZerstoerer3 = shipmanager.Zerstoerer(emptyTupelList, VARIABLE)

oUboot1 = shipmanager.Uboot(emptyTupelList, VARIABLE)
oUboot2 = shipmanager.Uboot(emptyTupelList, VARIABLE)
oUboot3 = shipmanager.Uboot(emptyTupelList, VARIABLE)
oUboot4 = shipmanager.Uboot(emptyTupelList, VARIABLE)

#opponentShips = [oSchlachtschiff1, oKreuzer1, oKreuzer2, oZerstoerer1, oZerstoerer2, oZerstoerer3, oUboot1, oUboot2, oUboot3, oUboot4]

opponentShips = [oSchlachtschiff1]




#initialize with empty List
emptyList = []
for ship in opponentShips:
    ship.setPositionMemory(emptyList)

for ship in playerShips:
    ship.setPositionMemory(emptyList)
