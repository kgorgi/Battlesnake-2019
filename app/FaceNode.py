from Node import Node

FACE_MOVE_COST = 50

class FaceNode(Node):
    def __init__(self, point, snake_info):
        x = point[0]
        y = point[1]
        super(FaceNode, self).__init__((x, y))

        self._snake_info = snake_info

        self.set_move_cost(FACE_MOVE_COST)

    def get_snake_info(self):
        return self._snake_info
        
        
