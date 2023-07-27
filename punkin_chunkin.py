# ------------------------------------------------------
# Problem 1
# ------------------------------------------------------
import math
import random
import pumpkin_display
import matplotlib.pyplot as plt
import cisc106

# Global Constants
SCREEN_WIDTH = pumpkin_display.SCREEN_WIDTH
SCREEN_HEIGHT = pumpkin_display.SCREEN_HEIGHT
# Add your global constants here
SCREEN_WIDTH = pumpkin_display.SCREEN_WIDTH
SCREEN_HEIGHT = pumpkin_display.SCREEN_HEIGHT
PUMPKIN_X = 25
PUMPKIN_Y_MIN = 0
PUMPKIN_Y_MAX = SCREEN_HEIGHT // 2
PUMPKIN_ANGLE_MIN = 0
PUMPKIN_ANGLE_MAX = 80
PUMPKIN_v0_MIN = 10
PUMPKIN_v0_MAX = 100
GRAVITY = -9.81

# ------------------------------------------------------
# Problem 2 
# ------------------------------------------------------
# Add your get_valid_integer function here
# The function get_valid_integer consumes (prompt, the minimum, and maximum values)
#to determine wether the number entered for height, angle, and velocity of the pumpkin is in the range of possiblities 
def get_valid_integer(prompt, minimum, maximum):
    while True:
        try:
            n = int(input(prompt))
            if minimum <= n <= maximum:
                return n
            print("Invalid attempt the number entered was not in between ", minimum, " and ", maximum)
        except:
            print("Please enter an integer")

#------------------------------------------------------
# Problem 3
#------------------------------------------------------
# Add your get_yes_or_no function here
# The function get_yes_or_no consumes a string (either "yes" or "no") and returns the users answer
def get_yes_or_no(string):
    yes_no = input("Enter yes or no ")
    # This while loop takes the input from the user and if that input is not equal to yes or no
    #it asks for a new input of yes or no until yes or no is inputted
    while(yes_no.lower()!="yes" and yes_no.lower()!="no"):
        print("Invalid Input")
        yes_no = input("Enter yes or no ")
    #Once a yes or a no is inputted the result is returned
    return yes_no

