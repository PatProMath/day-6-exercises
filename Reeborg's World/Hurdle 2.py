def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Define jump() function
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# Check if it is at goal, else it jumps
while not at_goal():
    jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
move()
move()
turn_left()
move()
turn_left()
turn_left()
