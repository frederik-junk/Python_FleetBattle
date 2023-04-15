import random
import shipmanager

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
        print("  ".join(str(elem).replace("1","#").replace("0","~") for elem in row))


def printhiddenBoard(board):
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        print(str(i+1).zfill(2), end="  ")
        print("  ".join(str(elem).replace("1","~").replace("0","~").replace("2","O").replace("3","x").replace("4","X") for elem in row))

# printleakedBoard(board)
# print(" \n")
# printhiddenBoard(board)

shipLength = int(2)
#splitting the input into the column and row indices 
def splitColumn(placementInput):
  
    startingColumnChar = placementInput[0] #extrcting the first char of the users input
    
    #match case to convert the letters into column idexes
    match startingColumnChar:
                case "A": 
                    startingColumnChar = 0
                case "B": 
                    startingColumnChar = 1
                case "C": 
                    startingColumnChar = 2
                case "D": 
                    startingColumnChar = 3
                case "E": 
                    startingColumnChar = 4
                case "F": 
                    startingColumnChar = 5
                case "G": 
                    startingColumnChar = 6
                case "H": 
                    startingColumnChar = 7
                case "I": 
                    startingColumnChar = 8
                case "J": 
                    startingColumnChar = 9
                case _: 
                    print("Bitte geben sie Buchstaben zwischen A und J ein.")
                    print("Bitte geben sie eine neue Startposition an.")
                    placeShip
    return startingColumnChar

def splitRow(placementInput):
    startingRowNumber = placementInput[1:] #extracting the rest of the users input
    return startingRowNumber
            
#function to place a ship in the right position with the right length and the right direction
def placeShip(board, shipLength):
    while True:
        try:
            placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")

            startingColumnChar = splitColumn(placementInput)
            startingRowNumber = splitRow(placementInput)
  
            try:
                if startingColumnChar.isalpha() == False:
                    raise ValueError
                startingColumnChar = startingColumnChar.upper()
                
                
            except ValueError as e:
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
                value = board[startingRowNumber][startingColumnChar]

                print(f"Die Spitze des Schiffes liegt auf {placementInput}")
                #putting the 1 in the right position
                board[startingRowNumber][startingColumnChar] = 1
                #placing the ship in the right direction
                #TODO give ship to this function
                shipDirection(board, shipLength, startingRowNumber, startingColumnChar)
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

def directionConverter(board, shipLength, startingRowNumber, startingColumnChar, direction, gameMode):
    j = 0 # just a counting variable for later use
    positionTupelList = [] #this is the List which is given to the position list of the object
    match direction:
        case "w":
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingRowNumber - shipLength
                if betweenStartingRowNumber <= 0:
                    if gameMode == 1:
                        raise IndexError
                    else:
                        raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else:
                    #changing every index between the beginning and the end to a 1
                    while j < shipLength:
                        board[startingRowNumber][startingColumnChar] = 1
                        #this is for the positionTuple 
                        positionTupel = (startingRowNumber,startingColumnChar)
                        positionTupelList.append(positionTupel)

                        startingRowNumber = startingRowNumber - 1

                        j += 1
                    return False
            except IndexError as e:
                if gameMode == 2:       
                    print(str(e))
                    print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                    return True #is send back to the beginning to set another direction
                else:
                    return True
            

        case "a":
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingColoumnChar = startingColumnChar - shipLength
                if betweenStartingColoumnChar <= 0:
                    if gameMode == 1:
                        raise IndexError
                    else:
                        raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else:  
                    while j < shipLength:
                        board[startingRowNumber][startingColumnChar] = 1
                        #this is for the positionTupel
                        positionTupel = (startingRowNumber,startingColumnChar)
                        positionTupelList.append(positionTupel)

                        startingColumnChar -= 1
                        j += 1
                    repeater = False
                    return repeater
            except IndexError as e:
                if gameMode == 2:
                    print(str(e))
                    print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                    return True
                else:
                    return True
        case "s": 
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingColumnChar + shipLength
                if betweenStartingRowNumber > 10:
                    if gameMode == 1:
                        raise IndexError
                    else:
                        raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else: 
                    while j < shipLength:
                        board[startingRowNumber][startingColumnChar] = 1
                        #this is for the positionTupel
                        positionTupel = (startingRowNumber,startingColumnChar)
                        positionTupelList.append(positionTupel)

                        startingRowNumber += 1
                        j += 1
                    return False
            except IndexError as e:
                if gameMode == 2:
                    print(str(e))
                    print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                    return True
                else:
                    return True
        case "d":
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingColumnChar + shipLength
                if betweenStartingRowNumber > 10:
                    if gameMode == 1:
                        raise IndexError
                    else:
                        raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else:
                    while j < shipLength:
                        board[startingRowNumber][startingColumnChar] = 1
                        #this is for the positionTupel
                        positionTupel = (startingRowNumber,startingColumnChar)
                        positionTupelList.append(positionTupel)

                        startingColumnChar += 1
                        j += 1
                    return False
            except IndexError as e:
                if gameMode == 2:
                    print(str(e))
                    print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                    return True
                else: 
                    return True
        case _: 
            if gameMode == 2:
                print("Bitte bestimmen sie mithilfe von w,a,s,d die Ausrichtung des Schiffes. In Kleinbuchstaben")
                return True
            else: return True
    #setting of the ship position
    #ship.setPosition(positionTupelList)
    

