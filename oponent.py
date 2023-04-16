import random
import python_game
import main
"""
#TODO delete comment when ships are implemented differently
#TODO import shipmanager if want to use again
#TODO real ship positions getter 
oschlachtschiff1 = shipmanager.Schlachtschiff(((1,1),(1,2),(1,3),(1,4),(1,5)))
okreuzer1 = shipmanager.Kreuzer(((1,1),(1,2),(1,3),(1,4)))
okreuzer2 = shipmanager.Kreuzer(((1,1),(1,2),(1,3),(1,4)))
ozerstoerer1 = shipmanager.Zerstoerer(((1,1),(1,2),(1,3)))
ozerstoerer2 = shipmanager.Zerstoerer(((1,1),(1,2),(1,3)))
ozerstoerer3 = shipmanager.Zerstoerer(((1,1),(1,2),(1,3)))
ouboot1 = shipmanager.UBoot(((1,1),(1,2)))
ouboot2 = shipmanager.UBoot(((1,1),(1,2)))
ouboot3 = shipmanager.UBoot(((1,1),(1,2)))
ouboot4 = shipmanager.UBoot(((1,1),(1,2)))

opponentShips = [oschlachtschiff1,okreuzer1,okreuzer2,ozerstoerer1,ozerstoerer2,ozerstoerer3,ouboot1,ouboot2,ouboot3,ouboot4]
def initOpponentShips():
    for ship in opponentShips:
        length = ship.getSize()
        python_game.cpuPlaceShip(python_gameleakedBoard1,length,ship)
"""


"""
    #TODO implement this usefully
    #for better undertanding what is happening
    if isHit == 2:
        print("Der Computer hat getroffen")
    else:
        print("Der Computer hat ins Wasser geschossen!")
"""

#variable to check if hit in former turn 
hitStatus = 0
rowLock = 1
columnLock = 1
directionLock = 0
def opponentAction():#hit random field 
    isHit = 1
    global hitStatus
    direction = random.randint(1,4)
    #if in previous turn something was hit
    if hitStatus == 0:
    #hit again, if random field was alredy fired at
        while(isHit == 1):
            row = random.randint(1,10)
            column = random.randint(1,10)
            isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column)
    #what to do when there was a hit in the former round
    elif hitStatus == 1:
        global rowLock
        global columnLock
        row = rowLock
        column = columnLock
        #if direction is known use it
        if directionLock != 0:
            direction = directionLock
        #if direction is unknown use a new random direction  
        elif directionLock == 0:
            while isHit == 1:
                direction = random.randint(1,4)
                match direction:
                    case 1: isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row-1,column)
                    case 2: isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column-1)
                    case 3: isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row+1,column)
                    case 4: isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column+1)

    i = 0 #move hit to a neighbouring field
    while isHit == 2:
            hitStatus = 1
            #variable for hitting the next field
            i = i+1
            #check in which direction to shoot, when hit the rim and not sunk hit in opposide direction
            match direction:
                case 1:
                    if row - i >= 0:
                        isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row-i,column)
                        if i > 1 and isHit == 0:
                            direction = 3
                            directionLock = direction
                        #only one field was hit
                        elif i == 1 and isHIt == 0:
                            directionLock = direction
                    else:
                        direction = 3
                        i = 0
                case 2:
                    if column - i >= 0:
                        isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column-i)   
                        if i > 1 and isHit == 0:
                            direction = 4
                            directionLock = direction
                       #only one field was hit
                        elif i == 1 and isHIt == 0:
                            directionLock = 0
                    else:
                        direction = 4
                        i = 0
                case 3:
                    if row + i <= 9:
                        isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row+i,column)
                        if i > 1 and isHit == 0:
                            direction = 1
                            directionLock = direction
                        #only one field was hit
                        elif i == 1 and isHIt == 0:
                            directionLock = 0
                    else:
                        direction = 1
                        i = 0
                case 4:
                    if column + i <= 9:
                        isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column+i)
                        if i > 1 and isHit == 0:
                            direction = 2
                            directionLock = direction
                        #only one field was hit
                        elif i == 1 and isHIt == 0:
                            directionLock = 0
                    else:
                        direction = 2
                        i = 0
            
        
    #if ship is sunk reset hitStatus
    if isHit == 3:
        i = 0
        hitStatus = 0
        opponentAction()

    #TODO delete after proper testing or fix if its used
    elif isHit == 1:
        print("This shouldnt hapen")
        opponentAction()

    #switch to player
    elif isHit == 0:
        main.nextPlayer()
    
