from astar import aStar
from filters import SnakePartFilter
from util_path import is_viable
from stall_path import stall

# Do food tree here
def food_path(food_list,board):
    snake_heads = [info.get_head() for info in board.get_enemies()]
    snake_heads.append(board.get_our_snake().get_head())
    for food in food_list:
        food_to_head = aStar(food,snake_heads,board,SnakePartFilter(snake_heads))
        if not food_to_head: continue
        if food_to_head[-1] == board.get_our_snake().get_head():
            return food_to_head
    return None

def find_food(food_list,board):
    snake_heads = [info.get_head() for info in board.get_enemies()]
    snake_heads.append(board.get_our_snake().get_head())
    for food in food_list:
        food_to_head = aStar(food,snake_heads,board,SnakePartFilter(snake_heads))
        if not food_to_head: continue
        if food_to_head[-1] == board.get_our_snake().get_head():
            return food_to_head
    return None

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
