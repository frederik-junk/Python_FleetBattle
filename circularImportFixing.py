from shipmanager import Schlachtschiff


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
pSchlachtschiff1 = Schlachtschiff(emptyTupelList)
pSchlachtschiff1.classPlaceShip(leakedBoard3, pSchlachtschiff1)

