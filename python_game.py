import random


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
    print("Der erste Buchstabe ist:", startingColumnChar)    #diese ausgabe kann entfernt werden
    print("Der Rest des Strings ist:", startingRowNumber) #diese ausgabe kann entfernt werden

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




def shipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar):
    directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
    j = 0 # just a counting variable for later use
    match directionInput:
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




def cpuShipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar):
    #get a random direction for the ship to be placed in
    cpuDirection = random.randint(0,4)
    match cpuDirection:
        case 0: cpuDirection = "w"
        case 1: cpuDirection = "a"
        case 2: cpuDirection = "s"
        case 3: cpuDirection = "d"
        case _: print("oh something went wrong") #eventuelle Schleife neue Zahl generieren 

    j = 0 # just a counting variable for later use
    match cpuDirection:
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
    lineone =  [1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1]
    linetwo =  [1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]
    linethree =[1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1]
    linefour = [0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1]
    linefive = [1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1]
    fullwordoutput = [lineone,linetwo,linethree,linefour,linefive]
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
    for i, row in enumerate(fullwordoutput):
        print("  ".join(str(elem).replace("1","#").replace("0"," ") for elem in row))
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
#winoutput()

def loseoutput():
    lineone =  [1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1]
    linetwo =  [1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0]
    linethree =[1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1]
    linefour = [1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0]
    linefive = [1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1]
    fullwordoutput = [lineone,linetwo,linethree,linefour,linefive]
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
    for i, row in enumerate(fullwordoutput):
        print("  ".join(str(elem).replace("1","#").replace("0"," ") for elem in row))
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
#loseoutput()

