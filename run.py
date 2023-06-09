import random


"""
Main variables of the Game

"""
user_name = input("please enter you name to start game:")
grid_w = [".", ".", ".", "."]
grid_x = [".", ".", ".", "."]
grid_y = [".", ".", ".", "."]
grid_z = [".", ".", ".", "."]
grid_a = [".", ".", ".", "."]
grid_b = [".", ".", ".", "."]
grid_c = [".", ".", ".", "."]
grid_d = [".", ".", ".", "."]
previous_input_user = []
previous_input_computer = []
user_ship = 4
computer_ship = 4
user_score = 0
computer_score = 0


class Welcome:

    """
    Class to print the welcome message to the player

    """
    def welcome_message(self):
        return ("--------------------------------\n"
                "Welcome to Ultimate BATTLESHIPS!!\n"
                "Board Size: 4 Number of ships: 4\n"
                "Top left corner is row:1, col:1\n"
                "-------------------------------")


def create_grid_user():

    """
    This function is used to build the User grid on the consol

    """

    for x in range(len(grid_w)):

        print(grid_w[x], end=" ")
        print(grid_x[x], end=" ")
        print(grid_y[x], end=" ")
        print(grid_z[x], end=" ")
        print(" ")


def create_grid_computer():

    """
     This function is used to build the computer grid on the consol

    """

    grid_e = [".", ".", ".", "."]
    grid_f = [".", ".", ".", "."]
    grid_g = [".", ".", ".", "."]
    grid_h = [".", ".", ".", "."]

    for x in range(len(grid_e)):

        print(grid_e[x], end=" ")
        print(grid_f[x], end=" ")
        print(grid_g[x], end=" ")
        print(grid_h[x], end=" ")
        print(" ")


def set_ship_location_computer():

    """
    This function is used to set the location of the user ship in the grid

    """
    global grid_w
    grid_w = [".", ".", ".", "."]
    global grid_x
    grid_x = [".", ".", ".", "."]
    global grid_y
    grid_y = [".", ".", ".", "."]
    global grid_z
    grid_z = [".", ".", ".", "."]
    print(f'Welcome {user_name}')
    w_1 = random.randrange(3)
    x_1 = random.randrange(3)
    y_1 = random.randrange(3)
    z_1 = random.randrange(3)
    grid_w[w_1] = "@"
    grid_x[x_1] = "@"
    grid_y[y_1] = "@"
    grid_z[z_1] = "@"


def set_ship_location_user():

    """
    This function is used to set the location of the computer ship in the grid

    """
    global grid_a
    grid_a = [".", ".", ".", "."]
    global grid_b
    grid_b = [".", ".", ".", "."]
    global grid_c
    grid_c = [".", ".", ".", "."]
    global grid_d
    grid_d = [".", ".", ".", "."]

    w_1 = random.randrange(3)
    x_1 = random.randrange(3)
    y_1 = random.randrange(3)
    z_1 = random.randrange(3)
    grid_a[w_1] = "@"
    grid_b[x_1] = "@"
    grid_c[y_1] = "@"
    grid_d[z_1] = "@"


def get_user_targets():

    """
    This function is used to get the user input Targets
    and check the availability with the game rules

    """
    global previous_input_user

    try:
        y_axis = int(input("please enter the column no:"))
        x_axis = int(input("please enter the row no:"))

        while y_axis > 4 and x_axis > 4:
            y_axis = int(input("please enter number between (1 & 4):"))
            x_axis = int(input("please enter number between (1 & 4):"))
        if previous_input_user == []:
            previous_input_user.append((y_axis, x_axis))

        else:

            for x in range(len(previous_input_user)):

                while previous_input_user[x] == (y_axis, x_axis):
                    print("please enter new set of coordinates:")
                    y_axis = int(input("please enter a new column no:"))
                    x_axis = int(input("please enter a new row no:"))

            else:
                previous_input_user.append((y_axis, x_axis))
                previous_input_user = list(dict.fromkeys(previous_input_user))

    except ValueError:
        try:
            y_axis = int(input("please enter an integer no:"))
            x_axis = int(input("please enter an integer no:"))
        except ValueError:
            run_game()

    return y_axis, x_axis


