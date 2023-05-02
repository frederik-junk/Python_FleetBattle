"Module that initializes the ships of player and opponent"
import shipmanager

emptyTupelList = []
variable = 0

#these are the user1 ship player or cpu
pSchlachtschiff1 = shipmanager.Schlachtschiff(emptyTupelList, variable)

pKreuzer1 = shipmanager.Kreuzer(emptyTupelList, variable)
pKreuzer2 = shipmanager.Kreuzer(emptyTupelList, variable)

pZerstoerer1 = shipmanager.Zerstoerer(emptyTupelList, variable)
pZerstoerer2 = shipmanager.Zerstoerer(emptyTupelList, variable)
pZerstoerer3 = shipmanager.Zerstoerer(emptyTupelList, variable)

pUboot1 = shipmanager.Uboot(emptyTupelList, variable)
pUboot2 = shipmanager.Uboot(emptyTupelList, variable)
pUboot3 = shipmanager.Uboot(emptyTupelList, variable)
pUboot4 = shipmanager.Uboot(emptyTupelList, variable)

#playerShips = [pSchlachtschiff1, pKreuzer1, pKreuzer2, pZerstoerer1, pZerstoerer2, pZerstoerer3, pUboot1, pUboot2, pUboot3, pUboot4]
playerShips = [pSchlachtschiff1]

#these are are the user2 ships player1 or player2
oSchlachtschiff1 = shipmanager.Schlachtschiff(emptyTupelList, variable)

oKreuzer1 = shipmanager.Kreuzer(emptyTupelList, variable)
oKreuzer2 = shipmanager.Kreuzer(emptyTupelList, variable)

oZerstoerer1 = shipmanager.Zerstoerer(emptyTupelList, variable)
oZerstoerer2 = shipmanager.Zerstoerer(emptyTupelList, variable)
oZerstoerer3 = shipmanager.Zerstoerer(emptyTupelList, variable)

oUboot1 = shipmanager.Uboot(emptyTupelList, variable)
oUboot2 = shipmanager.Uboot(emptyTupelList, variable)
oUboot3 = shipmanager.Uboot(emptyTupelList, variable)
oUboot4 = shipmanager.Uboot(emptyTupelList, variable)

#opponentShips = [oSchlachtschiff1, oKreuzer1, oKreuzer2, oZerstoerer1, oZerstoerer2, oZerstoerer3, oUboot1, oUboot2, oUboot3, oUboot4]

opponentShips = [oSchlachtschiff1]




#initialize with empty List
emptyList = []
for ship in opponentShips:
    ship.setPositionMemory(emptyList)

for ship in playerShips:
    ship.setPositionMemory(emptyList)
