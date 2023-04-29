import os
import circularImportFixing
import converterfunctions
import python_game
import outputmanager
import random
from termcolor import colored
from colorama import init
init()

directionLock = 0
hitStatus = 0
i = 0
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def shooting(gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    #used for CPU
    cpuMemory = (1,1)
    positionMemory = []
    shootingRepeater = True
    if gameMode ==  1:
        if currentPlayer == 1:

            cpuManager(gameMode,currentPlayer)
            nextPlayer(gameMode,currentPlayer)
        elif currentPlayer == 2:
            if playermanager(outputmanager.user2.getName(), python_game.leakedBoard1, python_game.hiddenBoard2, circularImportFixing.playerShips) == 2:
                return 2 #is the winningID which should be returned to the main.
            else:
                nextPlayer(gameMode, 2)

        else:
            print("Shit")
    elif gameMode == 2:
            match currentPlayer:
                case 1:
                    if playermanager(outputmanager.user1.getName(), python_game.leakedBoard2, python_game.hiddenBoard1, circularImportFixing.opponentShips) == 1:
                         return 1 #is the winningID which should be returned to the main.
                    else:
                        nextPlayer(gameMode, 1)
                case 2:
                    if playermanager(outputmanager.user2.getName(), python_game.leakedBoard1, python_game.hiddenBoard2, circularImportFixing.playerShips) == 2:
                         return 2 #is the winningID which should be returned to the main.
                    else:
                        nextPlayer(gameMode, 2)
                case _: 
                    print("something went wrong")
    else:
        print("Shit")

def playermanager(currentPlayerName, leakedBoard, hiddenBoard, shipList):
    shootingRepeater = True
    while shootingRepeater == True:
        shootingPosition = input(f"{currentPlayerName} geben Sie eine Koordinate an, auf die sie schießen wollen: \n")
        try:
            row = converterfunctions.splitRow(shootingPosition)
            if row == 11:
                raise Exception("Ihre Angabe ist fehlerhaft")
            column = converterfunctions.splitColumnConverter(shootingPosition)
            if column == 11:
                raise Exception("Ihre Angabe ist fehlerhaft")
        except Exception:
            print(colored("Ihre Eingabe enthaelt Fehler.\n Bitte geben Sie Buchstaben zwischen A und J ein.\nBitte geben Sie eine Zahl zwischen 1 und 10 ein.",'red'))
            print("Bitte geben Sie die Anfangskoordinaten erneut ein (z.B.: A3).")
            continue
        print(colored(f"Volle Feuerkraft auf {shootingPosition}!",'cyan'))
        clearConsole()
        match leakedBoard[row][column]:
            case 1:
                shootingTupel = (row, column)
                for ship in shipList:
                    postitions = ship.getPosition()
                    positionMemory = ship.getPositionMemory()
                    if shootingTupel in postitions:
                        print(colored("Das war ein Treffer! Weiter so!",'green'))
                        hiddenBoard[row][column] = 3
                        leakedBoard[row][column] = 3
                        positionMemory.append(shootingTupel)
                        ship.setPositionMemory(positionMemory)
                        postitions.remove(shootingTupel)
                        if len(postitions) == 0:
                            shipList.remove(ship)
                            positionMemory = ship.getPositionMemory()
                            for tupel in positionMemory:
                                row, column = tupel
                                hiddenBoard[row][column] = 4
                                hiddenBoard[row][column] = 4
                            print(colored("\nSchiff versenkt\n",'green',attrs=["blink"]))
                            if len(shipList) == 0:
                                python_game.printhiddenBoard(hiddenBoard)
                                winningID = 2
                                return winningID
                            else:
                                pass
                        python_game.printhiddenBoard
                    else:
                        pass
                print("Sie erhalten einen weiteren Schuss\n")
                shootingRepeater = True
            #TODO case 2-4 funktionieren nicht weil sie in hiddenBoard stehen
            case 2:
                print("Sie hatten dieses Feld bereits beschossen und einen Wassertreffer erzielt!\n")
                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                shootingRepeater = False
            case 3:
                print("Sie hatten dieses Feld bereits beschossen und sogar einen Treffer erzielt!\nIhr Schuss liefert allerdings keine neue Erkenntnis!")
                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                shootingRepeater = False
            case 4:
                print("Blubb blubb Schuss verweigert, denn hier herrscht Totenstille, Sie hatten dieses Feld bereits beschossen!\nDas Schiff an dieser Stelle ist bereits versenkt, lassen wir den Toten besser ihre verdiente Ruhe.\nIhr Schuss liefert keine neue Erkenntnis!")
                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                shootingRepeater = False
            case 0:
                print("Das war leider ein Wassertreffer")
                hiddenBoard[row][column] = 2 
                leakedBoard[row][column] = 2
                python_game.printhiddenBoard
                shootingRepeater = False
            case 6:
                print("Das war leider ein Wassertreffer")
                hiddenBoard[row][column] = 2 
                leakedBoard[row][column] = 2
                python_game.printhiddenBoard
                shootingRepeater = False
            case _:
                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
        python_game.printhiddenBoard(hiddenBoard)


def cpuManager(gameMode,currentPlayer):
            global hitStatus
            global directionLock
            global i
            leakedBoard = python_game.leakedBoard2
            hiddenBoard = python_game.hiddenBoard1
            #counterVariable for shooting
            
            #ship wasnt hit before
            if hitStatus == 0:
                #retundant also could use a set start worth
                row = random.randint(0,9)
                column = random.randint(0,9)
                #searching for an unshoot field
                while leakedBoard[row][column] !=0:
                    row = random.randint(0,9)
                    column = random.randint(0,9)
                shootingTupel = (row, column)
                positionMemory.append(shootingTupel)
                
            #continue hitting ship till its sunk
            elif hitStatus == 1:
                #Richtung des Schiffes noch nicht
                if directionLock == 0:
                    direction = random.randint(1,4)
                else:
                    direction = directionLock
                match direction:
                    case 1: row = row-i
                    case 2: column = column -i
                    case 3: row = row + i
                    case 4: column = column + i
               
            print(leakedBoard[row][column])
            match leakedBoard[row][column]:
                
                #hit water
                #is there a need for using case 6 ?
                case 0:
                    i = 0         
                    print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                    hiddenBoard[row][column] = 2
                    python_game.printhiddenBoard
                    shootingRepeater = False
                    #change direction if known, but water was hit
                    if directionLock !=0:
                        match directionLock:
                            case 1: directionLock = 3
                            case 2: directionLock = 4
                            case 3: directionLock = 1
                            case 4: directionLock = 2
                        nextPlayer(gameMode, currentPlayer)

                #hit ship
                case 1:
                        #determine which ship is hit
                        hitStatus = 1
                        for ship in circularImportFixing.opponentShips:
                                postitions = ship.getPosition()
                                if shootingTupel in postitions:
                                    print(colored("Der Computer hat eines Ihrer Schiffe getroffen",'red'))
                                    hiddenBoard[row][column] = 3
                                    postitions.remove(shootingTupel)
                                    #if 2 fields in one direction are hit Lock this direction
                                    if i >=2:
                                        directionLock=direction
                                    #ship is sunk
                                    if len(postitions) == 0:
                                        print(colored("Der Computer hat ein Schiff versenkt",'red'))
                                        circularImportFixing.opponentShips.remove(ship)
                                        hitStatus = 0
                                        directionLock = 0
                                    else:
                                        pass
                                    python_game.printhiddenBoard
                                else:
                                    pass
                        
                        i = i+1
                        print("Der Computer schießt erneut")
                        shooting(gameMode, currentPlayer)
                case _:
                    print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
            python_game.printhiddenBoard(hiddenBoard)
            nextPlayer(gameMode, currentPlayer)
               


# Switches the current player after each action

def nextPlayer(gameMode, currentPlayer):

    if currentPlayer == 1:
        currentPlayer = 2
        print("__________________________________\n")
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
        continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user2.getName()}  \n")
        clearConsole()
        shooting(gameMode, currentPlayer)
        
    else:
        currentPlayer = 1
        print("__________________________________\n")
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
        continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user1.getName()}  \n")
        clearConsole()
        shooting(gameMode, currentPlayer)
