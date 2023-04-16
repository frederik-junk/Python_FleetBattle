#creating class user to store player names
#in case of 1 player mode, computer uses player 1 as playeraccount
class User:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

#creating two instances of User
user1 = User("Spieler 1")
user2 = User("Spieler 2")

# variable that holds the game rules to print when starting the game
GAME_RULES = "Spielregeln:\n 1. Schiffe dürfen nur vertikal oder horizontal platziert werden\n 2. Schiffe dürfen sich nicht berühren \n 3. Schiffe dürfen nicht über den Rand des Spielfelds hinausgehen \n 4. Schiffe dürfen nicht übereinander platziert werden\n 5. Die Schiffe dürfen nicht über Eck gebaut sein oder Ausbuchtungen besitzen\n 6. Jeder Spieler hat 10 Schiffe\n"

#function to select the right winning/ losing informations after game has ended
def battleEnd(winID, gameMode):
    if winID == 1:
        if gameMode == 1: #computer wins the game (1 Player mode)
            loseoutput()
            print(f"{user1.getName()} hat das Spiel gewonnen. {user2.getName()} versuche es doch noch einmal!")
        else:
            winoutput() #player 1 wins the game (2 Player mode)
            print(f"Herzlichen Glueckwunsch {user1.getName()} du hast das Spiel gegen {user2.getName()} gewonnen!")
    else:
        if gameMode == 1: #player wins the game (1 Player mode)
            winoutput()
            print(f"Herzlichen Glueckwunsch {user2.getName()} du hast das Spiel gegen den Computer gewonnen!")
        else:
            winoutput() #player 2 wins the game (2 Player mode) mode
            print(f"Herzlichen Glueckwunsch {user2.getName()} du hast das Spiel gegen {user1.getName()} gewonnen!")

#function to print out the game name at beginning of the game
def welcomeUser():
    print("______________________________________________________\n")
    print(" ______ _           _     ____        _   _   _        ")
    print("|  ____| |         | |   |  _ \      | | | | | |       ")
    print("| |__  | | ___  ___| |_  | |_) | __ _| |_| |_| | ___   ")
    print("|  __| | |/ _ \/ _ \ __| |  _ < / _` | __| __| |/ _ \  ")
    print("| |    | |  __/  __/ |_  | |_) | (_| | |_| |_| |  __/  ")
    print("|_|    |_|\___|\___|\__| |____/ \__,_|\__|\__|_|\___|  ")
    print("______________________________________________________\n")

#function to print out "win" in case a user won the game (always used in 2 player mode)
def winoutput():
    print("_________________________________\n")
    print(" _____   _____   ______    _____")
    print("/ ____| |_   _| |  ____|  / ____|")
    print("| (___    | |   | |__    | |  __")
    print("\___ \    | |   |  __|   | | |_ |")
    print("____) |  _| |_  | |____  | |__| |")
    print("|_____/ |_____| |______|  \_____|")
    print("_________________________________\n")

#function to print out "lose" in case a user lost the game (only used in 1 player mode)
def loseoutput():
    print("_________________________________________________________________________________________\n")
    print(" _   _   _____   ______   _____    ______   _____    _                    _____   ______")
    print("| \ | | |_   _| |  ____| |  __ \  |  ____| |  __ \  | |          /\      / ____| |  ____|  ")
    print("|  \| |   | |   | |__    | |  | | | |__    | |__) | | |         /  \    | |  __  | |__     ")
    print("| . ` |   | |   |  __|   | |  | | |  __|   |  _  /  | |        / /\ \   | | |_ | |  __|    ")
    print("| |\  |  _| |_  | |____  | |__| | | |____  | | \ \  | |____   / ____ \  | |__| | | |____   ")
    print("|_| \_| |_____| |______| |_____/  |______| |_|  \_\ |______| /_/    \_\  \_____| |______|  ")
    print("_________________________________________________________________________________________\n")
    