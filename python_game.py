
letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow = ["01",1,1,0,0,0,0,0,0,0,0]
secondRow = ["02",0,0,0,0,0,0,0,0,0,0]
thirdRow = ["03",0,0,0,0,0,0,0,0,0,0]
fourthRow = ["04",0,0,0,0,0,0,0,0,0,0]
fifthRow = ["05",0,0,0,0,0,0,0,0,0,0]
sixthRow = ["06",0,0,0,0,0,0,0,0,0,0]
seventhRow = ["07",0,0,0,0,0,0,0,0,0,0]
eighthRow = ["08",0,0,0,0,0,0,0,0,0,0]
ninethRow = ["09",0,0,0,0,0,0,0,0,0,0]
tenthRow = ["10",0,0,0,0,0,0,0,0,0,0]
placementBoard = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]
probe = [[1,2,3],[5,6,7]]

        

def printPlacementBoard(placementBoard):
        
        #countingvariable for later use
        i = 0 

        #reading and printing of the first letterRow
        for element in letterRow:
            print(element, end='    ')
        print("\n")

        #auslesen und printen der spielfeldzeilen !!allerdings ist die erste Dekorspalte auch in dem Spielfeld array muss geeändert werden
        # mit offset oder so
        for row in placementBoard:
            for element in row:
                i += 1
                if i % 11 == 0:
                    #distinction in the last column
                    match element:
                        case 1: print("#", end="    ")
                        case 0: print("~", end="    ")
                    print("\n")
                #printing the other rows and columns
                elif element == 1:
                    print("#", end="    ")
                elif element == 0:
                    print("~", end="    ")
                #default case
                else:
                    print(element, end="    ")

#printPlacementBoard(placementBoard)



def placeShip(placementBoard):
    placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")
    firstChar = placementInput[0] #extrcting the first char of the users input
    restInput = placementInput[1:] #extracting the rest of the users input
    print("Der erste Buchstabe ist:", firstChar)
    print("Der Rest des Strings ist:", restInput)

placeShip(placementBoard)
    


