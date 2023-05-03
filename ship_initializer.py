"Module that initializes the ships of player and opponent"
import ship_manager

empty_tupel_list = []
VARIABLE = 0

# these are the user1 ship player or cpu
pSchlachtschiff1 = ship_manager.Schlachtschiff(empty_tupel_list, VARIABLE)

pKreuzer1 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)
pKreuzer2 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)

pZerstoerer1 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
pZerstoerer2 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
pZerstoerer3 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)

pUboot1 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
pUboot2 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
pUboot3 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
pUboot4 = ship_manager.Uboot(empty_tupel_list, VARIABLE)

# playerShips = [pSchlachtschiff1, pKreuzer1, pKreuzer2, pZerstoerer1, pZerstoerer2, pZerstoerer3, pUboot1, pUboot2, pUboot3, pUboot4]
playerShips = [pSchlachtschiff1]

# these are are the user2 ships player1 or player2
oSchlachtschiff1 = ship_manager.Schlachtschiff(empty_tupel_list, VARIABLE)

oKreuzer1 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)
oKreuzer2 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)

oZerstoerer1 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
oZerstoerer2 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
oZerstoerer3 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)

oUboot1 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
oUboot2 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
oUboot3 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
oUboot4 = ship_manager.Uboot(empty_tupel_list, VARIABLE)

# opponentShips = [oSchlachtschiff1, oKreuzer1, oKreuzer2, oZerstoerer1, oZerstoerer2, oZerstoerer3, oUboot1, oUboot2, oUboot3, oUboot4]

opponentShips = [oSchlachtschiff1]


# initialize with empty List
emptyList = []
for ship in opponentShips:
    ship.set_position_memory(emptyList)

for ship in playerShips:
    ship.set_position_memory(emptyList)
