import shipmanager
import random
import python_game


#o means opponent
oschlachtschiff1 = shipmanager.Schlachtschiff((1,1),(1,2),(1,3),(1,4),(1,5))
okreuzer1 = shipmanager.Kreuzer((1,1),(1,2),(1,3),(1,4))
okreuzer2 = shipmanager.Kreuzer((1,1),(1,2),(1,3),(1,4))
ozerstoerer1 = shipmanager.Zerstoerer((1,1),(1,2),(1,3))
ozerstoerer2 = shipmanager.Zerstoerer((1,1),(1,2),(1,3))
ozerstoerer3 = shipmanager.Zerstoerer((1,1),(1,2),(1,3))
ouboot1 = shipmanager.UBoot((1,1),(1,2))
ouboot2 = shipmanager.UBoot((1,1),(1,2))
ouboot3 = shipmanager.UBoot((1,1),(1,2))
ouboot4 = shipmanager.UBoot((1,1),(1,2))

opponentships = [oschlachtschiff1,okreuzer1,okreuzer2,ozerstoerer1,ozerstoerer2,ozerstoerer3,ouboot1,ouboot2,ouboot3,ouboot4]
def initShips():
    for ship in opponentships:
        length = ship.getSize()
        #python_game.cpuPlaceShip(leakedBoard2,length,ship)

def opponentAction():#hit random field 
    isHit = 1
    #hit again, if random field was alredy fired at
    while(isHit == 1):
        row = random.randint(1,10)
        column = random.randint(1,10)
        isHit = checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row,column)
    #fire again to a neighbouring field
    #TODO check if its in the field
    direction = random.randint(1,4)
    i = 0 #move hit to a neighbouring field
    while isHit == 2:
            i = i+1
            match direction:
                case 1:
                   isHit = checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row-i,column)
                case 2:
                    isHit = checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row,column-i)
                case 3:
                    isHit = checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row+i,column)
                case 4:
                    isHit = checkHit(python_game.hiddenBoard1,python_game.leakedBoard1,row,column+i)
                    
    #if a field is hit that was hit before shoot a random field
    #TODO what to do when hit a already shoot field after a hit
    if isHit == 1:
        opponentAction()
        
#hidden = ships hidden 
def checkHit(hiddenBoard,leakedBoard,row,column):
    #check if field was alredy hit
    if leakedBoard[row][column] != 0:
        return 1
    #hitted ship
    if hiddenBoard[row][column] == 1:
        #get which ship is hit
        for ship in opponentships:
            if(row,column)in ship.getPosition():
                shipName = ship
        shipName.hitOnShip()
        if shipName.getSize() == shipName.getDamageCounter():
            #ship sunk
            for position in shipName.getPosition():
                hiddenBoard[position]=4
            return 1
        #ship isnt sunk
        else:
            leakedBoard[row][column] = 3
        return 2
    #hitted water
    elif hiddenBoard[row][column] == 0:
        leakedBoard[row][column]= 2
    return 0
