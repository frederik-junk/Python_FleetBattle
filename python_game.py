import random
import converterfunctions

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




#function to print the board with leaked ships (used to show player at beginning his placed ships)
def printleakedBoard(board):
    #creates the first row with letters to locate the ship positon (horizontal)
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        #creates the first column with letters to locate the ship positon (vertical)
        print(str(i+1).zfill(2), end="  ") #zfill to format number  (0digit)
        #replace function to optical replace 1 = ship position, 0 = free space (water), 6 = placement blocker for following player ships
        print("  ".join(str(elem).replace("1","#").replace("0","~").replace("6","?") for elem in row))

#function tp print the board without showing the ships (used for the game itself to hide ship postions to the opponent)
def printhiddenBoard(board):
    #creates the first row with letters to locate the ship positon (horizontal)
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        #creates the first column with letters to locate the ship positon (vertical)
        print(str(i+1).zfill(2), end="  ") #zfill to format number  (0digit)
        #replace function to optical replace  1 = ship filed but hidden (shown as water), 2 = free space (water), 2 = shotted spot without hit, 3 = shotted spot with hit, 4 = eleminated ship (complet)
        print("  ".join(str(elem).replace("1","~").replace("0","~").replace("2","O").replace("3","x").replace("4","X") for elem in row))
         
#function to place a ship in the right position with the right length and the right direction
def placeShip(board, shipLength, ship, shipName):
    while True:
        try:
            placementInput = input(f"Geben sie eine Koordinate an, auf die die Spitze ihres {shipName} platziert werden soll. Es hab die Laenge {shipLength}.\n")

            startingColumnChar = converterfunctions.splitColumnConverter(placementInput)
            startingRowNumber = converterfunctions.splitRow(placementInput)
            if startingColumnChar == 11:  #eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
            else:
                print("Der erste Buchstabe ist:", placementInput[0])    #diese ausgabe kann entfernt werden

            if startingRowNumber == 11: #eleven is the statuscode for input is out of bounce
                raise Exception("Ihre Angabe ist fehlerhaft")
            else:
                print("Der Rest des Strings ist:", startingRowNumber)   #diese ausgabe kann entfernt werden
                
                
        except Exception as e:
            print(str(e))
            print("Ihre Eingabe enthaelt Fehler.\n Bitte geben sie Buchstaben zwischen A und J ein.\n Bitte geben sie eine Zahl zwischen 1 und 10 ein.")
            print("Bitte geben sie die Startposition in der Form (z.B.: A3) an.")
            continue     
                        
        #adding one for the correct alignment still needs fixes
        startingRowNumber = int(startingRowNumber) - 1
        startingColumnChar = int(startingColumnChar) 

        print(f"Die Spitze des Schiffes liegt auf {placementInput}")
        #putting the 1 in the right position
        board[startingRowNumber][startingColumnChar] = 1
        #placing the ship in the right direction
        #TODO give ship to this function
        shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship)
        break

    printleakedBoard(board)
    
    #DELETE if Positions for ships are available 
    #placing the ship in the right direction
    #shipDirection(board, shipLength, startingRowNumber, startingColumnChar)
    
    # printleakedBoard(board)

def shipDirection(board, shipLength, startingRowNumber, startingColumnChar, ship):
    gameMode = 2
    while True: 
        directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
        if converterfunctions.directionConverter(board, shipLength, startingRowNumber, startingColumnChar, directionInput, gameMode, ship) == True:
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

        if converterfunctions.directionConverter(board, shipLength, startingRowNumber, startingColumnChar, cpuDirection, gameMode) == True:
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
    #TODO hier könnte eine falsche Ausgabe entstehen wegen dem +65, ist dafür da die Zahl zu einem char via ascii-Tabelle um zu wandeln
    print("Schuss auf: "+chr(column+65),row)
    if hiddenBoard[row][column] != 0:
        return 1
    #hitted ship
    elif leakedBoard[row][column] == 1:
        #get which ship is hit
        for ship in opponentShips:
            if(row,column)in ship.getPosition():
                shipName = ship
        shipName.hitOnShip()
        if shipName.getSize() == shipName.getDamageCounter():
            #ship sunk
            for position in shipName.getPosition():
                hiddenBoard[position]=4
            return 3
        #ship isnt sunk
        else:
            leakedBoard[row][column] = 3
        return 2
    #hitted water
    elif hiddenBoard[row][column] == 0:
        leakedBoard[row][column]= 2
    return 0
