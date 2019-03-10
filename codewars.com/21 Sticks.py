# 21 Sticks

# The Game:
# In this game, there are 21 sticks lying in a pile. 
# Players take turns taking 1, 2, or 3 sticks. 
# The last person to take a stick wins. Like this:

# Your task:
# Create a robot that will always win the game. 
# Your robot will always go first. 
# The function should take an integer and returns 1, 2, or 3.

def make_move(sticks):    
    return 1 if sticks % 4 == 0 else sticks % 4