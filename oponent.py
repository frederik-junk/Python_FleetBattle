import shipmanager
import random
import python_game


#Schiffe noch Initialisieren mit vernünftigen Positions
oschlachtschiff1 = shipmanager.Schlachtschiff((1,1))
okreuzer1 = shipmanager.Kreuzer((1,1))
okreuzer2 = shipmanager.Kreuzer((1,1))
ozerstoerer1 = shipmanager.Zerstoerer((1,1))
ozerstoerer2 = shipmanager.Zerstoerer((1,1))
ozerstoerer3 = shipmanager.Zerstoerer((1,1))
ouboot1 = shipmanager.Uboot((1,1))
ouboot2 = shipmanager.Uboot((1,1))
ouboot3 = shipmanager.Uboot((1,1))
ouboot4 = shipmanager.Uboot((1,1))

opponentships = [oschlachtschiff1,okreuzer1,okreuzer2,ozerstoerer1,ozerstoerer2,ozerstoerer3,ouboot1,ouboot2,ouboot3,ouboot4]
def opponentAction():#random Feld fuer Treffer
    isHit = 1
    #erneut schießen, wenn das random Feld schonmal beschossen wurde nochmal schießen
    while(isHit == 1):
        row = random.randint(1,10)
        column = random.randint(1,10)
        isHit = checkHit(hiddenBoard1,leakedBoard1,row,coulmn)
    #erneut feuern auf ein anliegendes Feld
    direction = random.randint(1,4)
    #TODO checken, dass es noch im Feld ist
    i = 0 #variable zum verschieben des Treffers
    while isHit == 2:
            i = i+1
            match direction:
                case 1:
                   isHit = checkHit(hiddenBoard1,leakedBoard1,row-i,coulmn)
                case 2:
                    isHit = checkHit(hiddenBoard1,leakedBoard1,row,coulmn-i)
                case 3:
                    isHit = checkHit(hiddenBoard1,leakedBoard1,row+i,coulmn)
                case 4:
                    isHit = checkHit(hiddenBoard1,leakedBoard1,row,coulmn+i)
                    
    #wenn auf ein Feld geschoss wird, dass schonmal beschossen wurde wieder random schießen
    if isHit == 1:
        opponentAction()
        
#hidden = Schiffe versteckt 
def checkHit(hiddenBoard,leakedBoard,row,column):
    #check ob auf das Feld schonmal geschossen wurde
    if leakedBoard[row][column] != 0:
        return 1
    #wenn ein Schiff an der Position ist
    if hiddenBoard[row][column] == 1:
        #welches Schiff ist getroffen ermitteln
        for ship in opponentships:
            if(row,column)in ship.getPosition():
                shipName = ship
        shipName.hitOnShip()
        if shipName.getSize() == shipName.getDamageCounter():
            #Schiff versenkt
            for position in shipName.getPosition():
                hiddenBoard[position]=4
        #Schiff nicht versenkt
        else:
            leakedBoard[row][column] = 3
        return 2
    #wenn Wasser an derPosition ist
    elif hiddenBoard[row][column] == 0:
        leakedBoard[row][column]= 2
    return 0
