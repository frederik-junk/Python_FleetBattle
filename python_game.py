letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow =   [1,1,1,0,0,0,0,0,0,0]
secondRow =  [0,0,0,0,0,0,0,0,0,0]
thirdRow =   [0,1,0,0,0,0,0,2,0,0]
fourthRow =  [0,1,0,0,2,0,0,0,0,0]
fifthRow =   [0,1,0,0,0,0,0,0,0,0]
sixthRow =   [0,0,2,0,0,0,4,0,0,0]
seventhRow = [0,0,0,0,0,0,4,0,0,0]
eighthRow =  [0,0,0,3,0,0,4,0,0,0]
ninethRow =  [0,0,0,0,0,0,0,0,0,0]
tenthRow =   [0,0,0,0,0,0,0,0,0,0]
placementBoard = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]

def printleakedBoard(board):
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        print(str(i+1).zfill(2), end="  ")
        print("  ".join(str(elem).replace("1","#").replace("0","~") for elem in row))


def printhiddenBoard(board):
    print("  ".join(letterRow))
    for i, row in enumerate(board):
        print(str(i+1).zfill(2), end="  ")
        print("  ".join(str(elem).replace("1","~").replace("0","~").replace("2","O").replace("3","x").replace("4","X") for elem in row))

printleakedBoard(placementBoard)
print(" \n")
printhiddenBoard(placementBoard)

#printPlacementBoard(placementBoard)



def placeShip(placementBoard):
    placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")
    firstChar = placementInput[0] #extrcting the first char of the users input
    restInput = placementInput[1:] #extracting the rest of the users input
    print("Der erste Buchstabe ist:", firstChar)
    print("Der Rest des Strings ist:", restInput)

#placeShip(placementBoard)
    



def winoutput():
    lineone =  [1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1]
    linetwo =  [1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0]
    linethree =[1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1]
    linefour = [0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1]
    linefive = [1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1]
    fullwordoutput = [lineone,linetwo,linethree,linefour,linefive]
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
    for i, row in enumerate(fullwordoutput):
        print("  ".join(str(elem).replace("1","#").replace("0"," ") for elem in row))
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
winoutput()

def loseoutput():
    lineone =  [1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1]
    linetwo =  [1,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0]
    linethree =[1,1,1,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1]
    linefour = [1,0,1,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0]
    linefive = [1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1]
    fullwordoutput = [lineone,linetwo,linethree,linefour,linefive]
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
    for i, row in enumerate(fullwordoutput):
        print("  ".join(str(elem).replace("1","#").replace("0"," ") for elem in row))
    print("\n")
    print(len(linefive)*"== ")
    print("\n")
loseoutput()

