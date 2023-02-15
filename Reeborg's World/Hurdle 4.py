def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Define jump_high() function. It is a jump function for unknown heights
def jump_high():
    turn_left() # Turns upwards, ready to jump.
    height_count = 0 # Initializes the count for each height increase in the jump.
    while wall_on_right():
        height_count += 1 # Begins the count of the step
        move() # While there is a wall to the right, keep moving up!
    turn_right() # Turns forward to go past the hurdle.
    move() # Goes past the hurdle
    turn_right() # Turns down now for descent back
    for step in range(height_count):
        move() # For the number of height count, Reeborg keeps moving down until it reaches ground level. 
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
