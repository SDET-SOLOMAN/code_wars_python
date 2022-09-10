# Terminal game move function

# In this game, the hero moves from left to right.
# The player rolls the dice and moves the number of spaces indicated by the dice two times.

# Create a function for the terminal game that takes the current position of
# the hero and the roll (1-6) and return the new position.

# move(3, 6) should equal 15

# solution 1 using function and return
def move(position=3, roll=6):
    return position + roll * 2


# solution 2 using lambdas
move_two = lambda p, r: p + r * 2

print(move())
print(move_two(3, 6))
