import os
import circularImportFixing
import converterfunctions
import python_game
import outputmanager

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')



def shooting(gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    positionMemory = []
    shootingRepeater = True
    if gameMode ==  1:
        if currentPlayer == 1:
            print("You have")
            #hier KI Technik
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
                        row = converterfunctions.splitRow(shootingPosition)
                        column = converterfunctions.splitColumnConverter(shootingPosition)
                        leakedBoard = python_game.leakedBoard2
                        hiddenBoard = python_game.hiddenBoard1
                        match leakedBoard[row][column]:
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
                                            positionMemory = ship.getPositionMemory()
                                            for tupel in positionMemory:
                                                row, column = tupel
                                                hiddenBoard[row][column] = 4
                                            print("Schiff versenkt")
                                            circularImportFixing.opponentShips.remove(ship)
                                            if len(circularImportFixing.opponentShips) == 0:
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
                        #clearConsole()
                        python_game.printhiddenBoard(hiddenBoard)
                    nextPlayer(gameMode, currentPlayer)
       
                case 2:
                    while shootingRepeater == True:
                        shootingPosition = input(f"{outputmanager.user2.getName()} geben Sie eine Koordinate an, auf die sie schießen wollen: \n")
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
                        #clearConsole()
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
