from Node import Node

class Food (Node):

    def __init__(self, data):
        x = data['x']
        y = data['y']
        
        super(Food, self).__init__((x, y))
        

