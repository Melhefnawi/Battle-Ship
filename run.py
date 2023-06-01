import random

print("-------------------------------")
print ("Welcome to Ultimate BATTLESHIPS!!\n""Board Size: 5 Number of ships: 4\n""Top left corner is row:0, col:0\n")
print ("-------------------------------")

user = input("please enter you name to start game:")
grid_w = ["." ,"." ,"." ,"." , ".",".","."]
grid_x = [".",".",".",".",".",".",".","."]
grid_y = [".",".",".",".",".",".",".","."]
grid_z = [".",".",".",".",".",".",".","."]  

def  create_grid():
    
    for x in range (len(grid_w)):
        
        print(grid_w[x],end=" ")
        print(grid_x[x],end=" ")   
        print(grid_y[x],end=" ") 
        print(grid_z[x],end=" ") 
        print(" ")
    
create_grid()       

              
def change_grid_value():
    
    x = input("please enter the value of grid:")
    grid_w[0]=x
    print (grid_w)

      

change_grid_value()
create_grid()
    
def set_ship_location():
    w_1 = random.randrange(5)
    x_1 = random.randrange(5)
    y_1 = random.randrange(5)
    z_1 = random.randrange(5)
    print(w_1,x_1,y_1,z_1) 
    grid_w[w_1]= "@"
    grid_x[x_1]= "@"
    grid_y[y_1]= "@"
    grid_z[z_1]= "@"
    create_grid()


set_ship_location()

def get_user_target_x_axis():
    x_axis = input("please enter the row no:")
    
    return x_axis
    
def get_user_target_y_axis():
    y_axis = input("please enter the column no:")

    return y_axis

def compare_user_hit_with_ship_location():
    x = get_user_target_x_axis()
    y = get_user_target_y_axis()
    print (x)


compare_user_hit_with_ship_location()    