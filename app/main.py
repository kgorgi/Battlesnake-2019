import bottle
import os
import random
import json
from Board import Board
import pprint


@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


def init_snake(data):
    snake = data['you']
    snake = {
        'health' : snake['health'],
        'x' : snake['body']['data'][0]['x'],
        'y' : snake['body']['data'][0]['y'],
        'length' : len(snake['body']['data'])
    }
    return snake


def dir(snake, food):
    if snake['x'] > food['x']:
        return 'left'
    elif snake['x']<food['x']:
        return 'right'
    if snake['y'] > food['y']:
        return 'up'
    else:
        return 'down'


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
    snake = init_snake(data)
    # TODO: Do things with data
    
    directions = ['up', 'down', 'left', 'right']
    direction = dir(snake, board.food)
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
