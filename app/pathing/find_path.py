from food_path import food_path 
from stall_path import stall
from util_path import is_viable,emerge_checks,safety_check

# Subject to change
TURNS_TO_CHASE_FOOD = 100
HEALTH_TO_CHASE_FOOD = 50

# Follows 'General Tree' diagram
# Controls meta state
# Does emergency check
# Calls find_food or find_stall

def find_path_new(board,food):

    move=None

    emerge_checks(board)

    if(board.get_turn() < TURNS_TO_CHASE_FOOD or 
        board.get_our_snake() < HEALTH_TO_CHASE_FOOD):
        move = find_food(board,food)
    
    #cant do food
    if(move==None):
        move = stall()

    safety_check(move):

    return move

def find_path(board):
    food_list = board.get_food_list()

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
