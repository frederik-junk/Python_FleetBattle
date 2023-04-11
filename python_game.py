
letterRow = ["\\\\","A","B","C","D","E","F","G","H","I","J"]
firstRow = ["01",0,0,0,0,0,0,0,0,0,0]
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

        
#function to print the placement board
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


shipLength = int(2)



# function to place a ship in the right position with the right length and the right direction
def placeShip(placementBoard, shipLength):
    placementInput = input("Geben sie eine Koordinate an, auf die die Spitze des Schiffs platziert werden soll.\n")

    #splitting the input into the column and row indices 
    startingColumnChar = placementInput[0] #extrcting the first char of the users input
    startingRowNumber = placementInput[1:] #extracting the rest of the users input
    print("Der erste Buchstabe ist:", startingColumnChar)    #diese ausgabe kann entfernt werden
    print("Der Rest des Strings ist:", startingRowNumber) #diese ausgabe kann entfernt werden

    #match case to convert the letters into column idexes
    match startingColumnChar:
        case "A": startingColumnChar = 0
        case "B": startingColumnChar = 1
        case "C": startingColumnChar = 2
        case "D": startingColumnChar = 3
        case "E": startingColumnChar = 4
        case "F": startingColumnChar = 5
        case "G": startingColumnChar = 6
        case "H": startingColumnChar = 7
        case "I": startingColumnChar = 8
        case "J": startingColumnChar = 9
        case _: print("Bitte geben sie Buchstaben zwischen A und J ein")
    
    #adding one for the correct alignment still needs fixes
    startingRowNumber = int(startingRowNumber) - 1
    startingColumnChar = int(startingColumnChar) + 1
    #putting the 1 in the right position
    placementBoard[startingRowNumber][startingColumnChar] = 1

    printPlacementBoard(placementBoard)


    
    #asking the direction of the ship
    directionInput = input("Geben sie über w,a,s,d die Ausrichtung des Schiffes an.\n")
    j = 0 # just a counting variable for later use
    match directionInput:

        case "w": 
            #changin every index between the beginning and the end to a 1
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingRowNumber = startingRowNumber - 1
                j += 1

        case "a": 
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingColumnChar -= 1
                j += 1

        case "s": 
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingRowNumber += 1
                j += 1

        case "d": 
            while j < shipLength:
                placementBoard[startingRowNumber][startingColumnChar] = 1
                startingColumnChar += 1
                j += 1

        case _: print("Bitte bestimmen sie mithilfe von w,a,s,d die Ausrichtung des Schiffes. In Kleinbuchstaben")
    
    printPlacementBoard(placementBoard)



placeShip(placementBoard, shipLength)

    
    

