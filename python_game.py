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
    while True:
        try:
            placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")


            #splitting the input into the column and row indices 
            startingColumnChar = placementInput[0] #extrcting the first char of the users input
            startingRowNumber = placementInput[1:] #extracting the rest of the users input
            #splitting the input into the column and row indices 
            startingColumnChar = placementInput[0] #extrcting the first char of the users input
            startingRowNumber = placementInput[1:] #extracting the rest of the users input
  
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
                    continue 
                   
            
            #adding one for the correct alignment still needs fixes
            startingRowNumber = int(startingRowNumber) - 1
            startingColumnChar = int(startingColumnChar) 

            if startingRowNumber < 0:
                print("Bitte geben sie eine neue Startposition an.")
                continue
            else:
                value = placementBoard[startingRowNumber][startingColumnChar]

                print(f"Die Spitze des Schiffes liegt auf {placementInput}")
                #putting the 1 in the right position
                placementBoard[startingRowNumber][startingColumnChar] = 1
                #placing the ship in the right direction
                shipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar)
                break
        except IndexError:
            #if the index is out of bounds
            print(f"Ihre Angabe {placementInput} liegt außerhalb des Spielfelds.")
            print("Bitte geben sie eine neue Startposition an.\n")

    printleakedBoard(placementBoard)


    
    #placing the ship in the right direction
    # shipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar)
    
    # printleakedBoard(placementBoard)

def directionConverter(placementBoard, shipLength, startingRowNumber, startingColumnChar, direction):
    j = 0 # just a counting variable for later use
    match direction:
        case "w":
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingRowNumber - shipLength
                if betweenStartingRowNumber < 0:
                    raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else:
                    #changing every index between the beginning and the end to a 1
                    while j < shipLength:
                        placementBoard[startingRowNumber][startingColumnChar] = 1
                        startingRowNumber = startingRowNumber - 1
                        j += 1
                    return False
            except IndexError as e:
                print(str(e))
                print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                return True #is send back to the beginning to set another direction
            

        case "a":
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingColoumnChar = startingColumnChar - shipLength
                if betweenStartingColoumnChar < 0:
                    raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else:  
                    while j < shipLength:
                        placementBoard[startingRowNumber][startingColumnChar] = 1
                        startingColumnChar -= 1
                        j += 1
                    return False
            except IndexError as e:
                print(str(e))
                print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                return True
        case "s": 
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingColumnChar + shipLength
                if betweenStartingRowNumber > 10:
                    raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else: 
                    while j < shipLength:
                        placementBoard[startingRowNumber][startingColumnChar] = 1
                        startingRowNumber += 1
                        j += 1
                    return False
            except IndexError as e:
                print(str(e))
                print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                return True
        case "d":
            try: # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingColumnChar + shipLength
                if betweenStartingRowNumber > 10:
                    raise IndexError("In dieser Richtung läuft das Schiff über das Spielfeld hinaus.")
                else:
                    while j < shipLength:
                        placementBoard[startingRowNumber][startingColumnChar] = 1
                        startingColumnChar += 1
                        j += 1
                    return False
            except IndexError as e:
                print(str(e))
                print("Bitte nehmen sie eine andere Richtung, in die das Schiff ausgerichtet werden soll.")
                return True
        case _: 
            print("Bitte bestimmen sie mithilfe von w,a,s,d die Ausrichtung des Schiffes. In Kleinbuchstaben")
            return True


def shipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar):
    while True: 
        directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
        directionConverter(placementBoard, shipLength, startingRowNumber, startingColumnChar, directionInput)
        printleakedBoard(placementBoard)
       



def cpuShipDirection(placementBoard, shipLength, startingRowNumber, startingColumnChar):
    #get a random direction for the ship to be placed in
    while True:
        cpuDirection = random.randint(0,3)
        match cpuDirection:
            case 0: cpuDirection = "w"
            case 1: cpuDirection = "a"
            case 2: cpuDirection = "s"
            case 3: cpuDirection = "d"
            case _: print("oh something went wrong") #eventuelle Schleife neue Zahl generieren 

        directionConverter(placementBoard, shipLength, startingRowNumber, startingColumnChar, cpuDirection)

#function for the cpu opponent to place the a ship
def cpuPlaceShip(placementBoard, shipLength):
    startingRowNumber = random.randint(0, 10)
    startingColoumnChar = random.randint(0, 10)

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
    print(" _   _   _____   ______   _____    ______   _____    _                    _____   ______")   
    print("| \ | | |_   _| |  ____| |  __ \  |  ____| |  __ \  | |          /\      / ____| |  ____|  ")
    print("|  \| |   | |   | |__    | |  | | | |__    | |__) | | |         /  \    | |  __  | |__     ")
    print("| . ` |   | |   |  __|   | |  | | |  __|   |  _  /  | |        / /\ \   | | |_ | |  __|    ")
    print("| |\  |  _| |_  | |____  | |__| | | |____  | | \ \  | |____   / ____ \  | |__| | | |____   ")
    print("|_| \_| |_____| |______| |_____/  |______| |_|  \_\ |______| /_/    \_\  \_____| |______|  ")
#loseoutput()