def shipDirection(board, shipLength, startingRowNumber, startingColumnChar):
    gameMode = 2
    while True: 
        directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
        if directionConverter(board, shipLength, startingRowNumber, startingColumnChar, directionInput, gameMode) == True:
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
def addPlacementBlocker(board, positionTupelList):
    for tupel in positionTupelList:
        rowNumber, columnNumber = tupel
    #calculate the positions left, right, top and bottom of the position
    blockerLeftNumber = columnNumber - 1
    blockerRightNumber = columnNumber + 1
    blockerTopNumber = rowNumber - 1
    blockerBottomNumber = rowNumber + 1
    #list in which the blocker tupels are saved
    blockerList = []
    
    #if blocker number is out of bounce or there is a ship(1) ther will be no blocker placed
    if blockerTopNumber < 0 and blockerLeftNumber < 0 or board[blockerTopNumber][blockerLeftNumber] == 1:
        pass
    else:
        blockerList.append(blockerTopLeft = (blockerTopNumber, blockerLeftNumber))
        board[blockerTopNumber][blockerLeftNumber] = 6

    if blockerTopNumber < 0 or board[blockerTopNumber][columnNumber] == 1:
        pass
    else:
        blockerList.append(blockerTop = (blockerTopNumber, columnNumber))
        board[blockerTopNumber][columnNumber] = 6

    if blockerTopNumber < 0 and blockerRightNumber > 10 or board[blockerTopNumber][blockerRightNumber] == 0:
        pass
    else:
        blockerList.append(blockerTopRight = (blockerTopNumber, blockerRightNumber))
        board[blockerTopNumber][blockerRightNumber] = 6

    if  blockerRightNumber > 10 or board[rowNumber][blockerRightNumber] == 1:
        pass
    else:
        blockerList.append(blockerRight = (rowNumber, blockerRightNumber))
        board[rowNumber][blockerRightNumber] = 6

    if blockerBottomNumber > 10 and blockerRightNumber > 10 or board[blockerBottomNumber][blockerRightNumber] == 1:
        pass
    else:
        blockerList.append(blockerBottomRight = (blockerBottomNumber, blockerRightNumber))
        board[blockerBottomNumber][blockerRightNumber] = 6

    if blockerBottomNumber > 10 or board[blockerBottomNumber][columnNumber] == 1:
        pass
    else:
        blockerList.append(blockerBottom = (blockerBottomNumber, columnNumber))
        board[blockerBottomNumber][columnNumber] = 6

    if blockerBottomNumber > 10 and blockerLeftNumber < 0 or board[blockerBottomNumber][blockerLeftNumber] == 1:
        pass
    else:
        blockerList.append(blockerBottomLeft = (blockerBottomNumber, blockerLeftNumber))
        board[blockerBottomNumber][blockerLeftNumber] = 6
        
    if blockerLeftNumber < 0 or board[rowNumber][blockerLeftNumber] == 1:
        pass
    else:
        blockerList.append(blockerLeft = (rowNumber, blockerLeftNumber))
        board[rowNumber][blockerLeftNumber] = 6



#function for the cpu opponent to place the a ship
def cpuPlaceShip(board, shipLength):
    startingRowNumber = random.randint(0, 10)
    startingColoumnChar = random.randint(0, 10)

    #cpu places the ship with the random startig coordinates
    cpuShipDirection(board, shipLength, startingRowNumber, startingColoumnChar)
    printleakedBoard(board)

    
#cpuPlaceShip(board, shipLength)
# placeShip(board, shipLength)


def winoutput():
    print("_________________________________\n")
    print(" _____   _____   ______    _____")
    print("/ ____| |_   _| |  ____|  / ____|")     
    print("| (___    | |   | |__    | |  __")     
    print("\___ \    | |   |  __|   | | |_ |")     
    print("____) |  _| |_  | |____  | |__| |")     
    print("|_____/ |_____| |______|  \_____|")
    print("_________________________________\n")
#winoutput()

def loseoutput():
    print(" _   _   _____   ______   _____    ______   _____    _                    _____   ______")   
    print("| \ | | |_   _| |  ____| |  __ \  |  ____| |  __ \  | |          /\      / ____| |  ____|  ")
    print("|  \| |   | |   | |__    | |  | | | |__    | |__) | | |         /  \    | |  __  | |__     ")
    print("| . ` |   | |   |  __|   | |  | | |  __|   |  _  /  | |        / /\ \   | | |_ | |  __|    ")
    print("| |\  |  _| |_  | |____  | |__| | | |____  | | \ \  | |____   / ____ \  | |__| | | |____   ")
    print("|_| \_| |_____| |______| |_____/  |______| |_|  \_\ |______| /_/    \_\  \_____| |______|  ")
#loseoutput()

