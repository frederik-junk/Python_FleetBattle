from blockerfunctions import *
import python_game

def directionConverter(board, shipLength, startingRowNumber, startingColumnChar, direction, gameMode, ship):
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
                    addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
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
                    addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
                    return False
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
                    addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
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
                    addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
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


    #splitting the input into the column and row indices 
def splitColumnConverter(placementInput):
  
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
                    python_game.placeShip()
    return startingColumnChar

def splitRow(placementInput):
    startingRowNumber = placementInput[1:] #extracting the rest of the users input
    return startingRowNumber
    