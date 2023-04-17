import python_game

#creating main class with ships
class Ships:
    def __init__(self, name, size, position, positionMemory):
        self.__name = name #ship name
        self.__size = size #size of ship
        self.__position = position #position of ship stored in touple
        self.__damageCounter = 0 #damage counter as damage indcator
        self.__positionMemory = positionMemory

    #set function to store ship postion of each ship (tupel)
    def setPosition(self,position):
        self.__position = position

    def setPositionMemory(self, positionMemory):
        self.__positionMemory = positionMemory

    #get functions to get differnet values of each ship
    def getName(self):
        return self.__name

    def getSize(self):
        return self.__size

    def getPosition(self):
        return self.__position
    
    def getpositionMemory(self):
        return self.__positionMemory

    def getDamageCounter(self):
        return self.__damageCounter

    #function to decrease ship damage counter (each hit adds 1 damage)
    def hitOnShip(self):
        self.__damageCounter += 1

    #function to call ship place function 
    def classPlaceShip(self, board, ship, counter):
         result = python_game.placeShip(board, self.getSize(), ship, self.getName(), counter)
         print(self.getPosition()) #TODO: this is a debug output can be deleted
         return result
         

#classes for each ship type with standard values
class Schlachtschiff(Ships):
        def __init__(self,position, positionMemory):
            super().__init__("Schlachtschiff(1x)", 5, position, positionMemory)

class Kreuzer(Ships):
        def __init__(self,position, positionMemory):
            super().__init__("Kreuzer(2x)", 4, position, positionMemory)

class Zerstoerer(Ships):
        def __init__(self,position, positionMemory):
            super().__init__("Zerstoerer(3x)", 3, position, positionMemory)

class Uboot(Ships):
        def __init__(self,position, positionMemory):
            super().__init__("UBoot(4x)", 2, position, positionMemory)