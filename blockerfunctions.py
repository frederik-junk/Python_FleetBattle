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
