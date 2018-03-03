class Food (Node):

    def __init__(self, data, snake):
        x = data['x']
        y = data['y']
        
        super(Node, self).__init__((x, y))
        
        self.distance = abs(snake.x - self.x) + abs(snake.y - self.y)
        

