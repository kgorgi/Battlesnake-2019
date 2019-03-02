from Node import Node

SNAKE_MOVE_COST = 100

class SnakeNode(Node):
    def __init__(self, point, snake_info):
        x = point['x']
        y = point['y']
        super(SnakeNode, self).__init__((x, y))

        self._snake_info = snake_info

        # self.set_move_cost(SNAKE_MOVE_COST)

    def get_snake_info(self):
        return self._snake_info
        
        
