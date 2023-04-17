import shipmanager
import main
import circularImportFixing
import converterfunctions
import python_game




def shooting(gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    shootingPosition = input("Geben sie eine Koordinate an, auf die sie schißen wollen")

    row = converterfunctions.splitRow(shootingPosition)
    column = converterfunctions.splitColumnConverter(shootingPosition)


    match currentPlayer:
        case 1:
            leakedBoard = python_game.leakedBoard1
            hiddenBoard = python_game.hiddenBoard1
            if leakedBoard[row][column] == 1:
                shootingTupel = (row, column)

                for ship in circularImportFixing.opponentShips:
                    postitions = ship.getPosition()
                    if shootingTupel in postitions:
                        print("Treffer")
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
                print("Wasser")
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
                        print("Treffer")
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
                print("Wasser")
                hiddenBoard[row][column] = 3
                python_game.printhiddenBoard
        case _: 
            print("something went wrong")




    