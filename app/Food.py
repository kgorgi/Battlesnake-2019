class Food:

    def __init__(self, data, snake):
        self.x = data['x']
        self.y = data['y']
        self.distance = abs(snake.x - self.x) + abs(snake.y - self.y)
        

