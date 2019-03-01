from food_path import food_path, find_food 
from stall_path import stall
from util_path import is_viable, emerge_checks

# Subject to change
TURNS_TO_CHASE_FOOD = 50
HEALTH_TO_CHASE_FOOD = 50

# Follows 'General Tree' diagram
def find_path_new(board):
    food = board.get_food_list()
    
    emerge_checks(board)

    if(board.get_turn() < TURNS_TO_CHASE_FOOD or 
        board.get_our_snake() < HEALTH_TO_CHASE_FOOD):
        move = find_food(board,food)
    
    if(move is None):
        return stall(board)

    # safety_check(move):

    while not is_viable(board,move) :
        idx = food.index(move[-1])
        if idx >= len(food): return stall(board)
        else: food = food[idx+1:]
        move = find_food(board, food)
        if not move:
            return stall(board)
        move.reverse()
    
    return move


def find_path(board):
    food_list = board.get_food_list()
    us = board.get_our_snake()
 
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

