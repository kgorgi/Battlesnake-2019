from Node import Node

class FaceNode(Node):
    def __init__(self, point, snake_info):
        x = point['x']
        y = point['y']
        super(FaceNode, self).__init__((x, y))

        self._snake_info = snake_info

    def get_snake_info(self):
        return self._snake_info
        
        
