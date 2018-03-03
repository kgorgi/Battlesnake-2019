import bottle
import os
import random
import json
from Node import Node
from Board import Board
from Food import Food
from Snake import Snake
from astar import aStar, getNeighbours

@bottle.route('/')
def static():
    return "the server is running"

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

def dir(snake, food, board):
    path_list = aStar(snake.head, food, board)

    x, y = 0, 0
    if path_list is None:
        # No Direct Path, Choose The First Neighbour
        neighbours = getNeighbours(snake.head, board)
        if len(neighbours) == 0:
            # Time to DIE
            print("RIP")
            return "down"
        x, y = neighbours[0].get_point()
    else:
        x, y = path_list[1].get_point()
    
    sx, sy = snake.head
    
    if x > sx:
        return 'right'
    elif x < sx:
        return "left"
    elif y > sy:
        return "down"
    else: 
        return "up"


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00f2ff',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': 'https://files.gamebanana.com/img/ico/sprays/516c32f08e03d.png',
        "head_type": 'fang',
        'tail_type': 'skinny'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    board = Board(data)

    snake = board.get_snake()
    food = board.get_food_list()
    
    direction = dir(snake, food[0], board)

    print board
    print direction

    return {
        'move': direction,
        'taunt': 'Monty Python in Python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
