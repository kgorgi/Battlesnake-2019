from Node import Node

class Food (Node):

    def __init__(self, data, snake_head):
        x = data['x']
        y = data['y']

        super(Food, self).__init__((x, y))

        sx, sy = snake_head.get_point()
        self._start_distance = abs(x - sx) + abs(y - sy)
        
    def get_distance_to_head():
        return self._start_distance

