def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Define jump_high() function. It is a jump function for unknown heights
def jump_high():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left() 
    
# Unless it is at goal, else it keeps moving
while not at_goal():
    # Checks if its front is not clear to move ...
    if not front_is_clear():
        # If front is not clear, it jumps the hurdle/wall
        jump_high()
    else:
        # Otherwise it keeps moving forward
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
