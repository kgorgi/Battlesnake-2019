from tail_path import path_to_tail

def stall(board):
    
    us = board.get_our_snake()
    path= path_to_tail(board)
    
    if path and board.is_snake_node(path[-1]) and path[-1].get_snake_info().health == 100 and len(path)<=2:
        return None


    return path