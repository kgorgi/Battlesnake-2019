from pathing.astar import aStar

class SnakeInfo:
    def __init__(self, data,board, our_snake_id =""):
        self._head = (data['body'][0]['x'],  data['body'][0]['y'])
        self.health = data['health']
        self.length = len(data['body'])
        self._tail = (data['body'][self.length-1]['x'], data['body'][self.length-1]['y'])
        self._id = data['id']

        self._board = board

        self._enemy = not our_snake_id == self._id

    def is_enemy(self):
        return self._enemy
    
    def get_head(self):
        return self._board.get_node(self._head)

    def get_tail(self):
        return self._board.get_node(self._tail)
    
    def path_to_tail(self,board):
        return aStar(self.get_head(),self.get_tail(),board)
    

    def __str__(self):
        return 'Snake: ' + \
               ' head: ' + str(self.get_head().get_point()) + \
               ' tail: ' + str(self.get_tail().get_point()) + \
               ' health: ' + str(self.health) + \
               ' length: ' + str(self.length)
    
    def get_id(self):
        return self._id
