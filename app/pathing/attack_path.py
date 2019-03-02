from filters import SnakePartFilter
from astar import aStar
from util_path import is_viable
from neighbours import get_neighbours

def attack(board):
    us = board.get_our_snake()
    snake_heads = [info.get_head() for info in board.get_enemies()]
    snake_heads.append(board.get_our_snake().get_head())
    # Get Possible moves of enemies head
    # Select move closest to center 
    # A star to that position
    enemy_moves = find_enemy_moves(board)
    attack_point = closest_to_center(board, enemy_moves)
    
    path = None

    # If we can attack, return path to attack point
    if attack_point: 
        path = aStar(attack_point, [ us.get_head() ], board, SnakePartFilter( [ us.get_head() ] ))
    
    
    return path

# Return move an enemy can make closes to middle of board
def find_enemy_moves(board):
    snake_heads = [info.get_head() for info in board.get_enemies()]
    snake_heads.append(board.get_our_snake().get_head())
    enemy = board.get_enemies()[0]
    enemy_head = enemy.get_head().get_point()
    moves = get_neighbours(enemy_head, board, SnakePartFilter(snake_heads))
    return moves

def closest_to_center(board, moves):
    if not moves:   
        return None

    center = ( board.get_width() / 2 , board.get_height() / 2 )
    closest = None 
    manhattan = board.get_width() + board.get_height()
    for move in moves:
        dist = manhattan_dist(move.get_point(), center)
        if dist < manhattan:
            closest = move
            manhattan = dist
    
    return  closest 

def manhattan_dist(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])
        
        
