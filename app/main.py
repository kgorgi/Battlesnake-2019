import bottle
import os
import random
import json
import pprint
from Node import Node
from Board import Board
from Food import Food
from SnakeNode import SnakeNode
from astar import aStar
from Neighbours import get_neighbours, FoodFilter, SnakePartFilter
from Path import Path
@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

def dir(snake_head, next_node):
    x,y = next_node.get_point()
    sx,sy = snake_head.get_point()

    if x > sx:
        return 'right'
    elif x < sx:
        return 'left'
    if y > sy:
        return 'down'
    else:
        return 'up'


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game']['id']
    board_width = data['board']['width']
    baord_height = data['board']['width']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    return {
        'color': '#00f2ff',
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    board = Board(data)
    snake = board.get_our_snake()
    food = board.get_food_list()

    path = Path(board).find_path()

    direction = ""
    if path is None or snake.length < 2 or data['turn'] < 2:
        neighbours = get_neighbours(snake.get_head().get_point(), board, FoodFilter())
        if len(neighbours) < 0:
            return "down"
        direction = dir(snake.get_head(), neighbours[0])
    else:
        direction = dir(snake.get_head(), path[1])
    
    print direction

    return {
        'move': direction,
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
