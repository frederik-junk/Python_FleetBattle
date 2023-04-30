import os
import circularImportFixing
import converterfunctions
import python_game
import outputmanager
import random
import json
from termcolor import colored
from colorama import init
init()

directionLock = 0
hitStatus = 0
i = 0
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def shooting(gameMode, currentPlayer, data):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    #used for CPU
    cpuMemory = (1,1)
    positionMemory = []
    shootingRepeater = True
    if gameMode ==  1:
        if currentPlayer == 1:
            shootingIq = outputmanager.user1.getShootingIq()
            cpuManager1(gameMode,currentPlayer, shootingIq)
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
                        nextPlayer(gameMode, 1, data)
                case 2:
                    if playermanager(outputmanager.user2.getName(), python_game.leakedBoard1, python_game.hiddenBoard2, circularImportFixing.playerShips) == 2:
                         return 2 #is the winningID which should be returned to the main.
                    else:
                        nextPlayer(gameMode, 2, data)
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
                    positions = ship.getPosition()
                    positionMemory = ship.getPositionMemory()
                    if shootingTupel in positions:
                        print(colored("Das war ein Treffer! Weiter so!",'green'))
                        hiddenBoard[row][column] = 3
                        leakedBoard[row][column] = 3
                        positionMemory.append(shootingTupel)
                        ship.setPositionMemory(positionMemory)
                        positions.remove(shootingTupel)
                        #ship.setPositions(positions)
                        if len(positions) == 0:
                            shipList.remove(ship)
                            positionMemory = ship.getPositionMemory()
                            for tupel in positionMemory:
                                row, column = tupel
                                hiddenBoard[row][column] = 4
                                # two times the same row?
                                #hiddenBoard[row][column] = 4
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


def cpuManager(gameMode,currentPlayer, hitStatus):
            global directionLock
            global i
            global cpuMemory
            leakedBoard = python_game.leakedBoard2
            hiddenBoard = python_game.hiddenBoard1
            #counterVariable for shooting
            
            #ship wasnt hit before
            if hitStatus == 0:
                row = random.randint(0,9)
                column = random.randint(0,9)
                #searching for an unshoot field
                while hiddenBoard[row][column] != 0:
                    row = random.randint(0,9)
                    column = random.randint(0,9)
                shootingTupel = (row, column)
                cpuMemory = shootingTupel
            #continue hitting ship till its sunk
            elif hitStatus == 1:
                #saved hitted field
                shootingTupel = cpuMemory
                row, column = shootingTupel
                #direction of ship unknown
                if directionLock == 0:
                    direction = random.randint(1,4)
                else:
                    direction = directionLock
                match direction:
                    case 1: row = row-i
                    case 2: column = column -i
                    case 3: row = row + i
                    case 4: column = column + i
            #unecessary if already replaced elsewhere
            if leakedBoard[row][column] == 6:
                leakedBoard[row][column] = 0
            
            #print(leakedBoard[row][column])
            match leakedBoard[row][column]:
                
                #hit water
                case 0:
                    i = 0         
                    print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                    hiddenBoard[row][column] = 2
                    python_game.printhiddenBoard(hiddenBoard)
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
                        shootingTupel = cpuMemory
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
                                    python_game.printhiddenBoard(hiddenBoard)
                                else:
                                    pass
                        
                        i = i+1
                        print("Der Computer schießt erneut")
                        cpuManager(gameMode, currentPlayer, hitStatus)
                case _:
                    print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
            python_game.printhiddenBoard(hiddenBoard)
            nextPlayer(gameMode, currentPlayer)




# Switches the current player after each action
def nextPlayer(gameMode, currentPlayer, data):

    if currentPlayer == 1:
        currentPlayer = 2
        data["currentPlayer"] = currentPlayer
        print("__________________________________\n")
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
        
        
    elif currentPlayer == 2:
        currentPlayer = 1
        data["currentPlayer"] = currentPlayer
        print("__________________________________\n")
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
    else:
        print("Irgendwas ist hier schief gelaufen!")
    continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user1.getName()}  \n")
    clearConsole()
    shooting(gameMode, currentPlayer)







def direction():
    direction = random.randint(1,4)
    return direction


def checkHit(hiddenBoard, leakedBoard, cpuMemory):
    row, column = cpuMemory
    match leakedBoard[row][column]:
        case 0:
            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
            hiddenBoard[row][column] = 2
            shootingIq = 0
            return shootingIq

        case 1:
            [row][column] = 1 
            shootingIq = 1


            shootingTupel = cpuMemory
            for ship in circularImportFixing.opponentShips:
                    postitions = ship.getPosition()
                    if shootingTupel in postitions:
                        print(colored("Der Computer hat eines Ihrer Schiffe getroffen",'red'))
                        hiddenBoard[row][column] = 3
                        postitions.remove(shootingTupel)
                        #ship is sunk
                        if len(postitions) == 0:
                            print(colored("Der Computer hat ein Schiff versenkt",'red'))
                            circularImportFixing.opponentShips.remove(ship)
                            shootingIq = 0
                        else:
                            pass
            return shootingIq
        case _:
            print("something went terribly wrong")



def firstPosition(board):
    while True: #get correct shooting coordinates on which he didnt shot
                    row = random.randint(0,9)
                    column = random.randint(0,9)
                    if board[row][column] == 0:
                        shootingTuple = (row, column)
                        firstCpuMemory = shootingTuple
                        break
                    else:
                        continue
    return firstCpuMemory



