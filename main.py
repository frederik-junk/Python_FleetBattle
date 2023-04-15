import os
import outputmanager
import selectoperations

# extracting current Path for optimal usage on Windows and Linux systems
path = os.path.dirname(os.path.abspath(__file__))
print("Aktueller Pfad: ", path)


# setting current Player to 0 to define it afterwards in function below
currentPlayer = 0

# Switches the current player after each action
def nextPlayer():
    global currentPlayer
    if(currentPlayer == 1):
        currentPlayer = 2
        print(f"{outputmanager.user2.getName()} ist nun an der Reihe.")
    else:
        currentPlayer = 1
        print(f"{outputmanager.user1.getName()} ist nun an der Reihe.")
    return currentPlayer

# Holds the logic of the game. Welcomes the user, asks for game mode selection and navigates through the game
def main():
    outputmanager.welcomeUser()
    gameMode = selectoperations.gameModeSelection()
    outputmanager.battleEnd(2, gameMode)

if __name__ == "__main__":
    main()
