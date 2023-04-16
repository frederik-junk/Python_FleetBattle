import os
import outputmanager
import selectoperations
import player
import oponent
import circularImportFixing


# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))
print("Aktueller Pfad: ", path)


#this are the gameboards
letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow =   [0,0,0,0,0,0,0,0,0,0]
secondRow =  [0,0,0,0,0,0,0,0,0,0]
thirdRow =   [0,0,0,0,0,0,0,0,0,0]
fourthRow =  [0,0,0,0,0,0,0,0,0,0]
fifthRow =   [0,0,0,0,0,0,0,0,0,0]
sixthRow =   [0,0,0,0,0,0,0,0,0,0]
seventhRow = [0,0,0,0,0,0,0,0,0,0]
eighthRow =  [0,0,0,3,0,0,0,0,0,0]
ninethRow =  [0,0,0,0,0,0,0,0,0,0]
tenthRow =   [0,0,0,0,0,0,0,0,0,0]
leakedBoard1 = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]




# setting current Player to 0 to define it afterwards in function below
currentPlayer = 0

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    outputmanager.welcomeUser()
    gameMode = selectoperations.gameModeSelection()
    for ship in circularImportFixing.playerShips:
        ship.classPlaceShip(leakedBoard1, ship)
    outputmanager.battleEnd(2, gameMode)

if __name__ == "__main__":
    main()

# Switches the current player after each action
def nextPlayer():
    global currentPlayer
    if(currentPlayer == 1):
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
        player.playerAction(currentPlayer)
    else:
        currentPlayer = 1
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
        if(selectoperations.gameMode == 1):
            oponent.oponentAction()
        elif(selectoperations.gameMode == 2): 
            player.playerAction(currentPlayer)