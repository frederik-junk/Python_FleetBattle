"""Module contains the classes for each individual ship and getters / setters

Returns:
    _type_: _description_
"""
import python_game


# creating main class with ships
class Ships:
    """Class for the ships to save needed values
    """
    def __init__(self, name, size, position, position_memory):
        """Init function to set initial parameters if a new instance of ship class is made

        Args:
            name (String): The name of the ship
            size (int): The size of the ship
            position (Tuple): The position of the ship where it is located
            position_memory (_type_): _description_
        """
        self.__name = name  # ship name
        self.__size = size  # size of ship
        self.__position = position  # position of ship stored in tuple
        self.__damage_counter = 0  # damage counter as damage indcator
        self.__position_memory = position_memory

    # set function to store ship postion of each ship (tupel)
    def set_position(self, position):
        """Method for setting the position of the ship

        Args:
            position (Tuple): The position of the ship as a tuple
        """
        self.__position = position

    def set_position_memory(self, position_memory):
        """Method to fill the position memory with data

        Args:
            position_memory (_type_): _description_
        """
        self.__position_memory = position_memory

    # get functions to get differnet values of each ship
    def get_name(self):
        """Returns the name of the ship

        Returns:
            String: The name of the ship
        """
        return self.__name

    def get_size(self):
        """Method that returns the size of the ship

        Returns:
            int: The size of the ship to know which coordinates should be 
        """
        return self.__size

    def get_position(self):
        """Method that returns the saved position of the ship

        Returns:
            Tuple: The position of the ship as a tuple
        """
        return self.__position

    def get_position_memory(self):
        """Returns the position memory of a ship

        Returns:
            _type_: _description_
        """
        return self.__position_memory

    def get_damage_counter(self):
        """Returns the damage counter of a ship

        Returns:
            int: The damage points the ship has received
        """
        return self.__damage_counter

    # function to decrease ship damage counter (each hit adds 1 damage)
    def hit_on_ship(self):
        """Increases the damage counter of a ship if it has been hit
        """
        self.__damage_counter += 1

    # function to call ship place function
    def class_place_ship(self, board, ship, counter):
        """Method to place a ship on the board

        Args:
            board (List): The board on which the ship should be placed on       
            ship (Class): The class of the ship 
            counter (int): The counter to keep count on how many ships have already been placed
        """
        python_game.place_ship(board, self.get_size(), ship, self.get_name(), counter)

    def class_cpu_place_ship(self, board, ship):
        """Method to set a ship for the CPU opponent

        Args:
            board (List): The board on which the ships should be placed
            ship (Class): The type of ship which is to be placed
        """
        python_game.cpu_place_ship(board, self.get_size(), ship)


# classes for each ship type with standard values
class Schlachtschiff(Ships):
    """Individual class for Schlachtschiff to get initial name

    Args:
        Ships (Class): The super class Ships from which the methods are inherited
    """
    def __init__(self, position, position_memory):
        super().__init__("Schlachtschiff(1x)", 5, position, position_memory)


class Kreuzer(Ships):
    """Individual class for Kreuzer to get initial name

    Args:
        Ships (Class): The super class Ships from which the methods are inherited
    """
    def __init__(self, position, position_memory):
        super().__init__("Kreuzer(2x)", 4, position, position_memory)


class Zerstoerer(Ships):
    """Individual class for Zerstörer to get initial name

    Args:
        Ships (Class): The super class Ships from which the methods are inherited
    """
    def __init__(self, position, position_memory):
        super().__init__("Zerstoerer(3x)", 3, position, position_memory)


class Uboot(Ships):
    """Individual class for UBoot to get initial name

    Args:
        Ships (Class): The super class Ships from which the methods are inherited
    """
    def __init__(self, position, position_memory):
        super().__init__("UBoot(4x)", 2, position, position_memory)
