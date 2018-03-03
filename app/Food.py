class Food (Node):

    def __init__(self, data, snake):
<<<<<<< HEAD
        x = data['x']
        y = data['y']
        
        super(Node, self).__init__((x, y))
        
        self.distance = abs(snake.x - self.x) + abs(snake.y - self.y)
=======
        self.x = data['x']
        self.y = data['y']
        self.distance = abs(snake.head[0] - self.x) + abs(snake.head[1] - self.y)
>>>>>>> master
        

