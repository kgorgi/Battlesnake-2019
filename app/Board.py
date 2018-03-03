import pprint
from Node import Node
class Board:
    def __init__(self, data):
        self.width = data['width']
        self.height = data['height']
        self.board = self.init_board(data)
    

    def init_board(self, data):
        #Board is generated as a 2D array with 0's occupying all possitons.
        #enemy snake bodies are possitioned on the board as 2's and food is 3
        #location of food can also be accessed with the food object

        board = [[Node(0, (y,x)) for x in range(self.width)] for y in range(self.height)] #2d array filled with all 0

        enemies_list = []
        enemies = data['snakes']['data']
        for food in data['food']['data']:
            board[food['y']][food['x']] = Node(1, (food['x'], food['y']))
          
        
        #place body on board
        for snake in enemies:
            for body in snake['body']['data']:
                board[body['y']][body['x']] = Node(3, (body['x'], body['y']))

        for body in data['you']['body']['data']:
            board[body['y']][body['x']] = Node(2, (body['x'], body['y']))
        #pprint.pprint(board)
        return board

