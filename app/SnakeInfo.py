from aStar import aStar
from Neighbours import getNeighbours

class SnakeInfo:
    def __init__(self, data,board, our_snake_id =""):
    
        self._head = (data['body']['data'][0]['x'],  data['body']['data'][0]['y'])
        self.health = data['health']
        self.length = len(data['body']['data'])
        self._tail = (data['body']['data'][self.length-1]['x'], data['body']['data'][self.length-1]['y'])
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
        return 'Snake: head: '+ self._head+ 'tail: '+ self._tail+ ' health: '+ self.health+ ' length: '+ self.length
    
    def get_id(self):
        return self._id