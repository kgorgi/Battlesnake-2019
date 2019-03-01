from tail_path import path_to_tail

# for now chase tail?
'''
have to think how we should set this up ~ goh

- make fill and chase tail functions then implment stall diagram here?
if so make fill_path.py
'''

def find_stall()
    return

def stall(board):
    us = board.get_our_snake()
    path= path_to_tail(board)
    
    if path and board.is_snake_node(path[-1]) and path[-1].get_snake_info().health == 100 and len(path)<=2:
        return None
    return path