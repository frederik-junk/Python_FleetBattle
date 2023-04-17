import shipmanager
import main
import circularImportFixing
import converterfunctions
import python_game
import outputmanager


directionLock = 0
hitStatus = 0

def shooting(gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    #used for CPU
    positionMemory = (1,1)
    shootingRepeater = True
    if gameMode ==  1:
        if currentPlayer == 1:
            #loop isnt working here yet
            global hitStatus
            global directionLock
            print("You have")
            #hier KI Technik
            leakedBoard = python_game.leakedBoard2
            hiddenBoard = python_game.hiddenBoard1
            #counterVariable for shooting
            i = 0
            #ship wasnt hit before
            if hitStatus == 0:
                while leakedBoard[row][column] !=0:
                    row = random.randint(0,9)
                    column = random.randint(0,9)
                shootingTupel = (row, column)
                positionMemory = (shootingTupel)
                
            #continue hitting ship till its sunk
            elif hitStatus == 1:
                #Richtung des Schiffes noch nicht
                if directionLock == 0:
                    direction = random.randint(1,4)
                    match direction:
                        case 1: shootingTupel = (row-i, column)
                        case 2: shootingTupel = (row, column-i)
                        case 3: shootingTupel = (row+i, column)
                        case 4: shootingTupel = (row, column+i)
                else:
                    #muss noch befüllt werden, hier wird weiter in eine herausgefundene Richtung geschossen
                    row = converterfunctions.splitRow(positionMemory)
                    column = converterfunctions.splitColumnConverter(positionMemory)#CHECK will this work with a number?
                    shootingTupel = (row, column+i)

                    
                hitStatus = 1   
            match leakedBoard[row][column]:
                #hit water
                case 0:
                    print("Der Computer erzielt einen Wassertreffer")
                    hiddenBoard[row][column] = 2
                    python_game.printhiddenBoard
                    shootingRepeater = False
                    #change direction if known, but water was hit
                    if directionLock !=0:
                        match directionLock:
                            case 1: direction Lock = 3
                            case 2: direction Lock = 4
                            case 3: direction Lock = 1
                            case 4: direction Lock = 2
                        
                #hit ship
                case 1:
                    #TODO do a loop that doesnt always shoot the same field, this one shoots the same field every time
                    #while shootingRepeater == True: 
                        #determine which ship is hit
                        for ship in circularImportFixing.playerShips:
                                postitions = ship.getPosition()
                                if shootingTupel in postitions:
                                    print("Der Computer hat getroffen")
                                    hiddenBoard[row][column] = 3
                                    postitions.remove(shootingTupel)
                                    #if 2 fields in one direction are hit Lock this direction
                                    if i >=2:
                                        directionLock=direction
                                    #ship is sunk
                                    if len(postitions) == 0:
                                        print("Der Computer hat ein Schiff versenkt")
                                        circularImportFixing.playerShips.remove(ship)
                                        hitStatus = 0
                                        directionLock = 0
                                    else:
                                        pass
                                    python_game.printhiddenBoard
                                else:
                                    pass
                        
                            
                        i = i+1
                        print("Der Computer schießt erneut")
                        #shootingRepeater = True
                case _:
                    print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
            python_game.printhiddenBoard(hiddenBoard)
        nextPlayer(gameMode, currentPlayer)
               
        elif currentPlayer == 2:
                shootingPosition = input("Geben sie eine Koordinate an, auf die sie schießen wollen: \n")
                row = converterfunctions.splitRow(shootingPosition)
                column = converterfunctions.splitColumnConverter(shootingPosition)
                leakedBoard = python_game.leakedBoard1
                hiddenBoard = python_game.hiddenBoard2
                if leakedBoard[row][column] == 1:
                    shootingTupel = (row, column)

                    for ship in circularImportFixing.oponentShips:
                        postitions = ship.getPosition()
                        if shootingTupel in postitions:
                            print("Das war ein Treffer! Sehr gute Arbeit")
                            hiddenBoard[row][column] = 4
                            positionMemory.append(shootingTupel)
                            ship.setPositionMemory(positionMemory)
                            postitions.remove(shootingTupel)
                            if len(postitions) == 0:
                                positionMemory = ship.getPositionMemory()
                                for tupel in positionMemory:
                                    hiddenBoard[tupel[0]][tupel[1:]] = 4
                                print("Schiff versenkt")
                                circularImportFixing.playerShips.remove(ship)

                            else:
                                pass
                            python_game.printhiddenBoard
                        else:
                            pass
                else:
                    print("Das war leider ein Wassertreffer")
                    hiddenBoard[row][column] = 3
                    python_game.printhiddenBoard
        else:
            print("Shit")
    elif gameMode == 2:
            match currentPlayer:
                case 1:
                    while shootingRepeater == True:
                        shootingPosition = input("Geben sie eine Koordinate an, auf die sie schießen wollen: \n")
                        row = converterfunctions.splitRow(shootingPosition)
                        column = converterfunctions.splitColumnConverter(shootingPosition)
                        leakedBoard = python_game.leakedBoard2
                        hiddenBoard = python_game.hiddenBoard1
                        match leakedBoard[row][column]:
                            case 1:
                                shootingTupel = (row, column)
                                #Shooting 2 Times on the same ships
                                for ship in circularImportFixing.playerShips:
                                    postitions = ship.getPosition()
                                    if shootingTupel in postitions:
                                        print("Das war ein Treffer! Sehr gute Arbeit")
                                        hiddenBoard[row][column] = 3
                                        postitions.remove(shootingTupel)
                                        if len(postitions) == 0:
                                            print("Schiff versenkt")
                                            circularImportFixing.playerShips.remove(ship)
                                        else:
                                            pass
                                        python_game.printhiddenBoard
                                    else:
                                        pass
                                print("Sie erhalten einen weiteren Schuss")
                                shootingRepeater = True
                            case 2:
                                print("Sie hatten dieses Feld bereits beschossen und einen Wassertreffer erzielt!\n Ihr Schuss liefert keine neue Erkenntnis!")
                                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                                shootingRepeater = False
                            case 3:
                                print("Sie hatten dieses Feld bereits beschossen und sogar einen Treffer erzielt!\n Ihr Schuss liefert allerdings keine neue Erkenntnis!")
                                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                                shootingRepeater = False
                            case 4:
                                print("Blubb blubb Schuss verweigert, denn hier herrscht Totenstille, Sie hatten dieses Feld bereits beschossen!\n Das Schiff an dieser Stelle ist bereits versenkt, lassen wir den Toten besser ihre verdiente Ruhe.\n Ihr Schuss liefert keine neue Erkenntnis!")
                                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                                shootingRepeater = False
                            case 0:
                                print("Das war leider ein Wassertreffer")
                                hiddenBoard[row][column] = 2
                                python_game.printhiddenBoard
                                shootingRepeater = False
                            case _:
                                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
                        python_game.printhiddenBoard(hiddenBoard)
                    nextPlayer(gameMode, currentPlayer)
       
                case 2:
                    while shootingRepeater == True:
                        shootingPosition = input("Geben sie eine Koordinate an, auf die sie schießen wollen: \n")
                        row = converterfunctions.splitRow(shootingPosition)
                        column = converterfunctions.splitColumnConverter(shootingPosition)
                        leakedBoard = python_game.leakedBoard1
                        hiddenBoard = python_game.hiddenBoard2
                        print(leakedBoard[row][column])
                        match leakedBoard[row][column]:
                            case 1:
                                shootingTupel = (row, column)
                                for ship in circularImportFixing.playerShips:
                                    postitions = ship.getPosition()
                                    if shootingTupel in postitions:
                                        print("Das war ein Treffer! Sehr gute Arbeit")
                                        hiddenBoard[row][column] = 3
                                        postitions.remove(shootingTupel)
                                        if len(postitions) == 0:
                                            print("Schiff versenkt")
                                            circularImportFixing.playerShips.remove(ship)
                                        else:
                                            pass
                                        python_game.printhiddenBoard
                                    else:
                                        pass
                                print("Sie erhalten einen weiteren Schuss")
                                shootingRepeater = True
                            case 2:
                                print("Sie hatten dieses Feld bereits beschossen und einen Wassertreffer erzielt!\n Ihr Schuss liefert keine neue Erkenntnis!")
                                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                                shootingRepeater = False
                            case 3:
                                print("Sie hatten dieses Feld bereits beschossen und sogar einen Treffer erzielt!\n Ihr Schuss liefert allerdings keine neue Erkenntnis!")
                                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                                shootingRepeater = False
                            case 4:
                                print("Blubb blubb Schuss verweigert, denn hier herrscht Totenstille, Sie hatten dieses Feld bereits beschossen!\n Das Schiff an dieser Stelle ist bereits versenkt, lassen wir den Toten besser ihre verdiente Ruhe.\n Ihr Schuss liefert keine neue Erkenntnis!")
                                print("Tipp: Waehlen Sie beim naechsten Mal Felder, die noch mit [~] markiert sind!")
                                shootingRepeater = False
                            case 0:
                                print("Das war leider ein Wassertreffer")
                                hiddenBoard[row][column] = 2 
                                python_game.printhiddenBoard
                                shootingRepeater = False
                            case 6:
                                print("Das war leider ein Wassertreffer")
                                hiddenBoard[row][column] = 2 
                                python_game.printhiddenBoard
                                shootingRepeater = False
                            case _:
                                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
                        python_game.printhiddenBoard(hiddenBoard)
                    nextPlayer(gameMode, currentPlayer)
                case _: 
                    print("something went wrong")
                
    else:
        print("Shit")



    shootingPosition = input("Geben sie eine Koordinate an, auf die sie schießen wollen")

    row = converterfunctions.splitRow(shootingPosition)
    column = converterfunctions.splitColumnConverter(shootingPosition)




# Switches the current player after each action

def nextPlayer(gameMode, currentPlayer):

    if currentPlayer == 1:
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        shooting(gameMode, currentPlayer)
        
    else:
        currentPlayer = 1
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        shooting(gameMode, currentPlayer)
