import shipmanager
import main
import circularImportFixing
import converterfunctions
import python_game




def shooting(hiddenBoard, leakedBoard, gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    shootingPosition = input("Geben sie eine Koordinate an, auf die sie schießen wollen")

    row = converterfunctions.splitRow(shootingPosition)
    column = converterfunctions.splitColumnConverter(shootingPosition)


    match currentPlayer:
        case 1:
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




    