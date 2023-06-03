import random

print("-------------------------------")
print("Welcome to Ultimate BATTLESHIPS!!\n""Board Size: 5 Number of ships: 4\n""Top left corner is row:0, col:0\n")
print("-------------------------------")

user_name = input("please enter you name to start game:")
grid_w = [".", ".", ".", "."]
grid_x = [".", ".", ".", "."]
grid_y = [".", ".", ".", "."]
grid_z = [".", ".", ".", "."]
previous_input_coordinates = []

user_ship = 4
computer_ship = 4
user_score = 0
compter_score = 0


def create_grid():

    for x in range(len(grid_w)):

        print(grid_w[x], end=" ")
        print(grid_x[x], end=" ")
        print(grid_y[x], end=" ")
        print(grid_z[x], end=" ")
        print(" ")


def change_grid_value():

    x = input("please enter the value of grid:")
    grid_w[0] = x
    print(grid_w)


def set_ship_location():
    global grid_w 
    grid_w = [".", ".", ".", "."]
    global grid_x 
    grid_x= [".", ".", ".", "."]
    global grid_y 
    grid_y= [".", ".", ".", "."]
    global grid_z 
    grid_z= [".", ".", ".", "."]
    w_1 = random.randrange(3)
    x_1 = random.randrange(3)
    y_1 = random.randrange(3)
    z_1 = random.randrange(3)
    print(w_1, x_1, y_1, z_1)
    grid_w[w_1] = "@"
    grid_x[x_1] = "@"
    grid_y[y_1] = "@"
    grid_z[z_1] = "@"
    create_grid()


def get_user_targets():
    global previous_input_coordinates
    
    try:
       y_axis = int(input("please enter the column no:"))
       x_axis = int(input("please enter the row no:"))

       while y_axis > 4 and x_axis > 4:
           y_axis = int(input("please enter no between (1 & 3):"))
           x_axis = int(input("please enter no between (1 & 3):"))
       if previous_input_coordinates == [] :
           previous_input_coordinates.append((y_axis,x_axis))
           
       else:

            for x in range(len(previous_input_coordinates)):

                while previous_input_coordinates[x] == (y_axis,x_axis) :
                    y_axis = int(input("please enter a new column no, this was used before:"))
                    x_axis = int(input("please enter a new row no, this was used before:"))
                
            else:
                previous_input_coordinates.append((y_axis,x_axis))
                previous_input_coordinates = list(dict.fromkeys(previous_input_coordinates))
                
    except ValueError:
        try:
           y_axis = int(input("please enter an integer no:"))
           x_axis = int(input("please enter an integer no:"))
        except ValueError :
            run_game()   
       
    return y_axis , x_axis



def remove_ship_from_score():
    global user_ship
    user_ship -= 1


def update_the_score():
    global user_score
    user_score += 1


def compare_user_hit_with_ship_location():
    y,x = get_user_targets()
    if y == 1 and x == 1 and grid_w[0] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 1 and x == 2 and grid_w[1] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 1 and x == 3 and grid_w[2] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 1 and x == 4 and grid_w[3] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 2 and x == 1 and grid_x[0] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 2 and x == 2 and grid_x[1] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 2 and x == 3 and grid_x[2] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 2 and x == 4 and grid_x[3] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 3 and x == 1 and grid_y[0] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 3 and x == 2 and grid_y[1] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 3 and x == 3 and grid_y[2] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 3 and x == 4 and grid_y[3] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 4 and x == 1 and grid_z[0] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 4 and x == 2 and grid_z[1] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif (y == 4 and x == 3 and grid_z[2] == "@"):
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()
    elif y == 4 and x == 4 and grid_z[3] == "@":
        print("Congratulate you hit the Target")
        remove_ship_from_score()
        update_the_score()

    else:
        print("Sorry please enter new coordinates")


def run_game():
    set_ship_location()
    while user_ship != 0:
        print(user_score)
        print(previous_input_coordinates)
        
        compare_user_hit_with_ship_location()
    else:
        print("The Enemy surrender and you won the battel")


run_game()
