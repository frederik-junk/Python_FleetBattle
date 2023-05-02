import os
import circularImportFixing
import converterfunctions
import pythonGame
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

def shooting(data, gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    #used for CPU
    """Function to process shots of the user 

    Args:
        data (_type_): _description_
        gameMode (int): The game mode to indicate if there's another human player or the CPU
        currentPlayer (int): The current player to keep track on which boards should be printed etc.

    Returns:
        winningID(int): An int value to indicate which player won the game
    """
    cpuMemory = (1,1)
    positionMemory = []
    shootingRepeater = True
    if gameMode ==  1:
        if currentPlayer == 1:
            shootingIq = outputmanager.user1.getShootingIq()
            if cpuManager1(data, gameMode, currentPlayer, shootingIq) == 11:
                return 1
            nextPlayer(data, gameMode, currentPlayer, data)
        elif currentPlayer == 2:
            if playermanager(data ,outputmanager.user2.getName(), pythonGame.leakedBoard1, pythonGame.hiddenBoard2, circularImportFixing.playerShips, currentPlayer) == 2:
                return 2 #is the winningID which should be returned to the main.
            else:
                nextPlayer(data, gameMode, 2)

        else:
            print("Shit")
    elif gameMode == 2:
            match currentPlayer:
                case 1:
                    if playermanager(data, outputmanager.user1, pythonGame.leakedBoard2, pythonGame.hiddenBoard1, circularImportFixing.opponentShips) == 1:
                         return 1 #is the winningID which should be returned to the main.
                    else:
                        nextPlayer(data, gameMode, 1)
                case 2:
                    if playermanager(data, outputmanager.user2, pythonGame.leakedBoard1, pythonGame.hiddenBoard2, circularImportFixing.playerShips) == 2:
                         return 2 #is the winningID which should be returned to the main.
                    else:
                        nextPlayer(data, gameMode, 2)
                case _: 
                    print("something went wrong")
    else:
        print("Shit")

def playermanager(data, currentPlayer, leakedBoard, hiddenBoard, shipList):
    shootingRepeater = True
    pythonGame.printhiddenBoard(hiddenBoard)
    while shootingRepeater == True:
        shootingPosition = input(f"{currentPlayer.getName()} geben Sie eine Koordinate an, auf die sie schießen wollen: \n")
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
        clearConsole()
        print(colored(f"Volle Feuerkraft auf {shootingPosition}!",'cyan'))
        match leakedBoard[row][column]:
            case 1:
                shootingTupel = (row, column)
                shootingList = [row, column]
                for ship in shipList:
                    name = ship.getName()
                    print(name)
                    positions = ship.getPosition()
                    positionMemory = ship.getPositionMemory()
                    print(shootingTupel)
                    print(positions)
                    if shootingTupel in positions:
                        print(shootingTupel)
                        print(positions)
                        print(colored("Das war ein Treffer! Weiter so!",'green'))
                        hiddenBoard[row][column] = 3
                        leakedBoard[row][column] = 3
                        positionMemory.append(shootingTupel)
                        ship.setPositionMemory(positionMemory)
                        positions.remove(shootingTupel)
                        if len(positions) == 0:
                            currentPlayer.decreaseLeftShips()
                            positionMemory = ship.getPositionMemory()
                            for tupel in positionMemory:
                                row, column = tupel
                                hiddenBoard[row][column] = 4
                                # two times the same row?
                                #hiddenBoard[row][column] = 4
                            print(colored("\nSchiff versenkt\n",'green',attrs=["blink"]))
                            if currentPlayer.getLeftShips() == 0:
                                pythonGame.printhiddenBoard(hiddenBoard)
                                winningID = 2
                                return winningID
                            else:
                                pass
                        pythonGame.printhiddenBoard
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
                print("Blubb blubb Schuss verweigert, denn hier herrscht Totenstille, Sie hatten dieses Feld bereits beschossen!\nDas Schiff an dieser Stelle ist bereits versenkt, lassen wir den Toten besser ihre verdiente Ruhe.\n")
                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                shootingRepeater = False
            case 0:
                print(colored("Das war leider ein Wassertreffer", 'cyan'))
                hiddenBoard[row][column] = 2 
                leakedBoard[row][column] = 2
                pythonGame.printhiddenBoard
                shootingRepeater = False
            case 6:
                print(colored("Das war leider ein Wassertreffer", 'cyan'))
                hiddenBoard[row][column] = 2 
                leakedBoard[row][column] = 2
                pythonGame.printhiddenBoard
                shootingRepeater = False
            case _:
                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
        pythonGame.printhiddenBoard(hiddenBoard)






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
    shooting(gameMode, currentPlayer, data)







def randomDirection():
    direction = random.randint(0,3)
    return direction


def checkHit(hiddenBoard, leakedBoard, cpuMemory):
    row, column = cpuMemory
    match leakedBoard[row][column]:
        case 0:
            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
            hiddenBoard[row][column] = 2
            return leakedBoard[row][column]

        case 6:
            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
            hiddenBoard[row][column] = 2
            leakedBoard[row][column] = 0
            return leakedBoard[row][column]
        
        case 1:
            shootingTupel = cpuMemory
            for ship in circularImportFixing.playerShips:
                    positionMemory = ship.getPositionMemory()
                    postitions = ship.getPosition()
                    if shootingTupel in postitions:
                        print(colored("Der Computer hat eines Ihrer Schiffe getroffen",'red'))
                        hiddenBoard[row][column] = 3
                        positionMemory.append(shootingTupel)
                        ship.setPositionMemory(positionMemory)
                        postitions.remove(shootingTupel)
                        #ship is sunk
                        if len(postitions) == 0:
                            print(colored("Der Computer hat ein Schiff versenkt",'red'))
                            circularImportFixing.playerShips.remove(ship)
                            positionMemory = ship.getPositionMemory()
                            for tupel in positionMemory:
                                row, column = tupel
                                hiddenBoard[row][column] = 4
                            shootingIq = 0
                            outputmanager.user1.setShootingIq(shootingIq)
                        else:
                            pass
                        if len(circularImportFixing.playerShips) == 0:
                            return 11 #11 is the number which determines that the cpu won (for the winning ID)
            return leakedBoard[row][column]
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



def cpuManager1(gameMode, currentPlayer, shootingIq, data):
    leakedBoard = pythonGame.leakedBoard2
    hiddenBoard = pythonGame.hiddenBoard1
    global cpuMemory

    direction = outputmanager.user1.getDirection()
    cpuMemory = outputmanager.user1.getCpuMemory()
    while True:
        match shootingIq:
            case 0:
                #unecessary if already replaced elsewhere
                row, column = cpuMemory
                if leakedBoard[row][column] == 6:
                    leakedBoard[row][column] = 0
                firstShootingPosition = firstPosition(hiddenBoard)
                outputmanager.user1.setFirstCpuMemory(firstShootingPosition)

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
                            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                            hiddenBoard[row][column] = 2
                            shootingIq = 0
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            nextPlayer(gameMode, currentPlayer, data)
                            break
                        case 1: #if the random shot is a hit -> get a random direction
                            shootingIq = 1
                            outputmanager.user1.setShootingIq(shootingIq)
                            direction = randomDirection()
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
                            pythonGame.printhiddenBoard(hiddenBoard)
                            cpuMemory = (row, column)
                            outputmanager.user1.setCpuMemory(cpuMemory)
                            while True:
                                match checkHit(hiddenBoard, leakedBoard, cpuMemory):
                                    case 0: #the first shot in the new direction is a non-hit -> shootingIq = 2 (go opposite direction)
                                        print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                                        hiddenBoard[row][column] = 2
                                        shootingIq = 2
                                        outputmanager.user1.setShootingIq(shootingIq) 
                                        pythonGame.printhiddenBoard(hiddenBoard)  
                                        nextPlayer(gameMode, currentPlayer, data)
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
                                    case 11: #the cpu killed the last ship
                                        return 11
                                cpuMemory = (row, column)
                                outputmanager.user1.setCpuMemory(cpuMemory)
                                pythonGame.printhiddenBoard(hiddenBoard)
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
                            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                            hiddenBoard[row][column] = 2
                            shootingIq = 3
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            nextPlayer(gameMode, currentPlayer, data)
                            break
                        case 1:
                            shootingIq = 2
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            continue
                        case 11: #the cpu killed the last ship
                            return 11
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
                            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                            hiddenBoard[row][column] = 2
                            shootingIq = 4
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            nextPlayer(gameMode, currentPlayer, data)
                            break
                        case 1:
                            shootingIq = 3
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            continue
                        case 11: #the cpu killed the last ship
                            return 11
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
                            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                            hiddenBoard[row][column] = 2
                            shootingIq = 5
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            nextPlayer(gameMode, currentPlayer, data)
                            break
                        case 1:
                            shootingIq = 4
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            continue
                        case 11: #the cpu killed the last ship
                            return 11
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
                            print(colored("Der Computer erzielt einen Wassertreffer",'cyan'))
                            hiddenBoard[row][column] = 2
                            shootingIq = 0
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            nextPlayer(gameMode, currentPlayer, data)
                            break
                        case 1:
                            shootingIq = 5
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                            continue
                        case 11: #the cpu killed the last ship
                            return 11
                        case _:
                            print("something went wrong")
            case _:
                print("something went wrong")         
                    






            
                





# Switches the current player after each action

def nextPlayer(data, gameMode, currentPlayer):

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
    shooting(data, gameMode, currentPlayer)
