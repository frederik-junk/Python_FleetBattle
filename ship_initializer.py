"Module that initializes the ships of player and opponent"
import ship_manager

empty_tupel_list = []
VARIABLE = 0

# these are the user1 ship player or cpu
p_schlachtschiff_1 = ship_manager.Schlachtschiff(empty_tupel_list, VARIABLE)

p_kreuzer_1 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)
p_kreuzer_2 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)

p_zerstoerer_1 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
p_zerstoerer_2 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
p_zerstoerer_3 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)

p_uboot_1 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
p_uboot_2 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
p_uboot_3 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
p_uboot_4 = ship_manager.Uboot(empty_tupel_list, VARIABLE)

# playerShips = [pSchlachtschiff1, pKreuzer1, pKreuzer2, pZerstoerer1, pZerstoerer2, pZerstoerer3, pUboot1, pUboot2, pUboot3, pUboot4]
player_ships = [p_schlachtschiff_1]

# these are are the user2 ships player1 or player2
o_schlachtschiff_1 = ship_manager.Schlachtschiff(empty_tupel_list, VARIABLE)

o_kreuzer_1 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)
o_kreuzer_2 = ship_manager.Kreuzer(empty_tupel_list, VARIABLE)

o_zerstoerer_1 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
o_zerstoerer_2 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)
o_zerstoerer_3 = ship_manager.Zerstoerer(empty_tupel_list, VARIABLE)

o_uboot_1 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
o_uboot_2 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
o_uboot_3 = ship_manager.Uboot(empty_tupel_list, VARIABLE)
o_uboot_4 = ship_manager.Uboot(empty_tupel_list, VARIABLE)

# opponentShips = [oSchlachtschiff1, oKreuzer1, oKreuzer2, oZerstoerer1, oZerstoerer2, oZerstoerer3, oUboot1, oUboot2, oUboot3, oUboot4]

opponent_ships = [o_schlachtschiff_1]


# initialize with empty List
emptyList = []
for ship in opponent_ships:
    ship.set_position_memory(emptyList)

for ship in player_ships:
    ship.set_position_memory(emptyList)
