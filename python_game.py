import random
import shipmanager

letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow =   [0,0,0,0,0,0,0,0,0,0]
secondRow =  [0,0,0,0,0,0,0,0,0,0]
thirdRow =   [0,0,0,0,0,0,0,2,0,0]
fourthRow =  [0,0,0,0,2,0,0,0,0,0]
fifthRow =   [0,0,0,0,0,0,0,0,0,0]
sixthRow =   [0,0,2,0,0,0,4,0,0,0]
seventhRow = [0,0,0,0,0,0,4,0,0,0]
eighthRow =  [0,0,0,3,0,0,4,0,0,0]
ninethRow =  [0,0,0,0,0,0,0,0,0,0]
tenthRow =   [0,0,0,0,0,0,0,0,0,0]
placementBoard = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]

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

# printleakedBoard(placementBoard)
# print(" \n")
# printhiddenBoard(placementBoard)





shipLength = int(2)



# function to place a ship in the right position with the right length and the right direction
def placeShip(placementBoard, shipLength):
    placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")


    #splitting the input into the column and row indices 
    startingColumnChar = placementInput[0] #extrcting the first char of the users input
    startingRowNumber = placementInput[1:] #extracting the rest of the users input

    #match case to convert the letters into column idexes
    match startingColumnChar:
        case "A": startingColumnChar = 0
        case "B": startingColumnChar = 1
        case "C": startingColumnChar = 2
        case "D": startingColumnChar = 3
        case "E": startingColumnChar = 4
        case "F": startingColumnChar = 5
        case "G": startingColumnChar = 6
        case "H": startingColumnChar = 7
        case "I": startingColumnChar = 8
        case "J": startingColumnChar = 9
        case _: print("Bitte geben sie Buchstaben zwischen A und J ein")
    
    #adding one for the correct alignment still needs fixes
    startingRowNumber = int(startingRowNumber) - 1
    startingColumnChar = int(startingColumnChar) 

    
    #putting the 1 in the right position
    placementBoard[startingRowNumber][startingColumnChar] = 1

    # printleakedBoard(placementBoard)


    
    #placing the ship in the right direction
    # shipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar)
    
    # printleakedBoard(placementBoard)

def directionConverter(placementBoard, shipLength, startingRowNumber, startingColumnChar, direction):
    j = 0 # just a counting variable for later use
    match direction:
        case "w": 
            #changing every index between the beginning and the end to a 1
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingRowNumber = startingRowNumber - 1
                j += 1

        case "a": 
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingColumnChar -= 1
                j += 1

        case "s": 
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingRowNumber += 1
                j += 1

        case "d": 
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingColumnChar += 1
                j += 1

        case _: print("Bitte bestimmen sie mithilfe von w,a,s,d die Ausrichtung des Schiffes. In Kleinbuchstaben")

    
def shipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar):
    directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
    directionConverter(placementBoard, shipLength, startingRowNumber, startingColumnChar, directionInput)
 
         
def cpuShipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar):
    #get a random direction for the ship to be placed in
    cpuDirection = random.randint(0,4)
    match cpuDirection:
        case 0: cpuDirection = "w"
        case 1: cpuDirection = "a"
        case 2: cpuDirection = "s"
        case 3: cpuDirection = "d"
        case _: print("oh something went wrong") #eventuelle Schleife neue Zahl generieren 

    directionConverter(placementBoard, shipLength, startingRowNumber, startingColumnChar, cpuDirection)

#function for the cpu opponent to place the a ship
def cpuPlaceShip(placementBoard, shipLength):
    startingRowNumber = random.randint(0, 11)
    startingColoumnChar = random.randint(0, 11)

    #cpu places the ship with the random startig coordinates
    cpuShipDirection(placementBoard, shipLength, startingRowNumber, startingColoumnChar)
    printleakedBoard(placementBoard)

    
#cpuPlaceShip(placementBoard, shipLength)
# placeShip(placementBoard, shipLength)

    
    


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
    print("  _   _   _____   ______   _____    ______   _____    _                    _____   ______")   
    print("| \ | | |_   _| |  ____| |  __ \  |  ____| |  __ \  | |          /\      / ____| |  ____|  ")
    print("|  \| |   | |   | |__    | |  | | | |__    | |__) | | |         /  \    | |  __  | |__     ")
    print("| . ` |   | |   |  __|   | |  | | |  __|   |  _  /  | |        / /\ \   | | |_ | |  __|    ")
    print("| |\  |  _| |_  | |____  | |__| | | |____  | | \ \  | |____   / ____ \  | |__| | | |____   ")
    print("|_| \_| |_____| |______| |_____/  |______| |_|  \_\ |______| /_/    \_\  \_____| |______|  ")
#loseoutput()