def get_computer_targets():

    """
    This function is used to get the random computer input Targets
    and check the availability with the game rules
    and append them to save computer input targets.

    """
    global previous_input_computer
    previous_input_computer = []
    y_axis = random.randrange(1, 4)
    x_axis = random.randrange(1, 4)
    previous_input_computer.append((y_axis, x_axis))
    return y_axis, x_axis


def remove_ship_from_score_user():
    """
    This function is used to reduce the amount of ships if the ships get hit
    """
    global user_ship
    user_ship -= 1


def remove_ship_from_score_computer():

    """
    This function is used to reduce the amount of ships if the ships get hit
    """
    global computer_ship
    computer_ship -= 1


def update_the_score_computer():

    """
    This function is used to update the score in the case of hitting the Target

    """
    global computer_score
    computer_score += 1


def update_the_score_user():

    """
    This function is used to update the score in the case of hitting the Target

    """
    global user_score
    user_score += 1


def compare_computer_hit_with_ship_location():

    """
    This function is used to to compare the input hits with the ship locations
    it reduces the number of ships if hiy happened and increment the score
    """
    y, x = get_computer_targets()
    if y == 1 and x == 1 and grid_w[0] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 1 and x == 2 and grid_w[1] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 1 and x == 3 and grid_w[2] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 1 and x == 4 and grid_w[3] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 2 and x == 1 and grid_x[0] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 2 and x == 2 and grid_x[1] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 2 and x == 3 and grid_x[2] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 2 and x == 4 and grid_x[3] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 3 and x == 1 and grid_y[0] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 3 and x == 2 and grid_y[1] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 3 and x == 3 and grid_y[2] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 3 and x == 4 and grid_y[3] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 4 and x == 1 and grid_z[0] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 4 and x == 2 and grid_z[1] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif (y == 4 and x == 3 and grid_z[2] == "@"):
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()
    elif y == 4 and x == 4 and grid_z[3] == "@":
        print("Computer hit the Target")
        remove_ship_from_score_computer()
        update_the_score_computer()

    else:
        print("Computer missed the Target")


def compare_user_hit_with_ship_location():

    """
    This function is used to to compare the input hits with the ship locations
    it reduces the number of ships if hiy happened and increment the score

    """
    y, x = get_user_targets()
    if y == 1 and x == 1 and grid_a[0] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 1 and x == 2 and grid_a[1] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 1 and x == 3 and grid_a[2] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 1 and x == 4 and grid_a[3] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 2 and x == 1 and grid_b[0] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 2 and x == 2 and grid_b[1] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 2 and x == 2 and grid_b[2] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 2 and x == 4 and grid_b[3] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 3 and x == 1 and grid_c[0] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 3 and x == 2 and grid_c[1] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 3 and x == 3 and grid_c[2] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 3 and x == 4 and grid_c[3] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 4 and x == 1 and grid_d[0] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 4 and x == 2 and grid_d[1] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif (y == 4 and x == 3 and grid_d[2] == "@"):
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()
    elif y == 4 and x == 4 and grid_d[3] == "@":
        print(f"Congratulate {user_name} you hit the Target")
        remove_ship_from_score_user()
        update_the_score_user()

    else:
        print(f"Sorry {user_name} you missed Target")


def run_game():

    """
    This is the Main function for the Game, it sets the locations of the
    ships and create the boards of both contestants,
    it stays in a loop during the game time until all
    the ships of one of the contestant is gone.
    Then at the end of the game it prints who win the game.

    """

    set_ship_location_user()
    set_ship_location_computer()
    print(f"----{user_name} Battle Board------")
    create_grid_user()
    print(f"----Computer Battle Board------")
    create_grid_computer()
    while user_ship != 0 and computer_ship != 0:
        print(f"---------------New Round---------------")
        print(f"USER_SCORE:{user_score}")
        print(f"Computer_SCORE:{computer_score}")
        print(f"Input_Coordinates_User:{previous_input_user}")
        print(f"Input_Coordinates_Computer {previous_input_computer}")
        compare_user_hit_with_ship_location()
        compare_computer_hit_with_ship_location()
    else:
        if user_ship == 0:
            print(f"USER_SCORE:{user_score}")
            print(f"Computer_SCORE:{computer_score}")
            print("The Enemy surrender and you won the battel")
        else:
            print(f"USER_SCORE:{user_score}")
            print(f"Computer_SCORE:{computer_score}")
            print("The Enemy won and you lost the Battle")


greeting_message = Welcome()
print(greeting_message.welcome_message())
run_game()
