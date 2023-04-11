
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
tenthRow = [10,0,0,0,0,0,0,0,0,0,0]
placementBoard = [firstRow, secondRow, thirdRow, fourthRow, fifthRow, sixthRow, seventhRow, eighthRow,ninethRow, tenthRow]
probe = [[1,2,3],[5,6,7]]


#for row in placementBoard:
 #   for element in row:
  #      print(element, end=' ')
        
i = 0 

for element in letterRow:
    print(element, end='    ')
print("\n")
for row in placementBoard:
    for element in row:
        i += 1
        if i % 11 == 0:
            match element:
                case 1: print("#", end="    ")
                case 0: print("~", end="    ")
            print("\n")
        elif element == 1:
            print("#", end="    ")
        elif element == 0:
            print("~", end="    ")
        else:
            print(element, end="    ")


