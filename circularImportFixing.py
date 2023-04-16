from shipmanager import *


letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow =   [0,0,0,0,0,0,0,0,0,0]
secondRow =  [0,0,0,0,0,0,0,0,0,0]
thirdRow =   [0,0,0,0,0,0,0,0,0,0]
fourthRow =  [0,0,0,0,0,0,0,0,0,0]
fifthRow =   [0,0,0,0,0,0,0,0,0,0]
sixthRow =   [0,0,0,0,0,0,0,0,0,0]
seventhRow = [0,0,0,0,0,0,0,0,0,0]
eighthRow =  [0,0,0,0,0,0,0,0,0,0]
ninethRow =  [0,0,0,0,0,0,0,0,0,0]
tenthRow =   [0,0,0,0,0,0,0,0,0,0]
leakedBoard3 = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]


emptyTupelList = []

#these are the user1 ship player or cpu
pSchlachtschiff1 = Schlachtschiff(emptyTupelList)

pKreuzer1 = Kreuzer(emptyTupelList)
pKreuzer2 = Kreuzer(emptyTupelList)

pZerstoerer1 = Zerstoerer(emptyTupelList)
pZerstoerer2 = Zerstoerer(emptyTupelList)
pZerstoerer3 = Zerstoerer(emptyTupelList)

pUboot1 = Uboot(emptyTupelList)
pUboot2 = Uboot(emptyTupelList)
pUboot3 = Uboot(emptyTupelList)
pUboot4 = Uboot(emptyTupelList)

playerShips = [pSchlachtschiff1, pKreuzer1, pKreuzer2, pZerstoerer1, pZerstoerer2, pZerstoerer3, pUboot1, pUboot2, pUboot3, pUboot4]

#these are are the user2 ships player1 or player2 
oSchlachtschiff1 = Schlachtschiff(emptyTupelList)

oKreuzer1 = Kreuzer(emptyTupelList)
oKreuzer2 = Kreuzer(emptyTupelList)

oZertsoerer1 = Zerstoerer(emptyTupelList)
oZerstoerer2 = Zerstoerer(emptyTupelList)
oZerstoerer3 = Zerstoerer(emptyTupelList)

oUboot1 = Uboot(emptyTupelList)
oUboot2 = Uboot(emptyTupelList)
oUboot3 = Uboot(emptyTupelList)
oUboot4 = Uboot(emptyTupelList)

opponentShips = [oSchlachtschiff1, oKreuzer1, oKreuzer2, oZertsoerer1, oZerstoerer2, oZerstoerer3, oUboot1, oUboot2, oUboot3, oUboot4]

oUboot1.classPlaceShip(emptyTupelList, oUboot1)