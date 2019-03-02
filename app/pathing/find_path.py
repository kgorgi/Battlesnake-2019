from food_path import food_path, find_food 
from stall_path import stall
from util_path import is_viable, emerge_checks
from attack_path import attack 

# Subject to change
TURNS_TO_CHASE_FOOD = 50
HEALTH_TO_CHASE_FOOD = 50
ATTACK_LENGTH_THRESH = 2 # Difference between snake lengths to attack


def find_path(board):
    food_list = board.get_food_list()
    us = board.get_our_snake()
    
    path = None
    
    # Check if we should prioritize food
    if(TURNS_TO_CHASE_FOOD >= board.get_turn() or HEALTH_TO_CHASE_FOOD > us.health):
        path = food_path(food_list, board)
    
    # Check if we can attack
    if not path and (len(board.get_enemies()) is 1):
        enemy = board.get_enemies()[0]
        # Check if large enough to attack enemy
        if us.length - enemy.length - ATTACK_LENGTH_THRESH > 0:
            path = attack(board)
 
    # If no path to food stall
    if not path:
        return stall(board)
   
    # Check that the path is viable 
    # path = check(board, path, food_list) 
    path.reverse()
       
    return path


#check that there will be a path back to tail. else recomputes
def check(board, path, food):
    path.reverse()
    while not is_viable(board, path) :
        idx = food.index( path[-1])
        if idx >= len(food): return stall(board)
        else: food = food[idx+1:]
        path = food_path(food, board)
        if not path:
            return stall(board)
        path.reverse()
    return path

