"""Module contains functions to define the placement of the ships on the board
"""
from termcolor import colored
from colorama import init
import blockerfunctions
init()

#own exception class
class WrongPlacement(Exception):
    """Own exception class

    Args:
        Exception (Error): Prints an error message
    """
    pass

def directionConverter(board, shipLength, startingRowNumber, startingColumnChar, direction, gameMode, ship):
    """Function that is used to define the direction the ship is placed, based on the tip of the ship

    Args:
        board (List): The board on which the ships are placed
        shipLength (int): The length of each ship individual
        startingRowNumber (int): The number of the row in which the ship should be placed
        startingColumnChar (char): The letter of the column in which the ship should be placed
        direction (String): The direction in which the ship should be placed, based on its tip
        gameMode (int): The game mode to decide if player 2 has to set his ships too or if its computer generated
        ship (class): The class of each ship to set some initial values

    Raises:
        WrongPlacement: Prints an error message for different occasions, for example if a wrong direction char is given as input

    Returns:
        boolean: Returns a True or False value, depending on each branch
    """
    j = 0 # just a counting variable for later use
    positionTupelList = [] #this is the List which is given to the position list of the object
    match direction:
        case "w":
            try:  # exception for the case that the ship is placed out of bounce in the given direction
                betweenStartingRowNumber = startingRowNumber - shipLength
                if betweenStartingRowNumber <= 0:
                    if gameMode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                # changing every index between the beginning and the end to a 1
                while j < shipLength:
                    if board[startingRowNumber][startingColumnChar] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[startingRowNumber][startingColumnChar] == 6:
                        raise WrongPlacement("laeuft in Blocker")
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
            except WrongPlacement as placementError:
                if gameMode == 2:
                    if str(placementError) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(placementError))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.",'cyan'))
                    print(colored("Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und Ausrichtung.",'cyan'))
                    return True
                return True
        case "a":
            try:  # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingColoumnChar = startingColumnChar - shipLength
                if betweenStartingColoumnChar < 0:
                    if gameMode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                while j < shipLength:
                    if board[startingRowNumber][startingColumnChar] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[startingRowNumber][startingColumnChar] == 6:
                        raise WrongPlacement("laeuft in Blocker")
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
            except WrongPlacement as placementError:
                if gameMode == 2:
                    if str(placementError) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(placementError))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.",'cyan'))
                    print(colored("Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und Ausrichtung.",'cyan'))
                    return True
                return True
        case "s":
            try:  # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingRowNumber + shipLength
                if betweenStartingRowNumber > 10:
                    if gameMode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                while j < shipLength:
                    if board[startingRowNumber][startingColumnChar] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[startingRowNumber][startingColumnChar] == 6:
                        raise WrongPlacement("laeuft in Blocker")
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
            except WrongPlacement as placementError:
                if gameMode == 2:
                    if str(placementError) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(placementError))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.",'cyan'))
                    print(colored("Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und Ausrichtung.",'cyan'))
                    return True
                return True
        case "d":
            try:  # exception for the case that the ship travels out of bounce in the given direction
                betweenStartingRowNumber = startingColumnChar + shipLength
                if betweenStartingRowNumber > 10:
                    if gameMode == 1:
                        raise WrongPlacement
                    raise WrongPlacement("laeuft aus Spielfeld")
                while j < shipLength:
                    if board[startingRowNumber][startingColumnChar] == 1:
                        raise WrongPlacement("laeuft in anderes Schiff")
                    if board[startingRowNumber][startingColumnChar] == 6:
                        raise WrongPlacement("laeuft in Blocker")
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
            except WrongPlacement as placementError:
                if gameMode == 2:
                    if str(placementError) == "laeuft aus Spielfeld":
                        print(colored("In dieser Richtung läuft das Schiff aus dem Spielfeld",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in anderes Schiff":
                        print(colored("In dieser Richtung läuft das Schiff in eine anderes Schiff.",'red'))
                        positionTupelList.clear()
                    elif str(placementError) == "laeuft in Blocker":
                        print(colored("In dieser Richtung laeuft das Schiff in einen Verbotenen Bereich.",'red'))
                        positionTupelList.clear()
                    else:
                        print(str(placementError))
                        positionTupelList.clear()
                    print(colored("Bitte platzieren Sie Ihr Schiff neu.",'cyan'))
                    print(colored("Verwenden Sie eine andere Ausrichtung oder neue Koordinaten und Ausrichtung.",'cyan'))
                    return True
                return True
        case _:
            if gameMode == 2:
                print(
                    "Bitte bestimmen Sie mithilfe der Tasten [w][a][s][d] die Ausrichtung des Schiffes."
                )
                return True
            return True
    # setting of the ship position
    # ship.setPosition(positionTupelList)

def splitColumnConverter(placementInput):
    """Function that splits the input into the column and row indices

    Args:
        placementInput (_type_): _description_

    Raises:
        ValueError: Prints an error message if wrong input is given from the user

    Returns:
        startingColumnChar(char): The char to indicate the current column
    """
    startingColumnChar = str(
        placementInput[0]
    )  # extracting the first char of the users input
    try:
        if startingColumnChar.isalpha() is False:
            raise ValueError
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
    except ValueError as valueError:
        print(str(valueError))
        print(colored("Ihre Eingabe enthaelt Fehler. Bitte geben Sie erst den Buchstaben und dann die Zahl an.",'red'))
        print("Geben Sie bitte die Anfangskoordinaten erneut an (z.B.: A3).")
        startingColumnChar = 11
        return startingColumnChar

def splitRow(placementInput):
    """Function that splits the input into Rows

    Args:
        placementInput (_type_): _description_

    Raises:
        ValueError: Prints an error message if wrong input is given from the user

    Returns:
        startingRowNumber(int): The number of the current row where the ship is to be placed
    """
    try:
        startingRowNumber = int(placementInput[1:])
        # extracting the rest of the users input
        # the code above could raise a ValueError which is excepted down below
        if 0 < startingRowNumber <= 10:
            return startingRowNumber - 1
        raise ValueError("Ihre Angabe liegt außerhalb vom Spielfeld")
    except ValueError:
        startingRowNumber = 11
        return startingRowNumber
