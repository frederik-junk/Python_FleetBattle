from typing import Any
"""Module contains graphic elements for user interface and messages that are displayed if a game is over

Returns:
    _type_: _description_
"""
from termcolor import colored
from colorama import init
init()

#creating class user to store player names
#in case of 1 player mode, computer uses player 1 as playeraccount
class User:
    """Class for storing Username of the players
    """
    def __init__(self, name, cpuMemory, firstCpuMemory, shootingIq, direction):
        self.__name = name
        self.__leftships = 0
        self.__cpuMemory = cpuMemory
        self.__firstCpuMemory = firstCpuMemory
        self.__shootingIq = shootingIq
        self.__direction = direction

    def getName(self):
        """Returns the name of the user

        Returns:
            String: Returns the name of the user
        """
        return self.__name

    def setName(self, name):
        """Sets the player name

        Args:
            name (String): The name of the player
        """
        self.__name = name

    def getLeftShips(self):
        """Returns amount of left ships

        Returns:
            String: Returns the Amount of left ships
        """
        return self.__leftships

    def increaseLeftShips(self):
        """decreases the amount of left ships

        Args:
            leftships (Int): Amount of left ships of player
        """
        self.__leftships += 1

    def setLeftShips(self, leftships):
        """Sets the amount of left ships

        Args:
            leftships (Int): Amount of left ships of player
        """
        self.__leftships = leftships


    def getCpuMemory(self):
        return self.__cpuMemory
    
    def setCpuMemory(self, cpuMemory):
        self.__cpuMemory = cpuMemory


    def getFirstCpuMemory(self):
        return self.__firstCpuMemory
    
    def setFirstCpuMemory(self, firstCpuMemory):
        self.__firstCpuMemory = firstCpuMemory


    def getShootingIq(self):
        return self.__shootingIq
    
    def setShootingIq(self, shootingIq):
        self.__shootingIq = shootingIq


    def getDirection(self):
        return self.__direction
    
    def setDirection(self, direction):
        self.__direction = direction



#creating two instances of User
user1 = User("Spieler 1", (0,0), (0,0), 0, 0)
user2 = User("Spieler 2", (0,0), (0,0), 0, 0)

# variable that holds the game rules to print when starting the game
GAME_RULES = "Spielregeln:\n 1. Schiffe dürfen nur vertikal oder horizontal platziert werden\n 2. Schiffe dürfen sich nicht berühren \n 3. Schiffe dürfen nicht über den Rand des Spielfelds hinausgehen \n 4. Schiffe dürfen nicht übereinander platziert werden\n 5. Die Schiffe dürfen nicht über Eck gebaut sein oder Ausbuchtungen besitzen\n 6. Jeder Spieler hat 10 Schiffe\n"

#function to select the right winning/ losing informations after game has ended
def battleEnd(winningID, gameMode):
    """Function that prints a message after a game is over

    Args:
        winID (int): a number that indicates which player has won the game
        gameMode (int): the game mode in which has been played to indicate if the computer played or two humans
    """
    match winningID:
        
        case 1:
            if gameMode == 1: #computer wins the game (1 Player mode)
                loseoutput()
                print(colored(f"{user1.getName()} hat das Spiel gewonnen. {user2.getName()} versuche es doch noch einmal!",'magenta'))
            else:
                winoutput() #player 1 wins the game (2 Player mode)
                print(colored(f"Herzlichen Glueckwunsch {user1.getName()} du hast das Spiel gegen {user2.getName()} gewonnen!",'green'))
        case 2:
            if gameMode == 1: #player wins the game (1 Player mode)
                winoutput()
                print(colored(f"Herzlichen Glueckwunsch {user2.getName()} du hast das Spiel gegen den Computer gewonnen!",'green'))
            else:
                winoutput() #player 2 wins the game (2 Player mode) mode
                print(colored(f"Herzlichen Glueckwunsch {user2.getName()} du hast das Spiel gegen {user1.getName()} gewonnen!",'green'))
        case _:
            print("this is a fault")
    

    #winoutput()
    #print(colored(f"Herzlichen Glueckwunsch {winningID} du hast gewonnen",'green'))


    

def welcomeUser():
    """function to print out the game name at beginning of the game
    """
    print(colored("______________________________________________________\n",'cyan',attrs=["blink"]))
    print(colored(" ______ _           _     ____        _   _   _        ",'cyan',attrs=["blink"]))
    print(colored("|  ____| |         | |   |  _ \      | | | | | |       ",'cyan',attrs=["blink"]))
    print(colored("| |__  | | ___  ___| |_  | |_) | __ _| |_| |_| | ___   ",'cyan',attrs=["blink"]))
    print(colored("|  __| | |/ _ \/ _ \ __| |  _ < / _` | __| __| |/ _ \  ",'cyan',attrs=["blink"]))
    print(colored("| |    | |  __/  __/ |_  | |_) | (_| | |_| |_| |  __/  ",'cyan',attrs=["blink"]))
    print(colored("|_|    |_|\___|\___|\__| |____/ \__,_|\__|\__|_|\___|  ",'cyan',attrs=["blink"]))
    print(colored("______________________________________________________\n",'cyan',attrs=["blink"]))

def winoutput():
    """function to print out "win" in case a user won the game (always used in 2 player mode)
    """
    print("_________________________________\n")
    print(colored(" _____   _____   ______    _____",'green'))
    print(colored("/ ____| |_   _| |  ____|  / ____|",'green'))
    print(colored("| (___    | |   | |__    | |  __",'green'))
    print(colored("\___ \    | |   |  __|   | | |_ |",'green'))
    print(colored("____) |  _| |_  | |____  | |__| |",'green'))
    print(colored("|_____/ |_____| |______|  \_____|",'green'))
    print("_________________________________\n")

def loseoutput():
    """function to print out "lose" in case a user lost the game (only used in 1 player mode)
    """
    print("_________________________________________________________________________________________\n")
    print(colored(" _   _   _____   ______   _____    ______   _____    _                    _____   ______",'red'))
    print(colored("| \ | | |_   _| |  ____| |  __ \  |  ____| |  __ \  | |          /\      / ____| |  ____|  ",'red'))
    print(colored("|  \| |   | |   | |__    | |  | | | |__    | |__) | | |         /  \    | |  __  | |__     ",'red'))
    print(colored("| . ` |   | |   |  __|   | |  | | |  __|   |  _  /  | |        / /\ \   | | |_ | |  __|    ",'red'))
    print(colored("| |\  |  _| |_  | |____  | |__| | | |____  | | \ \  | |____   / ____ \  | |__| | | |____   ",'red'))
    print(colored("|_| \_| |_____| |______| |_____/  |______| |_|  \_\ |______| /_/    \_\  \_____| |______|  ",'red'))
    print("_________________________________________________________________________________________\n")
    