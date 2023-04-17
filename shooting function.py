import shipmanager
import main
import circularImportFixing
import converterfunctions
import python_game




def shooting(hiddenBoard, leakedBoard, gameMode, currentPlayer):  #I would remove gameMode and currentPlayer and would call the functions with other board wenn Spielverlauf
    shootingPosition = input("Geben sie eine Koordinate an, auf die sie schißen wollen")

    row = converterfunctions.splitRow(shootingPosition)
    column = converterfunctions.splitColumnConverter(shootingPosition)


    match currentPlayer:
        case 1:
            if leakedBoard[row][column] == 1:
                shootingTupel = (row, column)

                for ship in circularImportFixing.opponentShips:
                    postitions = ship.getPosition()
                    if shootingTupel in postitions:
                        print("Treffer")
                        hiddenBoard[row][column] = 4
                        postitions.remove(shootingTupel)
                        python_game.printhiddenBoard
                    else:
                        pass
            else:
                print("Wasser")
                hiddenBoard[row][column] = 3
        case 2:
            if leakedBoard[row][column] == 1:
                shootingTupel = (row, column)

                for ship in circularImportFixing.playerShips:
                    postitions = ship.getPosition()
                    if shootingTupel in postitions:
                        print("Treffer")
                        hiddenBoard[row][column] = 4
                        postitions.remove(shootingTupel)
                        python_game.printhiddenBoard
                    else:
                        pass
            else:
                print("Wasser")
                hiddenBoard[row][column] = 3
        case _: 
            print("something went wrong")




    