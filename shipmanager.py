import python_game

#creating main class with ships
class Ships:
    def __init__(self, name, size, position):
        self.__name = name #ship name
        self.__size = size #size of ship
        self.__position = position #position of ship stored in touple
        self.__damageCounter = 0 #damage counter as damage indcator

    #set function to store ship postion of each ship (tupel)
    def setPosition(self,position):
        self.__position = position

    #get functions to get differnet values of each ship
    def getName(self):
        return self.__name

    def getSize(self):
        return self.__size

    def getPosition(self):
        return self.__position

    def getDamageCounter(self):
        return self.__damageCounter

    #function to decrease ship damage counter (each hit adds 1 damage)
    def hitOnShip(self):
        self.__damageCounter += 1

    #function to call ship place function 
    def classPlaceShip(self, board, ship, counter):
         result = python_game.placeShip(board, self.getSize(), ship, self.getName(), counter)
         print(self.getPosition())
         return result
         

#classes for each ship type with standard values
class Schlachtschiff(Ships):
        def __init__(self,position):
            super().__init__("Schlachtschiff(1x)", 5, position)

class Kreuzer(Ships):
        def __init__(self,position):
            super().__init__("Kreuzer(2x)", 4, position)

class Zerstoerer(Ships):
        def __init__(self,position):
            super().__init__("Zerstoerer(3x)", 3, position)

class Uboot(Ships):
        def __init__(self,position):
            super().__init__("UBoot(4x)", 2, position)