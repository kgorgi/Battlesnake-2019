from SnakeNode import SnakeNode
from FaceNode import FaceNode

# Returns false for snake nodes
class FoodFilter:
    def __init__(self):
        pass
    
    def is_neighbour(self, node):
        return not (isinstance(node, SnakeNode) or isinstance(node,FaceNode))

# Returns true for nodes that are in the list:snake_parts
class SnakePartFilter:
    def __init__(self, snake_parts):
        self._snake_parts = snake_parts

    def is_neighbour(self, node):
        if node in self._snake_parts:
            return True
        elif (isinstance(node, SnakeNode) or isinstance(node,FaceNode)):
            return False
        else:
            return True 
