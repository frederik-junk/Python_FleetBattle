class User:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

user1 = User("Spieler 1")
user2 = User("Spieler 2")
def welcomeUser():
    print("______________________________________________________\n")
    print(" ______ _           _     ____        _   _   _        ")
    print("|  ____| |         | |   |  _ \      | | | | | |       ")
    print("| |__  | | ___  ___| |_  | |_) | __ _| |_| |_| | ___   ")
    print("|  __| | |/ _ \/ _ \ __| |  _ < / _` | __| __| |/ _ \  ")
    print("| |    | |  __/  __/ |_  | |_) | (_| | |_| |_| |  __/  ")
    print("|_|    |_|\___|\___|\__| |____/ \__,_|\__|\__|_|\___|  ")
    print("______________________________________________________\n")

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

def winoutput():
    print("_________________________________\n")
    print(" _____   _____   ______    _____")
    print("/ ____| |_   _| |  ____|  / ____|")     
    print("| (___    | |   | |__    | |  __")     
    print("\___ \    | |   |  __|   | | |_ |")     
    print("____) |  _| |_  | |____  | |__| |")     
    print("|_____/ |_____| |______|  \_____|")
    print("_________________________________\n")

def loseoutput():
    print("_________________________________________________________________________________________\n")
    print(" _   _   _____   ______   _____    ______   _____    _                    _____   ______")   
    print("| \ | | |_   _| |  ____| |  __ \  |  ____| |  __ \  | |          /\      / ____| |  ____|  ")
    print("|  \| |   | |   | |__    | |  | | | |__    | |__) | | |         /  \    | |  __  | |__     ")
    print("| . ` |   | |   |  __|   | |  | | |  __|   |  _  /  | |        / /\ \   | | |_ | |  __|    ")
    print("| |\  |  _| |_  | |____  | |__| | | |____  | | \ \  | |____   / ____ \  | |__| | | |____   ")
    print("|_| \_| |_____| |______| |_____/  |______| |_|  \_\ |______| /_/    \_\  \_____| |______|  ")
    print("_________________________________________________________________________________________\n")