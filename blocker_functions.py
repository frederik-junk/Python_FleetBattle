"""Module provides the functions to make sure that ships do not collide when placing them
"""


def add_placement_blocker(board, position_tupel_list):
    """Function to add the blockers so that ships cant be placed next to the ship

    Args:
        board (List): The board on which ships can be placed
        position_tupel_list (List): A tupel list that contains the coordinates of the ships position
    """
    for tupel in position_tupel_list:
        row_number, column_number = tupel
        # calculate the positions left, right, top and bottom of the position
        blocker_left_number = column_number - 1
        blocker_right_number = column_number + 1
        blocker_top_number = row_number - 1
        blocker_bottom_number = row_number + 1
        # list in which the blocker tupels are saved
        blocker_list = []

        # adding a blocker around each ship psotiob to avoid nearby placning of ships
        # proving if the blocker is out of bounce or if there is a ship (top left corner)
        if (
            blocker_top_number < 0
            or blocker_left_number < 0
            or board[blocker_top_number][blocker_left_number] == 1
        ):
            pass
        else:
            # creating a tuple with cordinates of the new blocker and add to list
            blocker_top_left = (blocker_top_number, blocker_left_number)
            blocker_list.append(blocker_top_left)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blocker_top_number][blocker_left_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (top middle)
        if blocker_top_number < 0 or board[blocker_top_number][column_number] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker  and adding it to the list
            blocker_top = (blocker_top_number, column_number)
            blocker_list.append(blocker_top)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blocker_top_number][column_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (top right corner)
        if (
            blocker_top_number < 0
            or blocker_right_number >= 10
            or board[blocker_top_number][blocker_right_number] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker  and adding it to the list
            blocker_top_right = (blocker_top_number, blocker_right_number)
            blocker_list.append(blocker_top_right)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blocker_top_number][blocker_right_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (right middle)
        if blocker_right_number >= 10 or board[row_number][blocker_right_number] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blocker_right = (row_number, blocker_right_number)
            blocker_list.append(blocker_right)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[row_number][blocker_right_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (bottom right corner)
        if (
            blocker_bottom_number >= 10
            or blocker_right_number >= 10
            or board[blocker_bottom_number][blocker_right_number] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blocker_bottom_right = (blocker_bottom_number, blocker_right_number)
            blocker_list.append(blocker_bottom_right)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blocker_bottom_number][blocker_right_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (bottom middle)
        if blocker_bottom_number >= 10 or board[blocker_bottom_number][column_number] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blocker_bottom = (blocker_bottom_number, column_number)
            blocker_list.append(blocker_bottom)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blocker_bottom_number][column_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (bottom left corner)
        if (
            blocker_bottom_number >= 10
            or blocker_left_number < 0
            or board[blocker_bottom_number][blocker_left_number] == 1
        ):
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blocker_bottom_left = (blocker_bottom_number, blocker_left_number)
            blocker_list.append(blocker_bottom_left)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[blocker_bottom_number][blocker_left_number] = 6

        # proving if the blocker is out of bounce or if there is a ship (left middle)
        if blocker_left_number < 0 or board[row_number][blocker_left_number] == 1:
            pass
        else:
            # creating a tuple containing the cordinates of the new blocker and adding it to the list
            blocker_left = (row_number, blocker_left_number)
            blocker_list.append(blocker_left)
            # changing the id value for the new blocker psotion in the board (6 = placement blocker)
            board[row_number][blocker_left_number] = 6
