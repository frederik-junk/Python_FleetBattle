import random
import python_game
import main
import hitShip

#variable to check if hit in former turn
# hitStatus = 0
rowLock = 1
columnLock = 1
directionLock = 0

#hit random field
def opponentAction():
    global hitStatus
    global rowLock
    global columnLock
    isHit = 1
    direction = random.randint(1,4)

    #if in previous turn something was hit
    if hitStatus == 0:

    #hit again, if random field was alredy fired at
        while isHit == 1:
            row = random.randint(1,10)
            column = random.randint(0,9)
<<<<<<< HEAD
            isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row)
=======
            isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column)
    
>>>>>>> c95e861e1909944a36de1b7a68f4df8989ff8379
    #what to do when there was a hit in the former round
    elif hitStatus == 1:
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
                    case 1: isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row-1)
                    case 2: isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column-1,row)
                    case 3: isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row+1)
                    case 4: isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column+1,row)

    i = 0 #move hit to a neighbouring field
    while isHit == 2:
<<<<<<< HEAD
         #for better undertanding what is happening
            print("Der Computer hat getroffen")
            hitStatus = 1
            #variable for hitting the next field
            i = i+1
            #check in which direction to shoot, when hit the rim and not sunk hit in opposide direction
            match direction:
                case 1:
                    if row - i >= 0:
                        isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row-i)
                        if i > 1 and isHit == 0:
                            direction = 3
                            directionLock = direction
                        #only one field was hit
                        elif i == 1 and isHit == 0:
                            directionLock = direction
                    else:
                        direction = 3
                        i = 0
                case 2:
                    if column - i >= 0:
                        isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column-i,row)   
                        if i > 1 and isHit == 0:
                            direction = 4
                            directionLock = direction
                       #only one field was hit
                        elif i == 1 and isHit == 0:
                            directionLock = 0
                    else:
                        direction = 4
                        i = 0
                case 3:
                    if row + i <= 9:
                        isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column,row+i)
                        if i > 1 and isHit == 0:
                            direction = 1
                            directionLock = direction
                        #only one field was hit
                        elif i == 1 and isHit == 0:
                            directionLock = 0
                    else:
                        direction = 1
                        i = 0
                case 4:
                    if column + i <= 9:
                        isHit = hitShip.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,column+i,row)
                        if i > 1 and isHit == 0:
                            direction = 2
                            directionLock = direction
                        #only one field was hit
                        elif i == 1 and isHit == 0:
                            directionLock = 0
                    else:
=======

        #for better undertanding what is happening
        print("Der Computer hat getroffen")
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
                    elif i == 1 and isHit == 0:
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
                    elif i == 1 and isHit == 0:
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
                    elif i == 1 and isHit == 0:
                        directionLock = 0
                else:
                    direction = 1
                    i = 0
            case 4:
                if column + i <= 9:
                    isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column+i)
                    if i > 1 and isHit == 0:
>>>>>>> c95e861e1909944a36de1b7a68f4df8989ff8379
                        direction = 2
                        directionLock = direction
                    #only one field was hit
                    elif i == 1 and isHit == 0:
                        directionLock = 0
                else:
                    direction = 2
                    i = 0
            
        
    #if ship is sunk reset hitStatus
    if isHit == 3:
        #for better undertanding what is happening
        print("Computer hat ein Schiff versenkt")
        i = 0
        hitStatus = 0
        opponentAction()

    #TODO delete after proper testing or fix if its used
    elif isHit == 1:
        print("This shouldnt hapen")
        opponentAction()

    #switch to player
    elif isHit == 0:
        #for better undertanding what is happening
        print("Der Computer hat Wasser getroffen")
        main.nextPlayer()
    
