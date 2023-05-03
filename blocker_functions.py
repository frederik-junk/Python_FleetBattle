"""Module provides functions to make sure that ships do not collide when placing them"""


def add_placement_blocker(board, position_tupel_list):
    """Function to add blockers to prevent ship placement right next to ships

    Args:
        board (List): The board on which ships can be placed
        position_tupel_list (List): A tupel list that contains the coordinates of the ships position
    """


    for tupel in position_tupel_list:
        row_number, column_number = tupel
        # calculates positions to the left, right, top and bottom of the position
        blocker_left_number = column_number - 1
        blocker_right_number = column_number + 1
        blocker_top_number = row_number - 1
        blocker_bottom_number = row_number + 1
        # list of blocker tupels
        blocker_list = []

        # adds a blocker around each ship to avoid nearby placement of ships
        # checks if blocker is out of bounce or if there is a ship (top left corner)
        if (
            blocker_top_number < 0
            or blocker_left_number < 0
            or board[blocker_top_number][blocker_left_number] == 1
        ):
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_top_left = (blocker_top_number, blocker_left_number)
            blocker_list.append(blocker_top_left)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[blocker_top_number][blocker_left_number] = 6

        # checks if blocker is out of bounce or if there is a ship (top middle)
        if blocker_top_number < 0 or board[blocker_top_number][column_number] == 1:
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_top = (blocker_top_number, column_number)
            blocker_list.append(blocker_top)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[blocker_top_number][column_number] = 6

        # checks if blocker is out of bounce or if there is a ship (top middle)
        if (
            blocker_top_number < 0
            or blocker_right_number >= 10
            or board[blocker_top_number][blocker_right_number] == 1
        ):
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_top_right = (blocker_top_number, blocker_right_number)
            blocker_list.append(blocker_top_right)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[blocker_top_number][blocker_right_number] = 6

        # checks if blocker is out of bounce or if there is a ship (right middle)
        if blocker_right_number >= 10 or board[row_number][blocker_right_number] == 1:
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_right = (row_number, blocker_right_number)
            blocker_list.append(blocker_right)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[row_number][blocker_right_number] = 6

        # checks if blocker is out of bounce or if there is a ship (bottom right corner)
        if (
            blocker_bottom_number >= 10
            or blocker_right_number >= 10
            or board[blocker_bottom_number][blocker_right_number] == 1
        ):
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_bottom_right = (blocker_bottom_number, blocker_right_number)
            blocker_list.append(blocker_bottom_right)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[blocker_bottom_number][blocker_right_number] = 6

        # checks if blocker is out of bounce or if there is a ship (bottom middle)
        if blocker_bottom_number >= 10 or board[blocker_bottom_number][column_number] == 1:
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_bottom = (blocker_bottom_number, column_number)
            blocker_list.append(blocker_bottom)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[blocker_bottom_number][column_number] = 6

        # checks if blocker is out of bounce or if there is a ship (bottom left corner)
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
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[blocker_bottom_number][blocker_left_number] = 6

        # checks if blocker is out of bounce or if there is a ship (left middle)
        if blocker_left_number < 0 or board[row_number][blocker_left_number] == 1:
            pass
        else:
            # creates a tuple with coordinates of the new blocker, adds it to blocker_list
            blocker_left = (row_number, blocker_left_number)
            blocker_list.append(blocker_left)
            # changes id value for new blocker at position on the board (6 = placement blocker)
            board[row_number][blocker_left_number] = 6
