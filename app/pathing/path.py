from food_path import find_food 
from stall_path import find_stall

# Subject to change
TURNS_TO_CHASE_FOOD = 100
HEALTH_TO_CHASE_FOOD = 50

# Check for low health / obvious stuff
def emerge_checks(board):
    return

# Check that move doesnt kill us. And not null
def safety_check(move):
    return

# Follows 'General Tree' diagram
def find_path(board,food):

    emerge_checks(board)

    if(board.get_turn() < TURNS_TO_CHASE_FOOD or 
        board.get_our_snake() < HEALTH_TO_CHASE_FOOD):
        move = find_food(board,food)
    else:
        move = find_stall()

    safety_check(move):

    return move