import python_game
import main

class Player:
    def __init__(self,name):
        self.__name = name

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
            isHit = hitShip.checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,column,row)
        elif currentPlayer == 1:
            isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row)

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
   
               
                    

