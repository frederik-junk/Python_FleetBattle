import main
import circularImportFixing

#hidden = ships hidden
def checkHit(hiddenBoard,leakedBoard,column,row, gameMode):
    #check if field was alredy hit
    print("Sie schießen auf: "+chr(column+65),row)
    if hiddenBoard[row][column] != 0:
        return 1
    #hitted ship
    elif leakedBoard[row][column] == 1:
        #get which ship is hit
        #TODO are gameMode and currentplayer functioning?
        #don´t import main!
        if(gameMode == 1 and currentplayer == 2):  
            for ship in circularImportFixing.opponentShips:
                if(row,column)in ship.getPosition():
                    shipName = ship
                    break
        else:
            for ship in circularImportFixing.playerShips:
                if(row,column)in ship.getPosition():
                    shipName = ship
                    break
        shipName.hitOnShip()
        if shipName.getSize() == shipName.getDamageCounter():
            #ship sunk
            for position in shipName.getPosition():
                hiddenBoard[position]=4
            return 3
        #ship isnt sunk
        else:
            leakedBoard[row][column] = 3
        return 2
    #hitted water
    elif hiddenBoard[row][column] == 0:
        leakedBoard[row][column]= 2
    return 0
