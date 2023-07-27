import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
X_OFFSET = SCREEN_WIDTH // 2
Y_OFFSET = SCREEN_HEIGHT // 2

def display_chunk(x_lst,y_lst,angle, target_x, target_y):
    
    def launch():        
        pumpkin.pendown()
        for idx in range(1,len(x_lst)):
            pumpkin.goto(x_lst[idx] - X_OFFSET,y_lst[idx] - Y_OFFSET)
        wn.onkeypress(None, 'c')
            
    def stop():
        wn.resetscreen()
        wn.bye()
             
    turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)    
    wn = turtle.Screen()
    # set up target
    wn.register_shape("target.gif")
    target = turtle.Turtle()
    target.hideturtle()
    target.penup()
    target.setpos(target_x- X_OFFSET,target_y - Y_OFFSET)
    target.shape("target.gif")
    target.showturtle()
    
    # set up pumpkin
    wn.register_shape("pumpkin.gif")
    wn.title("Type 'c' to chunk your pumpkin or 'q' to close")
    pumpkin = turtle.Turtle()
    pumpkin.hideturtle()
    pumpkin.penup()
    pumpkin.goto(x_lst[0] - X_OFFSET, y_lst[0] - Y_OFFSET)
    pumpkin.shape("pumpkin.gif")
    pumpkin.color("orange")
    pumpkin.pensize(5)
    pumpkin.showturtle()
            
    # wait for user to launch
    wn.onkeypress(launch, 'c')
    wn.onkeypress(stop, 'q')
    wn.listen()
    wn.mainloop()
    
