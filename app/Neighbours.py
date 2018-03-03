from SnakeNode import SnakeNode

def get_neighbours(point, board, filter_obj):
    x,y = point

    valid_adjacent = []

    if x - 1 >= 0:
        valid_adjacent.append((x-1,y))
    if y-1 >= 0:
        valid_adjacent.append((x,y-1))
    if x + 1 < board.get_width():
        valid_adjacent.append((x+1,y))
    if y + 1 < board.get_height():
        valid_adjacent.append((x,y+1))        

    neighbours = []
    for point in valid_adjacent:
        node = board.get_node(point)

        # Add empty node if available
        if node is None:
            node = board.add_blank(point)

        if filter_obj.is_neighbour(node):
            neighbours.append(node)
    
    return neighbours

class FoodFilter:
    def __init__(self):
        pass
    
    def is_neighbour(self, node):
        return not isinstance(node, SnakeNode)

class SnakePartFilter:
    def __init__(self, snake_parts):
        self._snake_parts = snake_parts

    def is_neighbour(self, node):
        if node in self._snake_parts:
            return True
        elif isinstance(node, SnakeNode):
            return False
        else:
            return True 

