class Snake(Node):
    def __init__(self, data):
        
        x = data['body']['data'][0]['x']
        y = data['body']['data'][0]['y']

        super(Node, self).__init__((x, y))

        self.head = (  data['body']['data'][0]['x']  ,  data['body']['data'][0]['y']  )
        self.health = data['health']
        self.length = len(data['body']['data'])
        self.tail = (  data['body']['data'][self.length-1]['x']  ,   data['body']['data'][self.length-1]['y']  )
        

    def __str__(self):
        return 'Snake: head: ', self.head, 'tail: ', self.tail, ' health: ', self.health, ' length: ', self.length, "node_loc: ", super(Node, self).get_point()