#------------------------------------------------------
# Problem 4
#------------------------------------------------------
def set_up_target():
    
    # intially our target will be at a set location    
    #x_target = SCREEN_WIDTH - 100
    #y_target = 100
    
    # after your program is developed and working correctly
    # set the target at a random location
    # using the following statements
   
    x_target = random.randrange(SCREEN_WIDTH // 2, SCREEN_WIDTH - 99, 50)
    y_target = random.randrange(10, (1 + SCREEN_HEIGHT // 5),10)   
    
    print("Target is", x_target," meters away and at a height =",y_target)
    return x_target, y_target

#------------------------------------------------------
# Problem 5 A
#------------------------------------------------------
# Add your get_init_pumpkin_height here
# The function get_init_pumpkin_height uses the get_valid_integer function
# Then it asks for a users input on the height of the pumpkin
# If the pumpkin is between the Max and Min values set up in the global constants then it returns the height
def get_init_pumpkin_height():
    height = get_valid_integer("Enter pumpkin height: ", PUMPKIN_Y_MIN, PUMPKIN_Y_MAX)
    return height

#------------------------------------------------------
# Problem 5 B
#------------------------------------------------------
# Add your get_pumpkin_angle here
# The function get_pumpkin_angle uses the get_valid_integer function
# Then it asks for a users input on the angle of the pumpkin's launch
# If the pumpkin's angle is between the Max and Min values set up in the global constants then it returns the angle
def get_pumpkin_angle():
    angle = get_valid_integer("Enter the angle at which you would like to launch the pumkin: ", PUMPKIN_ANGLE_MIN, PUMPKIN_ANGLE_MAX)
    return angle

#------------------------------------------------------
# Problem 5 C
#------------------------------------------------------
# Add your get_pumpkin_v0 here
# The function get_pumpkin_v0 uses the get_valid_integer function
# Then it asks for a users input on the velocity of the pumpkin
# If the pumpkin is between the Max and Min values set up in the global constants then it returns the velocity
def get_pumpkin_v0():
    v0 = get_valid_integer("Enter the velocity at which you would like to launch the pumpkin: ", PUMPKIN_v0_MIN, PUMPKIN_v0_MAX)
    return v0

#------------------------------------------------------
# Problem 6
#------------------------------------------------------
# Add your set_up_pumpkin function here
# The function set_up_pumpkin takes the height, angle, and velocity returned from the functions
# get_init_pumpkn_height, get_pumpkin_angle, and get_pumpkin_v0 and sets the values equal to variables
# which can be returned by calling this function 
def set_up_pumpkin():
    PUMPKIN_Y = 0
    PUMPKIN_Y = get_init_pumpkin_height()
    angle = get_pumpkin_angle()
    velocity = get_pumpkin_v0()
    return (PUMPKIN_X ,PUMPKIN_Y,angle,velocity)

#------------------------------------------------------
# Problem 7
#------------------------------------------------------
# Add your chunk_punkin function here
# The function chunk_punkin consmes the velocity and the angle
# then finds the velocity in the x direction and the velocity in the y direction
def chunk_punkin(v0, angle):
    # The radians function mst be used because the angles need to be converted from degrees to radians
    # for python to read
    angleRadian = math.radians(angle)
    vx = round(v0 * math.cos(angleRadian), 2)
    vy = round(v0 * math.sin(angleRadian), 2)
    return (vx, vy)

cisc106.assertEqual(chunk_punkin(30,40),(22.98, 19.28))
cisc106.assertEqual(chunk_punkin(60,90),(0.0, 60.0))
cisc106.assertEqual(chunk_punkin(12,50),(7.71, 9.19))
cisc106.assertEqual(chunk_punkin(30, 25),(27.19, 12.68))
cisc106.assertEqual(chunk_punkin(80, 60),  (40.00, 69.28))

#------------------------------------------------------
# Problem 8
#------------------------------------------------------
# Add your move_pumpkin function here
# The move_pumpkin function takes the orignal x and y coordinates of the pumpkin
# then adds the velocity coming from the x and y directions and adds it to them
# The y direction is different from the x due to gravity
# the new coordinates are returned as well as the new velocity in the y direction
def move_pumpkin(PUMPKIN_X, PUMPKIN_Y, vx, vy):
    NEW_PUMPKIN_X = (PUMPKIN_X + vx)
    NEW_PUMPKIN_Y = float(round(PUMPKIN_Y + vy + (0.5 * (GRAVITY)),2))
    NEW_Y_v0 = float(round((vy + GRAVITY),2))
    return (NEW_PUMPKIN_X, NEW_PUMPKIN_Y, NEW_Y_v0)

cisc106.assertEqual(move_pumpkin(100, 150, 20, 25),(120, 170.09, 15.19))
cisc106.assertEqual(move_pumpkin(300, 10, 50, -15), (350,-9.91, -24.81))
cisc106.assertEqual(move_pumpkin(200, 50, 50, 33), (250, 78.09, 23.19))
cisc106.assertEqual(move_pumpkin(100, 150, 20, 25),(120, 170.09, 15.19))
cisc106.assertEqual(move_pumpkin(300, 10, 50, -15), (350,-9.91, -24.81))

#------------------------------------------------------
# Problem 9
#------------------------------------------------------
# Add your did_hit_target function here
# The function did_hit_target consumes the x and y coordinates of both the pumpkin and the target
# Then determines wether the pumpkin hit the target based off of the size of the target
# And returns a boolean (True or False) for if t did or did not hit the target
def did_hit_target(PUMPKIN_X, PUMPKIN_Y, TARGET_X, TARGET_Y):
   if((abs(PUMPKIN_X-TARGET_X)<15) and abs(PUMPKIN_Y-TARGET_Y)<15):
       return True
   else:
       return False

cisc106.assertEqual(did_hit_target(450, 100, 460, 105), True)
cisc106.assertEqual(did_hit_target(450, 100, 460, 125), False)
cisc106.assertEqual(did_hit_target(150, 20, 30, 100), False)
cisc106.assertEqual(did_hit_target(99, 60, 300, 133), False)
cisc106.assertEqual(did_hit_target(100, 0, 500, 100), False)
#------------------------------------------------------
# Problem 10
#------------------------------------------------------
# Add your is_off_screen function here
# The function is_off_screen compares the x coordinate with the width of the screen to see if it went off the right side
# the y coordinate with the height of the screen to see if the pumpkin has gone off the top of the screen
# and compares both the x and y to 0 to see if the pumpkin went off the bottom or left of the screen 
def is_off_screen(PUMPKIN_X, PUMPKIN_Y):
    if PUMPKIN_X > SCREEN_WIDTH and PUMPKIN_Y > SCREEN_HEIGHT:
        return False
    elif PUMPKIN_X < 0 and PUMPKIN_Y < 0:
        return False
    else:
        return True

cisc106.assertEqual(is_off_screen(7777, 200),True)
cisc106.assertEqual(is_off_screen(80, 4),True)
cisc106.assertEqual(is_off_screen(1000, 601),False)
cisc106.assertEqual(is_off_screen(100,-100), True)
cisc106.assertEqual(is_off_screen(800, 100),True)
    
#------------------------------------------------------
# Problem 11
#------------------------------------------------------
# Add your compute_trajectory function here
# The function compute_trajectory consumes the x and y coordinates of the targets,
# the x and y coordinates of the pumpkin, the angle, and the velocity of the pumpkin
# Then compiles a list where the new values of the x and y coordinates of the pumpkin can be stored
# so that the x,y coordinates of the pumpkin can be paired and displayed on a graph
# Then if the pumpkin hits the target or misses a statement is printed explaining and a list of the
# x and y pumpkin corrdinates are returned
def compute_trajectory(x_target, y_target,x_pumpkin, y_pumpkin, angle_pumpkin, v_pumpkin):
                
    # initialize a list of x values. the first element should be the pumpkin’s initial x coordinate
    x_val_list=[x_pumpkin]
    x_val_list=[x_pumpkin]
    
    # initialize a list of y values. the first element should be the pumpkin’s initial y coordinate
    y_val_list=[y_pumpkin]
    y_val_list=[y_pumpkin]

    # chunk the pumpkin - call the chunk_pumpkin and assign the return values to 
    # variables representing the speed in the x direction and the speed in the y direction
    speed=chunk_punkin(v_pumpkin,angle_pumpkin)
    x_velocity=speed[0]
    y_velocity=speed[1]

    complete=False
    
    # call move_pumpkin repeatedly until either the pumpkin is off the screen
    #    or it hit the target
    # with each iteration, append the pumpkin's new x coordinate to the
    # end of the list of x values
    # and append the new y coordinate to the end of the list of y values
    while (did_hit_target(x_pumpkin,y_pumpkin,x_target,y_target)!=True) and complete==False:
        pumpkin_change=move_pumpkin(x_pumpkin,y_pumpkin,x_velocity,y_velocity)
        x_pumpkin=pumpkin_change[0]
        y_pumpkin=pumpkin_change[1]
        y_velocity=pumpkin_change[2]
        x_val_list.append(x_pumpkin)
        y_val_list.append(y_pumpkin)
        
    # if the pumpkin goes off screen - display a message to the user that they missed
    # if the pumpkin hit the target - display a message to the user that they hit the target
        if did_hit_target(x_pumpkin,y_pumpkin,x_target,y_target)==True:
            print("You have hit the target")
            complete=True
        if (x_pumpkin>SCREEN_WIDTH) or (y_pumpkin>SCREEN_HEIGHT) or (y_pumpkin<0):
            print("You have missed the target")
            complete=True
            
    # return the list of x values followed by the list of y values

    return (x_val_list),(y_val_list)


#------------------------------------------------------
# Problem 13
#------------------------------------------------------
# Add your plot_trajectory function here
# Solve Problem 12 first
# The function plot_trajectory consumes the x and y lists of the first and second attempts
# as well as the labels associated with them and the x and y coordinates of the target
# mat plot is then used to draw out the attempts and circles are displayed
# the plots are returned 
def plot_trajectory(X_LIST_1, Y_LIST_1, TAG_1, X_LIST_2, Y_LIST_2, TAG_2, X_TARGET, Y_TARGET):
    fig,ax = plt.subplots()
    ax.plot(X_LIST_1, Y_LIST_1, color="green", label=TAG_1)
    ax.plot(X_LIST_2, Y_LIST_2, color="red", label=TAG_2)
    ax.legend()
    ax.grid()
    plt.title("Punkin Chunkin Trajectory")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    index_1=len(X_LIST_1)-1
    index_2=len(X_LIST_2)-1
    ax.add_artist(plt.Circle(((X_LIST_1[index_1],Y_LIST_2[index_1])), 15, color='orange'))
    ax.add_artist(plt.Circle(((X_LIST_2[index_2],Y_LIST_2[index_2])), 15, color='red'))
    plt.show()
    return fig,ax 

#------------------------------------------------------
# Problem 12 &  Problem 14
#------------------------------------------------------
# Add your play_punkin_chunkin function here
# The function play_punkin_chunkin explains the game to the user
# then asks if the user would like to use two practice shots
# if the player answers yes they are able to try to hit the target two times
# before ther actal attempt. If the user enters no they must do their actaual attempt
# If the user hits the target a message will be displayed telling them so and if they miss
# a message will be displayed telling them
def play_punkin_chunkin():
    print("Hello and welcome to the game Punkin Chunkin! \nThe objective of this game is to launch a pumpkin and hit a target.\nYou will need to enter in the angle and velocity at which you launch the pumpkin.\n")
    TARGET_X, TARGET_Y = set_up_target()
    print("You will get two trials turns\nWould you like to practice?")
    if get_yes_or_no("Would you like to practice before you begin?") =="yes":
        
        print("\nThis is trial number 1")
        PUMPKIN_X ,PUMPKIN_Y,angle,velocity = set_up_pumpkin()
        X_LIST_1, Y_LIST_1 = compute_trajectory(TARGET_X,TARGET_Y,PUMPKIN_X,PUMPKIN_Y,angle,velocity)
        TAG_1 = "Pumpkin Trial 1"
        
        print("\nThis is trial number 2")
        PUMPKIN_X ,PUMPKIN_Y,angle,velocity = set_up_pumpkin()
        X_LIST_2, Y_LIST_2 = compute_trajectory(TARGET_X,TARGET_Y,PUMPKIN_X,PUMPKIN_Y,angle,velocity)
        TAG_2 = "Pumpkin Trial 2"
        
        plot_trajectory(X_LIST_1, Y_LIST_1, TAG_1, X_LIST_2, Y_LIST_2, TAG_2, TARGET_X, TARGET_Y)
            
    
    PUMPKIN_X ,PUMPKIN_Y,angle,velocity = set_up_pumpkin()
    x_val_list, y_val_list = compute_trajectory(TARGET_X,TARGET_Y,PUMPKIN_X,PUMPKIN_Y,angle,velocity)
    pumpkin_display.display_chunk(x_val_list, y_val_list, angle, TARGET_X, TARGET_Y)
    
    
if __name__ == "__main__":
    play_punkin_chunkin()


