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

player_ships = [p_schlachtschiff_1, p_kreuzer_1, p_kreuzer_2, p_zerstoerer_1, p_zerstoerer_2, p_zerstoerer_3, p_uboot_1, p_uboot_2, p_uboot_3, p_uboot_4]
#player_ships = [p_schlachtschiff_1]

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

opponent_ships = [o_schlachtschiff_1, o_kreuzer_1, o_kreuzer_2, o_zerstoerer_1, o_zerstoerer_2, o_zerstoerer_3, o_uboot_1, o_uboot_2, o_uboot_3, o_uboot_4]

#opponent_ships = [o_schlachtschiff_1]


# initialize with empty List
emptyList = []
for ship in opponent_ships:
    ship.set_position_memory(emptyList)

for ship in player_ships:
    ship.set_position_memory(emptyList)
