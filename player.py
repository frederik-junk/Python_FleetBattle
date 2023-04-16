import shipmanager
import python_game
import oponent
import main

class Player:
    def __init__(self,name):
        self.__name = name
"""
#playerships
#no implementation yet might change later
pschlachtschiff1 = shipmanager.Schlachtschiff(((1,1),(1,2),(1,3),(1,4),(1,5)))
pkreuzer1 = shipmanager.Kreuzer(((1,1),(1,2),(1,3),(1,4)))
pkreuzer2 = shipmanager.Kreuzer(((1,1),(1,2),(1,3),(1,4)))
pzerstoerer1 = shipmanager.Zerstoerer(((1,1),(1,2),(1,3)))
pzerstoerer2 = shipmanager.Zerstoerer(((1,1),(1,2),(1,3)))
pzerstoerer3 = shipmanager.Zerstoerer(((1,1),(1,2),(1,3)))
puboot1 = shipmanager.UBoot(((1,1),(1,2)))
puboot2 = shipmanager.UBoot(((1,1),(1,2)))
puboot3 = shipmanager.UBoot(((1,1),(1,2)))
puboot4 = shipmanager.UBoot(((1,1),(1,2)))

playerShips = [pschlachtschiff1,pkreuzer1,pkreuzer2,pzerstoerer1,pzerstoerer2,pzerstoerer3,puboot1,puboot2,puboot3,puboot4]
def initPlayerShips():
    for ship in playerShips:
        length = ship.getSize()
        python_game.placeShip(python_gameleakedBoard2,length,ship)
"""
def playerAction():
    isHit = 1
    while(isHit != 0):
        #input hitting field
        hittingInput = input("Bitte geben sie an auf welches Feld schießen wollen")
        #split row and column
        row = python_game.splitRow(placementInput)
        column = python_game.splitColumn(placementInput)
        isHit = oponent.checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row,column)
        if isHit == 1:
            #hit an alredy hitted field
            print("Bitte waelen sie ein Feld auf dass sie noch nicht geschossen haben!")
        elif isHit == 2:
            #hit a ship
            print("Sie haben getroffen, bitte schießen sie ernuet!")
        else:
            print("Das war leider ein Wassertreffer!")
    #TODO look how that is working
    main.nextPlayer()
   
               
                    

