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
    print(w_1,x_1,y_1) 


set_ship_location()
