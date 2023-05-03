import os
import random
from termcolor import colored
from colorama import init
import shipinitializer
import converterfunctions
import pythonGame
import outputmanager

cpuMemory = 0

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
    if gameMode ==  1:
        if currentPlayer == 1:
            shootingIq = outputmanager.user1.getShootingIq()
            match cpuManager1(data, gameMode, currentPlayer, shootingIq, pythonGame.leakedBoard2, pythonGame.hiddenBoard1):
                case 11:
                    return 1
                case None:
                    return 1
                case _:
                    nextPlayer(data, gameMode, 1)
          
        elif currentPlayer == 2:
            match playermanager(data ,outputmanager.user2, pythonGame.leakedBoard1, pythonGame.hiddenBoard2, shipinitializer.opponentShips) : #has to change with number of ships
                case "won":
                    return 2 #is the winningID which should be returned to the main.
                case None:
                    return 2
                case _:
                    nextPlayer(data, gameMode, 2)

        else:
            print("Shit")
    elif gameMode == 2:
        match currentPlayer:
            case 1:
                if playermanager(data, outputmanager.user1, pythonGame.leakedBoard2, pythonGame.hiddenBoard1, shipinitializer.opponentShips) == "won": #has to change with number of ships
                    winningId = 1
                    return winningId #is the winningID which should be returned to the main
                else:
                        nextPlayer(data, gameMode, 1)
            case 2:
                if playermanager(data, outputmanager.user2, pythonGame.leakedBoard1, pythonGame.hiddenBoard2, shipinitializer.playerShips) == "won": #has to change with number of ships
                    winningId = 2
                    return winningId #is the winningID which should be returned to the main.
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
                for ship in shipList:
                    name = ship.getName()
                    print(name)
                    positions = ship.getPosition()
                    positionMemory = ship.getPositionMemory()
                    if shootingTupel in positions:
                        print(colored("Das war ein Treffer! Weiter so!",'green'))
                        hiddenBoard[row][column] = 3
                        leakedBoard[row][column] = 3
                        positionMemory.append(shootingTupel)
                        ship.setPositionMemory(positionMemory)
                        positions.remove(shootingTupel)
                        if len(positions) == 0:
                            currentPlayer.increaseLeftShips()
                            positionMemory = ship.getPositionMemory()
                            for tupel in positionMemory:
                                row, column = tupel
                                hiddenBoard[row][column] = 4
                                # two times the same row?
                                #hiddenBoard[row][column] = 4
                            print(colored("\nSchiff versenkt\n",'green',attrs=["blink"]))
                            print(currentPlayer.getLeftShips())
                            if currentPlayer.getLeftShips() == 1:
                                shootingRepeater = False
                                pythonGame.printhiddenBoard(hiddenBoard)
                                return "won"
                        else:
                            pass
                    else:
                        pass
                print("Sie erhalten einen weiteren Schuss\n")
                shootingRepeater = True
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
            for ship in shipinitializer.playerShips:
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
                        positionMemory = ship.getPositionMemory()
                        for tupel in positionMemory:
                            row, column = tupel
                            hiddenBoard[row][column] = 4
                        shootingIq = 0
                        outputmanager.user1.setShootingIq(shootingIq)
                        print(colored("Der Computer hat ein Schiff versenkt",'red'))
                        outputmanager.user1.increaseLeftShips()
                        if outputmanager.user1.getLeftShips() == 1:
                            allHit = 11 #11 is the number which determines that the cpu won (for the winning ID)
                            return allHit
                        else:
                            pass
                    else:
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



def cpuManager1(data, gameMode, currentPlayer, shootingIq, leakedBoard, hiddenBoard):
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
                            nextPlayer(data, gameMode, currentPlayer)
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
                                        nextPlayer(data, gameMode, currentPlayer)
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
                                        pythonGame.printhiddenBoard(hiddenBoard)
                                        continue
                                    case 11: #the cpu killed the last ship
                                        allHit = 11
                                        return allHit

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
                            nextPlayer(data, gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 2
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                        case 11: #the cpu killed the last ship
                            allHit = 11
                            return allHit
                        case _:
                            print("something went wrong")
                    continue

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
                            nextPlayer(data, gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 3
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                        case 11: #the cpu killed the last ship
                            allHit = 11
                            return allHit
                        case _:
                            print("something went wrong")

                    continue

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
                            nextPlayer(data, gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 4
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                        case 11: #the cpu killed the last ship
                            allHit = 11
                            return allHit
                        case _:
                            print("something went wrong")

                    continue

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
                            nextPlayer(data, gameMode, currentPlayer)
                            break
                        case 1:
                            shootingIq = 5
                            outputmanager.user1.setShootingIq(shootingIq)
                            pythonGame.printhiddenBoard(hiddenBoard)
                        case 11: #the cpu killed the last ship
                            allHit = 11
                            return allHit
                        case _:
                            print("something went wrong")

                    continue
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
        continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user2.getName()}  \n")
        
        
    elif currentPlayer == 2:
        currentPlayer = 1
        data["currentPlayer"] = currentPlayer
        print("__________________________________\n")
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
        continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user1.getName()}  \n")
    else:
        print("Irgendwas ist hier schief gelaufen!")

    clearConsole()
    shooting(data, gameMode, currentPlayer)
