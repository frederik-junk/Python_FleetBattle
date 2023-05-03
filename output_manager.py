"""
Module contains graphic elements for user interface and messages that are displayed if a game is over

Returns:
    _type_: _description_
"""
from termcolor import colored
from colorama import init

init(autoreset=True)


# creating class user to store player names
# in case of 1 player mode, computer uses player 1 as playeraccount
class User:
    """Class for storing Username of the players
    """
    def __init__(self, name, cpu_memory, first_cpu_memory, shooting_iq, direction):
        """Init function for setting initial values

        Args:
            name (String): The name of the user
            cpu_memory (tuple): The memorized positions for the CPU
            first_cpu_memory (_type_): _description_
            shooting_iq (_type_): _description_
            direction (int): An int value to indicate the direction that the cpu should shoot at
        """
        self.__name = name
        self.__leftships = 0
        self.__cpu_memory = cpu_memory
        self.__first_cpu_memory = first_cpu_memory
        self.__shooting_iq = shooting_iq
        self.__direction = direction

    def get_name(self):
        """Returns the name of the user

        Returns:
            String: Returns the name of the user
        """
        return self.__name

    def set_name(self, name):
        """Sets the player name

        Args:
            name (String): The name of the player
        """
        self.__name = name

    def get_left_ships(self):
        """Returns amount of left ships

        Returns:
            String: Returns the Amount of left ships
        """
        return self.__leftships

    def increase_left_ships(self):
        """decreases the amount of left ships

        Args:
            leftships (Int): Amount of left ships of player
        """
        self.__leftships += 1

    def set_left_ships(self, leftships):
        """Sets the amount of left ships

        Args:
            leftships (Int): Amount of left ships of player
        """
        self.__leftships = leftships


    def get_cpu_memory(self):
        """Returns the cpu memory

        Returns:
            _type_: _description_
        """
        return self.__cpu_memory

    def set_cpu_memory(self, cpu_memory):
        """Sets the cpu memory

        Args:
            cpu_memory (_type_): _description_
        """
        self.__cpu_memory = cpu_memory


    def get_first_cpu_memory(self):
        """Returns the first data of the cpu memory

        Returns:
            _type_: _description_
        """
        return self.__first_cpu_memory

    def set_first_cpu_memory(self, first_cpu_memory):
        """Sets the first component of the cpu memory

        Args:
            first_cpu_memory (_type_): _description_
        """
        self.__first_cpu_memory = first_cpu_memory


    def get_shooting_iq(self):
        """Function that returns the shooting iq of the CPU player

        Returns:
            _type_: _description_
        """
        return self.__shooting_iq

    def set_shooting_iq(self, shooting_iq):
        """Sets the shooting iq for the CPU player

        Args:
            shooting_iq (_type_): _description_
        """
        self.__shooting_iq = shooting_iq


    def get_direction(self):
        """Returns the direction in which the cpu player takes hit shots

        Returns:
            _type_: _description_
        """
        return self.__direction

    def set_direction(self, direction):
        """Sets the direction value in which the cpu player takes his shots

        Args:
            direction (_type_): _description_
        """
        self.__direction = direction


# creating two instances of User
user_1 = User("Spieler 1", (0, 0), (0, 0), 0, 0)
user_2 = User("Spieler 2", (0, 0), (0, 0), 0, 0)

# variable that holds the game rules to print when starting the game
GAME_RULES1 = "Spielregeln:\n 1. Schiffe dürfen nur vertikal oder horizontal platziert werden"
GAME_RULES2 = " 2. Schiffe dürfen sich nicht berühren \n 3. Schiffe dürfen nicht über den Rand des Spielfelds hinausgehen"
GAME_RULES3 = " 4. Schiffe dürfen nicht übereinander platziert werden"
GAME_RULES4 = " 5. Die Schiffe dürfen nicht über Eck gebaut sein oder Ausbuchtungen besitzen\n 6. Jeder Spieler hat 10 Schiffe\n"

#function to select the right winning/ losing informations after game has ended
def battle_end(winning_id, game_mode):
    """Function that prints a message after a game is over

    Args:
        winID (int): a number that indicates which player has won the game
        game_mode (int): the game mode in which has been played to indicate if the computer played or two humans
    """
    match winning_id:
        case 1:
            if game_mode == 1: #computer wins the game (1 Player mode)
                lose_output()
                print(colored(f"{user_1.get_name()} hat das Spiel gewonnen. {user_2.get_name()} versuche es doch noch einmal!",'magenta'))
            else:
                win_output() #player 1 wins the game (2 Player mode)
                print(colored(f"Herzlichen Glueckwunsch {user_1.get_name()} du hast das Spiel gegen {user_2.get_name()} gewonnen!",'green'))
        case 2:
            if game_mode == 1: #player wins the game (1 Player mode)
                win_output()
                print(colored(f"Herzlichen Glueckwunsch {user_2.get_name()} du hast das Spiel gegen den Computer gewonnen!",'green'))
            else:
                win_output() #player 2 wins the game (2 Player mode) mode
                print(colored(f"Herzlichen Glueckwunsch {user_2.get_name()} du hast das Spiel gegen {user_1.get_name()} gewonnen!",'green'))
        case _:
            win_output()
            print(colored("Herzlichen Glueckwunsch du hast gewonnen!",'green'))


    #win_output()
    #print(colored(f"Herzlichen Glueckwunsch {winning_id} du hast gewonnen",'green'))




def welcome_user():
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

def win_output():
    """function to print out "win" in case a user won the game (always used in 2 player mode)
    """
    print("_________________________________\n")
    print(colored(" _____   _____   ______    _____", "green"))
    print(colored("/ ____| |_   _| |  ____|  / ____|", "green"))
    print(colored("| (___    | |   | |__    | |  __", "green"))
    print(colored("\___ \    | |   |  __|   | | |_ |", "green"))
    print(colored("____) |  _| |_  | |____  | |__| |", "green"))
    print(colored("|_____/ |_____| |______|  \_____|", "green"))
    print("_________________________________\n")

def lose_output():
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
