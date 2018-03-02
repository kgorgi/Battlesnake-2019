class Food:

    def __init__(self, data, snake):
        self.x = data['x']
        self.y = data['y']
        self.distance = abs(snake.head[0] - self.x) + abs(snake.head[1] - self.y)
        

