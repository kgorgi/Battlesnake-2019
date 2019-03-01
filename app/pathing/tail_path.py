
from filters import SnakePartFilter
from astar import aStar

def path_to_tail(board):
    snake_tails = [info.get_tail() for info in board.get_enemies()]
    snake_tails.append(board.get_our_snake().get_tail())
    path_to_tail = aStar(board.get_our_snake().get_head(),snake_tails,board,SnakePartFilter(snake_tails))
    return path_to_tail