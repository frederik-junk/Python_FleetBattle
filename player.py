import python_game
import main

class Player:
    def __init__(self,name):
        self.__name = name

def playerAction(currentPlayer):
    isHit = 1
    while isHit != 0:
        #input hitting field
        #TODO check if input is valid
        hittingInput = input("Bitte geben Sie an auf welches Feld Sie schießen wollen")
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
            print("Dieses Feld haben Sie bereits beschossen. Bitte wählen Sie ein anderes!")
            playerAction(currentPlayer)
        elif isHit == 2:
            #hit a ship
            print("Treffer! Bitte wählen Sie ein neues Zielfeld.")
        elif isHit == 3:
            print("Schiff versenkt! \nBitte wählen Sie ein neues Zielfeld.")
        else:
            print("Das war leider ein Wassertreffer!")
    #switch to player/computer
    main.nextPlayer()
