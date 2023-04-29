import blockerfunctions
from termcolor import colored
from colorama import init
init()

#own exception class
class wrongPlacement(Exception):
    pass

def directionConverter(board, shipLength, startingRowNumber, startingColumnChar, direction, gameMode, ship):
    j = 0 # just a counting variable for later use
    positionTupelList = [] #this is the List which is given to the position list of the object
    match direction:
        case "w":
            try:  # exception for the case that the ship is placed out of bounce in the given direction
                betweenStartingRowNumber = startingRowNumber - shipLength
                if betweenStartingRowNumber <= 0:
                    if gameMode == 1:
                        raise wrongPlacement
                    else:
                        raise wrongPlacement("laeuft aus Spielfeld")
                else:
                    # changing every index between the beginning and the end to a 1
                    while j < shipLength:
                        if board[startingRowNumber][startingColumnChar] == 1:
                            raise wrongPlacement("laeuft in anderes Schiff")
                        elif board[startingRowNumber][startingColumnChar] == 6:
                            raise wrongPlacement("laeuft in Blocker")
                        else:
                            #board[startingRowNumber][startingColumnChar] = 1 TODO:delete this

                            #this is for the positionTuple 
                            positionTupel = (startingRowNumber,startingColumnChar)
                            #add every postion tuple to tuple list to store the ship position
                            positionTupelList.append(positionTupel)

                            startingRowNumber = startingRowNumber - 1

                            j += 1
                        if j == shipLength:
                            for tupel in positionTupelList:
                                rowNumber, columnNumber = tupel
                                board[rowNumber][columnNumber] = 1
                    blockerfunctions.addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
                    return False
            except wrongPlacement as e:
                if gameMode == 2:
                    if str(e) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(e))
                        positionTupelList.clear()
                    
                    print(colored("Bitte platzieren Sie Ihr Schiff neu. Tipp:\n -Sie können die gleichen Koordinaten und eine andere Ausrichtung verwenden\n -Sie können aber auch eine neue Koordinate und eine neue Ausrichtung angeben",'cyan'))
                    return True
                else: 
                    return True
        case "a":
            try:  # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingColoumnChar = startingColumnChar - shipLength
                if betweenStartingColoumnChar < 0:
                    if gameMode == 1:
                        raise wrongPlacement
                    else:
                        raise wrongPlacement("laeuft aus Spielfeld")
                else:  
                    while j < shipLength:
                        if board[startingRowNumber][startingColumnChar] == 1:
                            raise wrongPlacement("laeuft in anderes Schiff")
                        elif board[startingRowNumber][startingColumnChar] == 6:
                            raise wrongPlacement("laeuft in Blocker")
                        else:
                            #board[startingRowNumber][startingColumnChar] = 1 TODO:this can be deleted
                            #this is for the positionTupel
                            positionTupel = (startingRowNumber,startingColumnChar)
                            #add every postion tuple to tuple list to store the ship position
                            positionTupelList.append(positionTupel)

                            startingColumnChar -= 1
                            j += 1
                        if j == shipLength:
                            for tupel in positionTupelList:
                                rowNumber, columnNumber = tupel
                                board[rowNumber][columnNumber] = 1
                    blockerfunctions.addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
                    return False
            except wrongPlacement as e:
                if gameMode == 2:
                    if str(e) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(e))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu. Tipp:\n -Sie können die gleichen Koordinaten und eine andere Ausrichtung verwenden\n -Sie können aber auch eine neue Koordinate und eine neue Ausrichtung angeben",'cyan'))
                    return True
                else: 
                    return True
        case "s":
            try:  # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingRowNumber + shipLength
                if betweenStartingRowNumber > 10:
                    if gameMode == 1:
                        raise wrongPlacement
                    else:
                        raise wrongPlacement("laeuft aus Spielfeld")
                else: 
                    while j < shipLength:
                        if board[startingRowNumber][startingColumnChar] == 1:
                            raise wrongPlacement("laeuft in anderes Schiff")
                        elif board[startingRowNumber][startingColumnChar] == 6:
                            raise wrongPlacement("laeuft in Blocker")
                        else:
                            #board[startingRowNumber][startingColumnChar] = 1 TODO: delete this
                            #this is for the positionTupel
                            positionTupel = (startingRowNumber,startingColumnChar)
                            #add every postion tuple to tuple list to store the ship position
                            positionTupelList.append(positionTupel)

                            startingRowNumber += 1
                            j += 1
                        if j == shipLength:
                            for tupel in positionTupelList:
                                rowNumber, columnNumber = tupel
                                board[rowNumber][columnNumber] = 1
                    blockerfunctions.addPlacementBlocker(board, positionTupelList)
                    ship.setPosition(positionTupelList)
                    return False
            except wrongPlacement as e:
                if gameMode == 2:
                    if str(e) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(e))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu. Tipp:\n -Sie können die gleichen Koordinaten und eine andere Ausrichtung verwenden\n -Sie können aber auch eine neue Koordinate und eine neue Ausrichtung angeben",'cyan'))
                    return True
                else: 
                    return True
        case "d":
            try:  # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingColumnChar + shipLength
                if betweenStartingRowNumber > 10:
                    if gameMode == 1:
                        raise wrongPlacement
                    else:
                        raise wrongPlacement("laeuft aus Spielfeld")
                else:
                    while j < shipLength:
                        if board[startingRowNumber][startingColumnChar] == 1:
                            raise wrongPlacement("laeuft in anderes Schiff")
                        elif board[startingRowNumber][startingColumnChar] == 6:
                            raise wrongPlacement("laeuft in Blocker")
                        else:
                            #board[startingRowNumber][startingColumnChar] = 1 TODO: delete this
                            #this is for the positionTupel
                            positionTupel = (startingRowNumber,startingColumnChar)
                            #add every postion tuple to tuple list to store the ship position
                            positionTupelList.append(positionTupel)
                            
                            startingColumnChar += 1
                            j += 1
                        if j == shipLength:
                            for tupel in positionTupelList:
                                rowNumber, columnNumber = tupel
                                board[rowNumber][columnNumber] = 1
                    ship.setPosition(positionTupelList)
                    blockerfunctions.addPlacementBlocker(board, positionTupelList)
                    return False
            except wrongPlacement as e:
                if gameMode == 2:
                    if str(e) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(e) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(e))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu. Tipp:\n -Sie können die gleichen Koordinaten und eine andere Ausrichtung verwenden\n -Sie können aber auch eine neue Koordinate und eine neue Ausrichtung angeben",'cyan'))
                    return True
                else:
                    return True
        case _:
            if gameMode == 2:
                print(
                    "Bitte bestimmen Sie mithilfe der Tasten [w][a][s][d] die Ausrichtung des Schiffes."
                )
                return True
            else:
                return True
    # setting of the ship position
    # ship.setPosition(positionTupelList)

    # splitting the input into the column and row indices

