"""
import main
import circularImportFixing

#hidden = ships hidden
def checkHit(hiddenBoard,leakedBoard,column,row,gameMode):
    #check if field was alredy hit
    print("Sie schießen auf: "+chr(column+65),row + 1)
    if hiddenBoard[row][column] != 0:
        return 1
    #hitted ship
    elif leakedBoard[row][column] == 0:
        #get which ship is hit
        #TODO are gameMode and currentplayer functioning?
        #don´t import main!
        if(main.gameMode == 1 and main.currentplayer == 2):  
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
                print(type(position[0]))
                hiddenBoard[a,b] = 4
            return 3
        #ship isnt sunk
        else:
            hiddenBoard[row][column] = 3
        return 2
    #hitted water
    elif leakedBoard[row][column] == 0:
        hiddenBoard[row][column]= 2
    return 0
"""

    
