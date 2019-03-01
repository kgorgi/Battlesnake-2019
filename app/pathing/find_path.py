from food_path import food_path, find_food 
from stall_path import stall
from util_path import is_viable, emerge_checks

# Subject to change
TURNS_TO_CHASE_FOOD = 50
HEALTH_TO_CHASE_FOOD = 50

def find_path(board):
    food_list = board.get_food_list()
    us = board.get_our_snake()

    # If Checking for Stall Scenarios 
    if( us.health > HEALTH_TO_CHASE_FOOD and board.get_turn() > TURNS_TO_CHASE_FOOD):
        return stall(board)

    fpath = food_path(food_list,board)
    if not fpath:
            return stall(board)
    fpath.reverse()


    while not is_viable(board,fpath) :
        idx = food_list.index(fpath[-1])
        if idx >= len(food_list): return stall(board)
        else: food_list = food_list[idx+1:]
        fpath = food_path(food_list,board)
        if not fpath:
            return stall(board)
        fpath.reverse()
        
    return fpath