def splitColumnConverter(placementInput):
    startingColumnChar = str(
        placementInput[0]
    )  # extracting the first char of the users input
    try:
        if startingColumnChar.isalpha() is False:
            raise ValueError
        else:
            startingColumnChar = startingColumnChar.upper()
        # match case to convert the letters into column idexes
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
                print("Bitte geben Sie Buchstaben zwischen A und J ein.\n")
                print("Bitte geben Sie eine neue Startposition an.\n")
                startingColumnChar = 11
                return startingColumnChar
        return startingColumnChar
    except ValueError as e:
        print(str(e))
        print(colored("Ihre Eingabe enthaelt Fehler. Bitte geben Sie erst den Buchstaben und dann die Zahl an.",'red'))
        print("Geben Sie bitte die Anfangskoordinaten erneut an (z.B.: A3).")
        startingColumnChar = 11
        return startingColumnChar

def splitRow(placementInput):
    try:
        startingRowNumber = int(placementInput[1:])
        # extracting the rest of the users input
        # the code above could raise a ValueError which is excepted down below
        if 0 < startingRowNumber <= 10:
            return startingRowNumber - 1
        else:
            raise ValueError("Ihre Angabe liegt außerhalb vom Spielfeld")

    except ValueError:
        startingRowNumber = 11
        return startingRowNumber
