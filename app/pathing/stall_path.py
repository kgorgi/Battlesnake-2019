from tail_path import path_to_tail
from filters import SnakePartFilter
from astar import aStar

# General Decision Logic Exists Here
def stall(board):
    us = board.get_our_snake()
    path = follow_our_tail(board)
    
    # If no path to tail follow other tail
    if path is None:
        path = follow_other_tail(board)   
    
    # If no path to other tail fill board
    if path is None:
        path = fill(board)
    return path

# TODO
# Return path to fill board not following tail
def fill(board):
    return None

# Returns path to our tail
def follow_our_tail(board):
    our_tail = [ board.get_our_snake().get_tail() ]
    head = board.get_our_snake().get_head()
    path_to_tail = aStar(head, our_tail, board, SnakePartFilter(our_tail))
    return path_to_tail

# Return path to other tail
def follow_other_tail():
    snake_tails = [info.get_tail() for info in board.get_enemies()]
    head = board.get_our_snake().get_head()
    path_to_tail = aStar(head, snake_tails, board, SnakePartFilter(snake_tails))
    return path_to_tail(board)


