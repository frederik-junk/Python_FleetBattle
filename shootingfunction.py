import os
import circularImportFixing
import converterfunctions
import python_game
import outputmanager
import random


directionLock = 0
hitStatus = 0

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')




def shooting(gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    #used for CPU
    positionMemory = []
    shootingRepeater = True
    if gameMode ==  1:
        if currentPlayer == 1:
            #loop isnt working here yet
            global hitStatus
            global directionLock
            leakedBoard = python_game.leakedBoard2
            hiddenBoard = python_game.hiddenBoard1
            #counterVariable for shooting
            i = 0
            #ship wasnt hit before
            if hitStatus == 0:
                #retundant also could use a set start worth
                row = random.randint(0,9)
                column = random.randint(0,9)
                #searching for an unshoot field
                while leakedBoard[row][column] !=0:
                    row = random.randint(0,9)
                    column = random.randint(0,9)
                shootingTupel = (row, column)
                positionMemory.append(shootingTupel)
                
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
                    row = converterfunctions.splitRow(shootingTupel)
                    column = converterfunctions.splitColumnConverter(shootingTupel)#CHECK will this work with a number?
                    shootingTupel = (row, column+i)

                    
                hitStatus = 1
            print(leakedBoard[row][column])
            match leakedBoard[row][column]:
                
                #hit water
                #is there a need for using case 6 ?
                case 0:
                             
                    print("Der Computer erzielt einen Wassertreffer")
                    hiddenBoard[row][column] = 2
                    python_game.printhiddenBoard
                    shootingRepeater = False
                    #change direction if known, but water was hit
                    if directionLock !=0:
                        match directionLock:
                            case 1: directionLock = 3
                            case 2: directionLock = 4
                            case 3: directionLock = 1
                            case 4: directionLock = 2
                        
                #hit ship
                case 1:
                    #TODO do a loop that doesnt always shoot the same field, this one shoots the same field every time
                    #while shootingRepeater == True: 
                        #determine which ship is hit
                        for ship in circularImportFixing.opponentShips:
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
                                        circularImportFixing.opponentShips.remove(ship)
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

                    for ship in circularImportFixing.playerShips:
                        postitions = ship.getPosition()
                        if shootingTupel in postitions:
                            print("Das war ein Treffer! Sehr gute Arbeit")
                            hiddenBoard[row][column] = 3
                            positionMemory.append(shootingTupel)
                            ship.setPositionMemory(positionMemory)
                            postitions.remove(shootingTupel)
                            if len(postitions) == 0:
                                positionMemory = ship.getPositionMemory()
                                for tupel in positionMemory:
                                    row, column = tupel
                                    hiddenBoard[row][column] = 4
                                print("Schiff versenkt")
                                circularImportFixing.playerShips.remove(ship)

                                if len(circularImportFixing.playerShips) == 0:
                                    winningID = 2
                                    return winningID
                                else:
                                    pass

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
                        shootingPosition = input(f"{outputmanager.user1.getName()} geben sie eine Koordinate an, auf die sie schießen wollen: \n")
                        try:
                            row = converterfunctions.splitRow(shootingPosition)
                            if row == 11:
                                raise Exception("Ihre Angabe ist fehlerhaft")
                            column = converterfunctions.splitColumnConverter(shootingPosition)
                            if column == 11:
                                raise Exception("Ihre Angabe ist fehlerhaft")
                        except Exception:
                            print("Ihre Eingabe enthaelt Fehler.\n Bitte geben Sie Buchstaben zwischen A und J ein.\n Bitte geben Sie eine Zahl zwischen 1 und 10 ein.")
                            print("Bitte geben Sie die Startposition in der Form (z.B.: A3) an.")
                            continue 
                        leakedBoard = python_game.leakedBoard2
                        hiddenBoard = python_game.hiddenBoard1
                        match leakedBoard[row][column]:
                            #hit ship
                            case 1:
                                shootingTupel = (row, column)
                                for ship in circularImportFixing.opponentShips:
                                    postitions = ship.getPosition()
                                    if shootingTupel in postitions:
                                        print("Das war ein Treffer! Sehr gute Arbeit")
                                        hiddenBoard[row][column] = 3
                                        positionMemory.append(shootingTupel)
                                        ship.setPositionMemory(positionMemory)
                                        postitions.remove(shootingTupel)
                                        if len(postitions) == 0:
                                            circularImportFixing.opponentShips.remove(ship)
                                            positionMemory = ship.getPositionMemory()
                                            for tupel in positionMemory:
                                                row, column = tupel
                                                hiddenBoard[row][column] = 4
                                            print("Schiff versenkt")
                                            if len(circularImportFixing.opponentShips) == 0:
                                                python_game.printhiddenBoard(hiddenBoard)
                                                winningID = 1
                                                return winningID
                                            else:
                                                pass
                                        else:
                                            pass
                                        python_game.printhiddenBoard
                                    else:
                                        pass
                                print("Sie erhalten einen weiteren Schuss")
                                shootingRepeater = True
                            #TODO case 2-4 funktionieren nicht weil sie in hiddenBoard stehen
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
                            #hit Water
                            case 0:
                                print("Das war leider ein Wassertreffer")
                                hiddenBoard[row][column] = 2
                                python_game.printhiddenBoard
                                shootingRepeater = False
                            case _:
                                print("Hier ist ein Fehler aufgetreten den es nicht geben kann")
                        #clearConsole()
                        python_game.printhiddenBoard(hiddenBoard)
                    nextPlayer(gameMode, currentPlayer)
       
                case 2:
                    while shootingRepeater == True:
                        shootingPosition = input(f"{outputmanager.user2.getName()} geben Sie eine Koordinate an, auf die sie schießen wollen: \n")
                        try:
                            row = converterfunctions.splitRow(shootingPosition)
                            if row == 11:
                                raise Exception("Ihre Angabe ist fehlerhaft")
                            column = converterfunctions.splitColumnConverter(shootingPosition)
                            if column == 11:
                                raise Exception("Ihre Angabe ist fehlerhaft")
                        except Exception:
                            print("Ihre Eingabe enthaelt Fehler.\n Bitte geben Sie Buchstaben zwischen A und J ein.\n Bitte geben Sie eine Zahl zwischen 1 und 10 ein.")
                            print("Bitte geben Sie die Startposition in der Form (z.B.: A3) an.")
                            continue
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
                                        positionMemory.append(shootingTupel)
                                        ship.setPositionMemory(positionMemory)
                                        postitions.remove(shootingTupel)
                                        if len(postitions) == 0:
                                            circularImportFixing.playerShips.remove(ship)
                                            positionMemory = ship.getPositionMemory()
                                            for tupel in positionMemory:
                                                row, column = tupel
                                                hiddenBoard[row][column] = 4
                                            print("Schiff versenkt")
                                            if len(circularImportFixing.playerShips) == 0:
                                                python_game.printhiddenBoard(hiddenBoard)
                                                winningID = 2
                                                return winningID
                                            else:
                                                print("wrong path") #this is a debugging output
                                                pass
                                        python_game.printhiddenBoard
                                    else:
                                        pass
                                print("Sie erhalten einen weiteren Schuss")
                                shootingRepeater = True
                            #TODO case 2-4 funktionieren nicht weil sie in hiddenBoard stehen
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
                        #clearConsole()
                        python_game.printhiddenBoard(hiddenBoard)
                    nextPlayer(gameMode, currentPlayer)

                case _: 
                    print("something went wrong")
                
    else:
        print("Shit")






# Switches the current player after each action

def nextPlayer(gameMode, currentPlayer):

    if currentPlayer == 1:
        currentPlayer = 2
        print("__________________________________\n")
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
        continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user2.getName()}  \n")
        #clearConsole()
        shooting(gameMode, currentPlayer)
        
    else:
        currentPlayer = 1
        print("__________________________________\n")
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        print("__________________________________\n")
        continueRequest = input(f"Beliebige Taste und Enter drücken um fortzufahren. Bitte uebergebe das Geraet an {outputmanager.user1.getName()}  \n")
        #clearConsole()
        shooting(gameMode, currentPlayer)
