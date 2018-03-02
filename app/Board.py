import pprint
class Board:
    def __init__(self, data):
        self.width = data['width']
        self.height = data['height']
        self.board, self.food = self.init_board(data)
    

    def init_board(self, data):
        #Board is generated as a 2D array with 0's occupying all possitons.
        #enemy snake bodies are possitioned on the board as 2's and food is 3
        #location of food can also be accessed with the food object
        
        board = [[0 for x in range(self.width)] for y in range(self.height)] #2d array filled with all 0

        food_list = []
        enemies_list = []
        enemies = data['snakes']['data']
        for food in data['food']['data']:
            board[food['y']][food['x']] = '3'
            food_list.append(food)
        
        #place body on board
        for snake in enemies:
            for body in snake['body']['data']:
                board[body['y']][body['x']] = 2
                #self.enemies_list.append((body['x'], body['y']))

        for body in data['you']['body']['data']:
            board[body['y']][body['x']] = 1

        self.food = data['food']['data'][0]

        pprint.pprint(board)

        return board, food
