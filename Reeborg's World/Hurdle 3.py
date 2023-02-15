def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Define jump_over() function. Unlike jump(), it does not move() at the beginning.
def jump_over():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# Check if it is at goal, else it jumps
while not at_goal():
    if not front_is_clear():
        jump_over()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
