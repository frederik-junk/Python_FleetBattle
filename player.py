import python_game
import main
import converterfunctions
import hitShip
import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self,name):
        self.__name = name

def playerAction(currentPlayer, gameMode):
    isHit = 1
    while isHit != 0:
        #input hitting field
        #TODO check if input is valid
        while True:
            try:
                hittingInput = input("Bitte geben Sie an auf welches Feld Sie schießen wollen: \n")
                #split row and column
                row = converterfunctions.splitRow(hittingInput)
                column = converterfunctions.splitColumnConverter(hittingInput)
                if row == 11:
                    raise Exception("wrong Input")
                elif column == 11:
                    raise Exception("wrong Input") 
                else:
                    break
            except Exception:
                print("Ihre Angabe ist fehlerhaft.\n Bitte geben Sie Buchstaben zwischen A und J ein.\n Bitte geben Sie eine Zahl zwischen 1 und 10 ein.")
                print("Bitte geben Sie die Schießposition in der Form (z.B.: A3) an.")
                continue
            
        #choose on which board to shoot

        if currentPlayer == 2:
            isHit = hitShip.checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,column,row, gameMode)
            python_game.printhiddenBoard(python_game.hiddenBoard1)
        elif currentPlayer == 1:
            isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row, gameMode)
            python_game.printhiddenBoard(python_game.hiddenBoard2)

        if isHit == 1:
            #hit an alredy hitted field
            print("Bitte waehlen sie ein Feld auf dass Sie noch nicht geschossen haben!")
            playerAction(currentPlayer,gameMode)
        elif isHit == 2:
            #hit a ship
            print("Treffer! Bitte wählen Sie ein neues Zielfeld.")
            continueRequest = input("Beliebige Taste und Enter drücken um fortzufahren: \n")
            #clearConsole()
        elif isHit == 3:
            print("Schiff versenkt! \nBitte wählen Sie ein neues Zielfeld.")
            continueRequest = input("Beliebige Taste und Enter drücken um fortzufahren: \n")
            #clearConsole()
        else:
            print("Das war leider ein Wassertreffer!")
            continueRequest = input("Beliebige Taste und Enter drücken um fortzufahren: \n")
            #clearConsole()
    #switch to player/computer
    main.nextPlayer()
