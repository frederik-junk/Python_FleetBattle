from python_game import placeShip



class Ships:
    def __init__(self, name, size, position):
        self.__name = name
        self.__size = size
        self.__position = position
        self.__damageCounter = 0

    def setPosition(self,position):
        self.__position = position

    def getName(self):
        return self.__name
    
    def getSize(self):
        return self.__size
    
    def getPosition(self):
        return self.__position
    
    def getDamageCounter(self):
        return self.__damageCounter
    
    def hitOnShip(self):
        self.__damageCounter += 1

    def classPlaceShip(self, board, ship):
         result = python_game.placeShip(board, self.getSize(), ship, self.getName())
         return result
         



class Schlachtschiff(Ships):
        def __init__(self,position):
            super().__init__("Schlachtschiff(1)", 5, position)

class Kreuzer(Ships):
        def __init__(self,position):
            super().__init__("Kreuzer(2)", 4, position)

class Zerstoerer(Ships):
        def __init__(self,position):
            super().__init__("Zerstoerer(3)", 3, position)

class Uboot(Ships):
        def __init__(self,position):
            super().__init__("UBoot(4)", 2, position)