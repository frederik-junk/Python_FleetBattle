import random
import shipmanager
from converterfunctions import *

letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow =   [0,0,0,0,0,0,0,0,0,0]
secondRow =  [0,0,0,0,0,0,0,0,0,0]
thirdRow =   [0,0,0,0,0,0,0,0,0,0]
fourthRow =  [0,0,0,0,0,0,0,0,0,0]
fifthRow =   [0,0,0,0,0,0,0,0,0,0]
sixthRow =   [0,0,0,0,0,0,0,0,0,0]
seventhRow = [0,0,0,0,0,0,0,0,0,0]
eighthRow =  [0,0,0,3,0,0,0,0,0,0]
ninethRow =  [0,0,0,0,0,0,0,0,0,0]
tenthRow =   [0,0,0,0,0,0,0,0,0,0]
leakedBoard1 = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]
leakedBoard2 = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]
hiddenBoard1 = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]
hiddenBoard2 = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]

def printleakedBoard(board):
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        print(str(i+1).zfill(2), end="  ")
        print("  ".join(str(elem).replace("1","#").replace("0","~").replace("6","?") for elem in row))


def printhiddenBoard(board):
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        print(str(i+1).zfill(2), end="  ")
        print("  ".join(str(elem).replace("1","~").replace("0","~").replace("2","O").replace("3","x").replace("4","X") for elem in row))

# printleakedBoard(board)
# print(" \n")
# printhiddenBoard(board)

shipLength = int(2)


            
#function to place a ship in the right position with the right length and the right direction
def placeShip(board, shipLength, ship):
    while True:
        try:
            placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")

            startingColumnChar = splitColumnConverter(placementInput)
            startingRowNumber = splitRow(placementInput)
  
            try:
                if startingColumnChar.isalpha() == False:
                    raise ValueError
                startingColumnChar = startingColumnChar.upper()
                
                
            except ValueError as e:   #TODO: overlook this handling of exceptions
                print(str(e))
                print("Ihre Eingabe enthaelt Fehler. Bitte geben Sie erst den Buchstaben und dann die Zahl an.")
                print("Geben sie nun die Startposition erneut in der Form (z.B.: A3) an.")
                continue

            except Exception:
                print("Ihre Eingabe enthaelt Fehler. Bitte geben sie Buchstaben zwischen A und J ein.")
                print("Bitte geben sie die Startposition in der Form (z.B.: A3) an.")
                continue

            print("Der erste Buchstabe ist:", startingColumnChar)    #diese ausgabe kann entfernt werden
            print("Der Rest des Strings ist:", startingRowNumber)   #diese ausgabe kann entfernt werden

           
                   
            
            #adding one for the correct alignment still needs fixes
            startingRowNumber = int(startingRowNumber) - 1
            startingColumnChar = int(startingColumnChar) 

            if startingRowNumber < 0:
                print("Bitte geben sie eine neue Startposition an.")
                continue
            else:
                value = board[startingRowNumber][startingColumnChar] #dies kann entfernt werden

                print(f"Die Spitze des Schiffes liegt auf {placementInput}")
                #putting the 1 in the right position
                board[startingRowNumber][startingColumnChar] = 1
                #placing the ship in the right direction
                #TODO give ship to this function
                shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship)
                break
        except IndexError:
            #if the index is out of bounds
            print(f"Ihre Angabe {placementInput} liegt außerhalb des Spielfelds.")
            print("Bitte geben sie eine neue Startposition an.\n")

    printleakedBoard(board)


    #DELETE if Positions for ships are available 
    #placing the ship in the right direction
    #shipDirection(board, shipLength, startingRowNumber, startingColumnChar)
    
    # printleakedBoard(board)

schlachtschiff = shipmanager.Schlachtschiff(3)

def shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship):
    gameMode = 2
    while True: 
        directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
        if directionConverter(board, shipLength, startingRowNumber, startingColumnChar, directionInput, gameMode, ship) == True:
            continue
        else:
            print("Ihr Schiff wurde platziert!") #TODO insert Name of ship Type here 
            printleakedBoard(board)
            break

def cpuShipDirection(board, shipLength, startingRowNumber, startingColumnChar):
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

        if directionConverter(board, shipLength, startingRowNumber, startingColumnChar, cpuDirection, gameMode) == True:
            continue
        else:
            break

#function to add the blockers so that ships cant be placed next to the ship

#function for the cpu opponent to place the a ship
def cpuPlaceShip(board, shipLength):
    startingRowNumber = random.randint(0, 10)
    startingColoumnChar = random.randint(0, 10)

    #cpu places the ship with the random startig coordinates
    cpuShipDirection(board, shipLength, startingRowNumber, startingColoumnChar)
    printleakedBoard(board)

    



#hidden = ships hidden
def checkHit(hiddenBoard,leakedBoard,row,column):
    #check if field was alredy hit
    if hiddenBoard[row][column] != 0:
        return 1
    #hitted ship
    elif leakedBoard[row][column] == 1:
        #get which ship is hit
        for ship in opponentships:
            if(row,column)in ship.getPosition():
                shipName = ship
        shipName.hitOnShip()
        if shipName.getSize() == shipName.getDamageCounter():
            #ship sunk
            for position in shipName.getPosition():
                hiddenBoard[position]=4
            return 1
        #ship isnt sunk
        else:
            leakedBoard[row][column] = 3
        return 2
    #hitted water
    elif hiddenBoard[row][column] == 0:
        leakedBoard[row][column]= 2
    return 0
