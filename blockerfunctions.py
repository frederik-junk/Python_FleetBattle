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
        if blockerTopNumber < 0 or blockerLeftNumber < 0 or board[blockerTopNumber][blockerLeftNumber] == 1:
            pass
        else:
            blockerTopLeft = (blockerTopNumber, blockerLeftNumber)
            blockerList.append(blockerTopLeft)
            board[blockerTopNumber][blockerLeftNumber] = 6

        if blockerTopNumber < 0 or board[blockerTopNumber][columnNumber] == 1:
            pass
        else:
            blockerTop = (blockerTopNumber, columnNumber)
            blockerList.append(blockerTop)
            board[blockerTopNumber][columnNumber] = 6

        if blockerTopNumber < 0 or blockerRightNumber >= 10 or board[blockerTopNumber][blockerRightNumber] == 1:
            pass
        else:
            blockerTopRight = (blockerTopNumber, blockerRightNumber)
            blockerList.append(blockerTopRight)
            board[blockerTopNumber][blockerRightNumber] = 6

        if  blockerRightNumber >= 10 or board[rowNumber][blockerRightNumber] == 1:
            pass
        else:
            blockerRight = (rowNumber, blockerRightNumber)
            blockerList.append(blockerRight)
            board[rowNumber][blockerRightNumber] = 6

        if blockerBottomNumber >= 10 or blockerRightNumber >= 10 or board[blockerBottomNumber][blockerRightNumber] == 1:
            pass
        else:
            blockerBottomRight = (blockerBottomNumber, blockerRightNumber)
            blockerList.append(blockerBottomRight)
            board[blockerBottomNumber][blockerRightNumber] = 6

        if blockerBottomNumber >= 10 or board[blockerBottomNumber][columnNumber] == 1:
            pass
        else:
            blockerBottom = (blockerBottomNumber, columnNumber)
            blockerList.append(blockerBottom)
            board[blockerBottomNumber][columnNumber] = 6

        if blockerBottomNumber >= 10 or blockerLeftNumber < 0 or board[blockerBottomNumber][blockerLeftNumber] == 1:
            pass
        else:
            blockerBottomLeft = (blockerBottomNumber, blockerLeftNumber)
            blockerList.append(blockerBottomLeft)
            board[blockerBottomNumber][blockerLeftNumber] = 6
            
        if blockerLeftNumber < 0 or board[rowNumber][blockerLeftNumber] == 1:
            pass
        else:
            blockerLeft = (rowNumber, blockerLeftNumber)
            blockerList.append(blockerLeft)
            board[rowNumber][blockerLeftNumber] = 6