def cpuManager1(gameMode, currentPlayer, shootingIq):
    leakedBoard = python_game.leakedBoard2
    hiddenBoard = python_game.hiddenBoard1
    global cpuMemory
    global direction

    direction = outputmanager.user1.getDirection()
    cpuMemory = outputmanager.user1.getCpuMemory()

    while True:
        match shootingIq:
            case 0:
                firstShootingPosition = firstPosition(hiddenBoard)
                outputmanager.user1.setFirstCpuMemory(firstShootingPosition)
                #unecessary if already replaced elsewhere
                if leakedBoard[row][column] == 6:
                    leakedBoard[row][column] = 0

                shootingIq = 1
                outputmanager.user1.setShootingIq(shootingIq)
                continue

     
            case 1:
                cpuMemory = outputmanager.user1.getFirstCpuMemory()
                row, column = cpuMemory
                while True:
                    #check if it is a hit
                    match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                        case 0: #if the random shot is a non-hit -> still shootingIq = 0
                            shootingIq = 0
                            outputmanager.user1.setShootingIq(shootingIq)
                            nextPlayer(gameMode, currentPlayer)
                            break
                        case 1: #if the random shot is a hit -> get a random direction
                            shootingIq = 1
                            outputmanager.user1.setShootingIq(shootingIq)
                            direction = direction()
                            outputmanager.user1.setDirection(direction)
                            match direction:
                                case 0:
                                    row = row + 1
                                case 1:
                                    column = column - 1
                                case 2:
                                    column = column + 1
                                case 3:
                                    row = row - 1
                                case _:
                                    print("something went wrong")
                            outputmanager.user1.setDirection(direction)

                            cpuMemory = (row, column)
                            outputmanager.user1.setCpuMemory(cpuMemory)
                            while True:
                                match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                                    case 0: #the first shot in the new direction is a non-hit -> shootingIq = 2 (go opposite direction)
                                        shootingIq = 2
                                        outputmanager.user1.setShootingIq(shootingIq)   
                                        nextPlayer(gameMode, currentPlayer)
                                        break

                                    case 1: #the first shot in the new direction is a hit -> shootingIq = 1 until the first non-hit
                                        shootingIq = 1
                                        outputmanager.user1.setShootingIq(shootingIq)
                                        match direction:
                                            case 0:
                                                row = row + 1
                                            case 1:
                                                column = column - 1
                                            case 2:
                                                column = column + 1
                                            case 3:
                                                row = row - 1
                                            case _:
                                                print("something went wrong")
                                cpuMemory = (row, column)
                                outputmanager.user1.setCpuMemory(cpuMemory)
                                continue
                        case _:
                            print("something went wrong")
                    break

            case 2:
                cpuMemory = outputmanager.user1.getFirstCpuMemory()
                row, column = cpuMemory
                while True:
                    match direction:
                        case 0:
                            row = row - 1
                        case 1:
                            column = column + 1
                        case 2:
                            column = column - 1
                        case 3:
                            row = row + 1
                        case _:
                            print("something went wrong")
                    cpuMemory = (row, column)
                    outputmanager.user1.setCpuMemory(cpuMemory)

                    match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                        case 0: 
                            shootingIq = 3
                            outputmanager.user1.setShootingIq(shootingIq)
                            nextPlayer(gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 2
                            outputmanager.user1.setShootingIq(shootingIq)
                            continue
                        case _:
                            print("something went wrong")

            case 3:
                cpuMemory = outputmanager.user1.getFirstCpuMemory()
                row, column = cpuMemory 
                while True:
                    match direction:
                        case 0:
                            column = column + 1
                        case 1:
                            row = row + 1
                        case 2:
                            row = row - 1
                        case 3:
                            column = column - 1
                        case _:
                            print("something went wrong")
                    cpuMemory = (row, column)
                    outputmanager.user1.setCpuMemory(cpuMemory)

                    match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                        case 0: 
                            shootingIq = 4
                            outputmanager.user1.setShootingIq(shootingIq)
                            nextPlayer(gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 3
                            outputmanager.user1.setShootingIq(shootingIq)
                            continue
                        case _:
                            print("something went wrong")

            case 4:
                cpuMemory = outputmanager.user1.getFirstCpuMemory()
                row, column = cpuMemory
                while True:
                    match direction:
                        case 0:
                            column = column - 1
                        case 1:
                            row = row - 1
                        case 2:
                            row = row + 1
                        case 3:
                            column = column + 1
                        case _:
                            print("something went wrong")
                    cpuMemory = (row, column)
                    outputmanager.user1.setCpuMemory(cpuMemory)

                    match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                        case 0: 
                            shootingIq = 5
                            outputmanager.user1.setShootingIq(shootingIq)
                            nextPlayer(gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 4
                            outputmanager.user1.setShootingIq(shootingIq)
                            continue
                        case _:
                            print("something went wrong")

            case 5:
                cpuMemory = outputmanager.user1.getFirstCpuMemory()
                row, column = cpuMemory
                while True:
                    match direction:
                        case 0:
                            column = column + 1
                        case 1:
                            row = row + 1
                        case 2:
                            row = row - 1
                        case 3:
                            column = column - 1
                        case _:
                            print("something went wrong")
                    cpuMemory = (row, column)
                    outputmanager.user1.setCpuMemory(cpuMemory)

                    match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                        case 0: 
                            shootingIq = 0
                            outputmanager.user1.setShootingIq(shootingIq)
                            nextPlayer(gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 5
                            outputmanager.user1.setShootingIq(shootingIq)
                            continue
                        case _:
                            print("something went wrong")
            case _:
                print("something went wrong")         
                    





