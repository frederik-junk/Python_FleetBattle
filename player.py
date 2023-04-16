import python_game
import main

class Player:
    def __init__(self,name):
        self.__name = name
"""
#TODO delete comment when ships are implemented differently
#TODO import shipmanager if want to use again
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
def playerAction(currentPlayer):
    isHit = 1
    while(isHit != 0):
        #input hitting field
        #TODO check if input is valid
        hittingInput = input("Bitte geben sie an auf welches Feld schießen wollen")
        #split row and column
        row = converterFunctions.splitRow(placementInput)
        column = converterFunctions.splitColumn(placementInput)
        #choose on which board to shoot
        if currentPlayer == 2:
            isHit = python_game.checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row,column)
        elif currentPlayer == 1:
            isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column)

        if isHit == 1:
            #hit an alredy hitted field
            print("Bitte waelen sie ein Feld auf dass sie noch nicht geschossen haben!")
            playerAction(currentPlayer)
        elif isHit == 2:
            #hit a ship
            print("Sie haben getroffen, bitte schießen sie ernuet!")
        elif isHit == 3:
            print("Sie haben das Schiff versenkt! \nSie duerfen nich einmal schießen")
        else:
            print("Das war leider ein Wassertreffer!")
    #switch to player/computer 
    main.nextPlayer()
   
               
                    

