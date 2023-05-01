def addPlacementBlocker(board, positionTupelList):
    """ Function to add the blockers so that ships cant be placed next to the ship

    Args:
        board (List): The board on which ships can be placed
        positionTupelList (List): A tupel list that contains the coordinates of the ships position
    """
    for tupel in positionTupelList:
        rowNumber, columnNumber = tupel
        # calculate the positions left, right, top and bottom of the position (4 directions around the placed ship compartment)
        blockerLeftNumber = columnNumber - 1
        blockerRightNumber = columnNumber + 1
        blockerTopNumber = rowNumber - 1
        blockerBottomNumber = rowNumber + 1
        # list in which the blocker tupels are saved
        blockerList = []

        # adding a blocker around each ship psotiob to avoid nearby placning of ships
        # proving if the blocker is out of bounce or if there is a ship (top left corner)
        if (
            blockerTopNumber < 0
            or blockerLeftNumber < 0
            or board[blockerTopNumber][blockerLeftNumber] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blockerTopLeft = (blockerTopNumber, blockerLeftNumber)
            blockerList.append(blockerTopLeft)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blockerTopNumber][blockerLeftNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (top middle)
        if blockerTopNumber < 0 or board[blockerTopNumber][columnNumber] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker  and adding it to the list
            blockerTop = (blockerTopNumber, columnNumber)
            blockerList.append(blockerTop)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blockerTopNumber][columnNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (top right corner)
        if (
            blockerTopNumber < 0
            or blockerRightNumber >= 10
            or board[blockerTopNumber][blockerRightNumber] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker  and adding it to the list
            blockerTopRight = (blockerTopNumber, blockerRightNumber)
            blockerList.append(blockerTopRight)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blockerTopNumber][blockerRightNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (right middle)
        if blockerRightNumber >= 10 or board[rowNumber][blockerRightNumber] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blockerRight = (rowNumber, blockerRightNumber)
            blockerList.append(blockerRight)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[rowNumber][blockerRightNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (bottom right corner)
        if (
            blockerBottomNumber >= 10
            or blockerRightNumber >= 10
            or board[blockerBottomNumber][blockerRightNumber] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blockerBottomRight = (blockerBottomNumber, blockerRightNumber)
            blockerList.append(blockerBottomRight)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blockerBottomNumber][blockerRightNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (bottom middle)
        if blockerBottomNumber >= 10 or board[blockerBottomNumber][columnNumber] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blockerBottom = (blockerBottomNumber, columnNumber)
            blockerList.append(blockerBottom)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blockerBottomNumber][columnNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (bottom left corner)
        if (
            blockerBottomNumber >= 10
            or blockerLeftNumber < 0
            or board[blockerBottomNumber][blockerLeftNumber] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blockerBottomLeft = (blockerBottomNumber, blockerLeftNumber)
            blockerList.append(blockerBottomLeft)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blockerBottomNumber][blockerLeftNumber] = 6

        # proving if the blocker is out of bounce or if there is a ship (left middle)
        if blockerLeftNumber < 0 or board[rowNumber][blockerLeftNumber] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blockerLeft = (rowNumber, blockerLeftNumber)
            blockerList.append(blockerLeft)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[rowNumber][blockerLeftNumber] = 6
