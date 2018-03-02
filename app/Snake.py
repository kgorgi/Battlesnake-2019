class Snake:
    def __init__(self, data):
        self.x = data['body']['data'][0]['x']
        self.y = data['body']['data'][0]['y']
        self.head = (  data['body']['data'][0]['x']  ,  data['body']['data'][0]['y']  )
        self.health = data['health']
        self.length = len(data['body']['data'])
        self.tail = (  data['body']['data'][self.length-1]['x']  ,   data['body']['data'][self.length-1]['y']  )
        print 'Snake: head: ', self.head, 'tail: ', self.tail, ' health: ', self.health, ' lnegth: ', self.length
