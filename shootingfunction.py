import shipmanager
import main
import circularImportFixing
import converterfunctions
import python_game




def shooting(gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    positionMemory = []
    if gameMode ==  1:
        if currentPlayer == 1:
            print("You have")
            #hier KI Technik
        elif currentPlayer == 2:
                leakedBoard = python_game.leakedBoard2
                hiddenBoard = python_game.hiddenBoard2
                if leakedBoard[row][column] == 1:
                    shootingTupel = (row, column)

                    for ship in circularImportFixing.playerShips:
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
                    leakedBoard = python_game.leakedBoard1
                    hiddenBoard = python_game.hiddenBoard1
                    if leakedBoard[row][column] == 1:
                        shootingTupel = (row, column)

                        for ship in circularImportFixing.opponentShips:
                            postitions = ship.getPosition()
                            if shootingTupel in postitions:
                                print("Das war ein Treffer! Sehr gute Arbeit")
                                hiddenBoard[row][column] = 4
                                postitions.remove(shootingTupel)
                                if len(postitions) == 0:
                                    print("Schiff versenkt")
                                else:
                                    pass
                                python_game.printhiddenBoard
                            else:
                                pass
                    else:
                        print("Das war leider ein Wassertreffer")
                        hiddenBoard[row][column] = 3
                        python_game.printhiddenBoard
                case 2:
                    leakedBoard = python_game.leakedBoard2
                    hiddenBoard = python_game.hiddenBoard2
                    if leakedBoard[row][column] == 1:
                        shootingTupel = (row, column)

                        for ship in circularImportFixing.playerShips:
                            postitions = ship.getPosition()
                            if shootingTupel in postitions:
                                print("Das war ein Treffer! Sehr gute Arbeit")
                                hiddenBoard[row][column] = 4
                                postitions.remove(shootingTupel)
                                if len(postitions) == 0:
                                    print("Schiff versenkt")
                                else:
                                    pass
                                python_game.printhiddenBoard
                            else:
                                pass
                    else:
                        print("Das war leider ein Wassertreffer")
                        hiddenBoard[row][column] = 3
                        python_game.printhiddenBoard
                case _: 
                    print("something went wrong")
    else:
        print("Shit")



    shootingPosition = input("Geben sie eine Koordinate an, auf die sie schießen wollen")

    row = converterfunctions.splitRow(shootingPosition)
    column = converterfunctions.splitColumnConverter(shootingPosition)




# Switches the current player after each action
"""
def nextPlayer(currentPlayer):
    print(currentPlayer)

    if currentPlayer == 1:
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        player.playerAction(currentPlayer, gameMode)
        
    else:
        currentPlayer = 1
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        print(gameMode)
        if gameMode == 1:
            oponent.oponentAction()
        else:
            player.playerAction(currentPlayer, gameMode)
"""