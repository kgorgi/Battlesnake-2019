class SnakeInfo:
    def __init__(self, data, our_snake_id =""):
    
        self.head = (data['body']['data'][0]['x'],  data['body']['data'][0]['y'])
        self.health = data['health']
        self.length = len(data['body']['data'])
        self.tail = (data['body']['data'][self.length-1]['x'], data['body']['data'][self.length-1]['y'])
        self._id = data['id']

        self._enemy = not our_snake_id == self._id

    def is_enemy(self):
        return self._enemy

    def __str__(self):
        return 'Snake: head: ', self.head, 'tail: ', self.tail, ' health: ', self.health, ' length: ', self.length
    
    def get_id(self):
        return self._id