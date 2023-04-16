import shipmanager


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
pSchlachtschiff1 = shipmanager.Schlachtschiff(emptyTupelList)

pKreuzer1 = shipmanager.Kreuzer(emptyTupelList)
pKreuzer2 = shipmanager.Kreuzer(emptyTupelList)

pZerstoerer1 = shipmanager.Zerstoerer(emptyTupelList)
pZerstoerer2 = shipmanager.Zerstoerer(emptyTupelList)
pZerstoerer3 = shipmanager.Zerstoerer(emptyTupelList)

pUboot1 = shipmanager.Uboot(emptyTupelList)
pUboot2 = shipmanager.Uboot(emptyTupelList)
pUboot3 = shipmanager.Uboot(emptyTupelList)
pUboot4 = shipmanager.Uboot(emptyTupelList)

playerShips = [pSchlachtschiff1, pKreuzer1, pKreuzer2, pZerstoerer1, pZerstoerer2, pZerstoerer3, pUboot1, pUboot2, pUboot3, pUboot4]

#these are are the user2 ships player1 or player2 
oSchlachtschiff1 = shipmanager.Schlachtschiff(emptyTupelList)

oKreuzer1 = shipmanager.Kreuzer(emptyTupelList)
oKreuzer2 = shipmanager.Kreuzer(emptyTupelList)

oZertsoerer1 = shipmanager.Zerstoerer(emptyTupelList)
oZerstoerer2 = shipmanager.Zerstoerer(emptyTupelList)
oZerstoerer3 = shipmanager.Zerstoerer(emptyTupelList)

oUboot1 = shipmanager.Uboot(emptyTupelList)
oUboot2 = shipmanager.Uboot(emptyTupelList)
oUboot3 = shipmanager.Uboot(emptyTupelList)
oUboot4 = shipmanager.Uboot(emptyTupelList)

opponentShips = [oSchlachtschiff1, oKreuzer1, oKreuzer2, oZertsoerer1, oZerstoerer2, oZerstoerer3, oUboot1, oUboot2, oUboot3, oUboot4]


#pKreuzer1.classPlaceShip(leakedBoard3, pKreuzer1)
