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

def opponentAction():#hit random field 
    isHit = 1
    #hit again, if random field was alredy fired at
    while(isHit == 1):
        row = random.randint(1,10)
        column = random.randint(1,10)
        isHit = python_game.checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column)
    #fire again to a neighbouring field
    #TODO check if its in the field
    direction = random.randint(1,4)
    i = 0 #move hit to a neighbouring field
    while isHit == 2:
            i = i+1
            match direction:
                case 1:
                    python_game.isHit = checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row-i,column)
                case 2:
                    python_game.isHit = checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column-i)
                case 3:
                    python_game.isHit = checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row+i,column)
                case 4:
                    python_game.isHit = checkHit(python_game.hiddenBoard2,python_game.leakedBoard2,row,column+i)
                    
    #if a field is hit that was hit before shoot a random field
    #TODO what to do when hit a already shoot field after a hit
    if isHit == 1:
        opponentAction()
    #TODO look into how that is working
    main.nextPlayer()
    
