from SnakeNode import SnakeNode
from neighbours import get_neighbours
from Board import get_enemy_heads

# Returns false for snake nodes
class FoodFilter:
    def __init__(self):
        pass
    
    def is_neighbour(self, node):
        return not isinstance(node, SnakeNode)

# Returns true for nodes that are in the list:snake_parts
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

class SafeSnakePartFilter(SnakePartFilter):
    def is_neighbour(self,node):
        if super.is_neighbour(node):
            for n in get_neighbours(node.get_point()):
                if n in get_enemy_heads(): return False
            return True  
        else: 
            return False
