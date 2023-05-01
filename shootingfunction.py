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
            hitStatus = 0
            cpuManager(data, gameMode,currentPlayer, hitStatus)
            nextPlayer(data, gameMode,currentPlayer)
        elif currentPlayer == 2:
            if playermanager(outputmanager.user2.getName(), pythonGame.leakedBoard1, pythonGame.hiddenBoard2, circularImportFixing.playerShips) == 2:
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
                            outputmanager.decreaseLeftShips(currentPlayer)
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
                print("Das war leider ein Wassertreffer")
                hiddenBoard[row][column] = 2 
                leakedBoard[row][column] = 2
                pythonGame.printhiddenBoard
                shootingRepeater = False
            case 6:
                print("Das war leider ein Wassertreffer")
                hiddenBoard[row][column] = 2 
                leakedBoard[row][column] = 2
                pythonGame.printhiddenBoard
                shootingRepeater = False
            case _:
                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
        pythonGame.printhiddenBoard(hiddenBoard)


def cpuManager(data, gameMode, currentPlayer, hitStatus):
            global directionLock
            global i
            global cpuMemory
            leakedBoard = pythonGame.leakedBoard2
            hiddenBoard = pythonGame.hiddenBoard1
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
                    pythonGame.printhiddenBoard(hiddenBoard)
                    #change direction if known, but water was hit
                    if directionLock !=0:
                        match directionLock:
                            case 1: directionLock = 3
                            case 2: directionLock = 4
                            case 3: directionLock = 1
                            case 4: directionLock = 2
                        nextPlayer(data, gameMode, currentPlayer)

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
                                    pythonGame.printhiddenBoard(hiddenBoard)
                                else:
                                    pass
                        
                        i = i+1
                        print("Der Computer schießt erneut")
                        cpuManager(gameMode, currentPlayer, hitStatus)
                case _:
                    print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
            pythonGame.printhiddenBoard(hiddenBoard)
            nextPlayer(data, gameMode, currentPlayer)





def cpuManager1(currentPlayer, shootingIq):
    leakedBoard = pythonGame.leakedBoard2
    hiddenBoard = pythonGame.hiddenBoard1
    global cpuMemory
    match shootingIq:
        case 0:
            while True: #get correct shooting coordinates on which he didnt shot
                row = random.randint(0,9)
                column = random.randint(0,9)
                if hiddenBoard[row][column] == 0:
                    shootingTuple = (row, column)
                    cpuMemory = shootingTuple
                    break
                else:
                    continue

            #check if it is a hit
            
                





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
