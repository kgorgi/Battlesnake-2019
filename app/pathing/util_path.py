from filters import FoodFilter,SnakePartFilter
from neighbours import get_neighbours
from astar import aStar

# Check for low health / obvious stuff
def emerge_checks(board):
    return

# Check that move doesnt kill us. And not null
def safety_check(move):
    return

def is_viable(board,path):
    us = board.get_our_snake()
    path_check = aStar(path[1],us.get_tail(),board,SnakePartFilter([us.get_tail()]))

    if not path_check:
        return False
    
    return path_check

def dir(snake_head, next_node):
    x,y = next_node.get_point()
    sx,sy = snake_head.get_point()

    if x > sx:
        return 'right'
    elif x < sx:
        return 'left'
    if y > sy:
        return 'down'
    else:
        return 'up'

def direction(path,snake,data,board):
    if path is None or snake.length < 2 or data['turn'] < 2:
        neighbours = get_neighbours(snake.get_head().get_point(), board, FoodFilter())
        if len(neighbours) <= 0:
            return "down"
        direction = dir(snake.get_head(), neighbours[0])
    else:
        direction = dir(snake.get_head(), path[1])
    
    print direction
    return direction
