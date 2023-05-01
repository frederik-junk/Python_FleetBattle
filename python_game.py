import random
import converterfunctions
import os
import main
from termcolor import colored
from colorama import init
init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#letterrow to show user the name of each column
letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]# Erstellen des Spielfelds

def initializeBoard(board):
        for i in range(10):
            row = []
            for j in range(10):
                row.append(0)
            board.append(row)

def boardmaster():

    #creating board with leaked ships for player 1 ship placing
    leakedBoard1 = []
    initializeBoard(leakedBoard1)

    #creating board with leaked ships for player 2 ship placing
    leakedBoard2 = []
    initializeBoard(leakedBoard2)

    #creating board with hidden ships from player 1 for game of player 2
    hiddenBoard1 = []
    initializeBoard(hiddenBoard1)

    #creating board with hidden ships from player 2 for game of player 1
    hiddenBoard2 = []
    initializeBoard(hiddenBoard2)

    boardtupel = (leakedBoard1, leakedBoard2, hiddenBoard1, hiddenBoard2)

    return boardtupel


leakedBoard1, leakedBoard2, hiddenBoard1, hiddenBoard2 = boardmaster()


#function to print the board with leaked ships (used to show player at beginning his placed ships)
def printleakedBoard(board):
    #creates the first row with letters to locate the ship positon (horizontal)
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        #creates the first column with letters to locate the ship positon (vertical)
        print(str(i+1).zfill(2), end="  ") #zfill to format number  (0digit)
        #replace function to optical replace 1 = ship position, 0 = free space (water), 6 = placement blocker for following player ships
        print("  ".join(str(elem).replace("1","#").replace("0","~").replace("6","X") for elem in row))
#function tp print the board without showing the ships (used for the game itself to hide ship postions to the opponent)
def printhiddenBoard(board):
    #creates the first row with letters to locate the ship positon (horizontal)
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        #creates the first column with letters to locate the ship positon (vertical)
        print(str(i+1).zfill(2), end="  ") #zfill to format number  (0digit)
        #replace function to optical replace  1 = ship filed but hidden (shown as water), 2 = free space (water), 2 = shotted spot without hit, 3 = shotted spot with hit, 4 = eleminated ship (complet)
        print("  ".join(str(elem).replace("1","~").replace("0","~").replace("2","O").replace("3","x").replace("4","#") for elem in row))
         
#function to place a ship in the right position with the right length and the right direction
def placeShip(board, shipLength, ship, shipName, counter):
    if counter == 1:
        printleakedBoard(board)
    while True:
        placementInput = input(f"Geben Sie eine Koordinate an, auf die die Spitze Ihres {counter}. Schiffs ({shipName}) platziert werden soll. Dieses hat die Laenge {shipLength}.\n")

        try: 
            startingColumnChar = converterfunctions.splitColumnConverter(placementInput)
            if startingColumnChar == 11:  #eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
            startingRowNumber = converterfunctions.splitRow(placementInput)  
            if startingRowNumber == 11: #eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
                   
        except Exception:
            print(colored("Ihre Eingabe enthaelt Fehler.\n Bitte geben Sie Buchstaben zwischen A und J ein.\n Bitte geben Sie eine Zahl zwischen 1 und 10 ein.",'red'))
            print("Bitte geben Sie neue Anfangskoordinaten ein (z.B.: A3).")
            continue     
                        
        #subtract one for the correct alignment
        startingRowNumber = int(startingRowNumber)
        startingColumnChar = int(startingColumnChar)
        if board[startingRowNumber][startingColumnChar] == 1:
            print(colored(f"Sie können an dieser Stelle {placementInput} kein Schiff platzieren, da dort schon ein Schiff liegt.",'red'))
            continue
        elif board[startingRowNumber][startingColumnChar] == 6:
            print(colored(f"Sie können hier {placementInput} kein Schiff platzieren, da es zu nah an einem anderen Schiff liegt.",'red'))
            continue 
        else:
            print(colored(f"Die Spitze des Schiffes liegt auf {placementInput}",'cyan'))
            #placing the ship in the right direction
            #TODO give ship to this function
            if shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship) == True:
                continue
            else:
                break

    #printleakedBoard(board)


    #DELETE if Positions for ships are available 
    #placing the ship in the right direction
    #shipDirection(board, shipLength, startingRowNumber, startingColumnChar)

def shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship):
    gameMode = 2 
    directionInput = input("Geben Sie über die Tasten [w][a][s][d] die Ausrichtung des Schiffes an.\n")
    if converterfunctions.directionConverter(board, shipLength, startingRowNumber, startingColumnChar, directionInput, gameMode, ship) == True:
        return True #is send back to set another coordinate
    else:
        clear_console()
        print(colored("Ihr Schiff wurde platziert!",'green')) #TODO insert Name of ship Type here 
        printleakedBoard(board)
        return False

def cpuShipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship):
    gameMode = 1
    #get a random direction for the ship to be placed in
    while True:
        cpuDirection = random.randint(0,3)
        match cpuDirection:
            case 0: cpuDirection = "w"
            case 1: cpuDirection = "a"
            case 2: cpuDirection = "s"
            case 3: cpuDirection = "d"
            case _: print("oh something went wrong") #eventuelle Schleife neue Zahl generieren 

        possiblePositions = converterfunctions.directionConverter(board, shipLength, startingRowNumber, startingColumnChar, cpuDirection, gameMode, ship)
        if possiblePositions == True:
            return 11
        else:
            break

#function to add the blockers so that ships cant be placed next to the ship

#function for the cpu opponent to place the a ship
def cpuPlaceShip(board, shipLength, ship):
    while True:
        startingRowNumber = random.randint(0, 9)
        startingColoumnChar = random.randint(0, 9)

        #cpu places the ship with the random startig coordinates
        if cpuShipDirection(board, shipLength, startingRowNumber, startingColoumnChar, ship) == 11:
            continue
        else:
            printleakedBoard(board)
            break

    


