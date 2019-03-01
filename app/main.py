import bottle
from bottle import HTTPResponse
import os
import random
import json
import pprint
from Node import Node
from Board import Board
from Food import Food
from SnakeNode import SnakeNode
from pathing.find_path import find_path
from pathing.path import Path
from pathing.util_path import direction

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')




@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game']['id']
    board_width = data['board']['width']
    board_height = data['board']['height']

    return {
        'color': '#00f2ff',
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    board = Board(data)
    snake = board.get_our_snake()
    food = board.get_food_list()

    path = find_path(board)

    new_direction = direction(path,snake,data,board)

    return HTTPResponse(
        status = 200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
        'move': new_direction,
        'taunt': 'battlesnake-python!'
        })
    )

@bottle.post('/ping')
def ping():
    return bottle.HTTPResponse(status=200)

@bottle.post('/end')
def end():
    data = bottle.request.json

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return HTTPResponse(status=200)

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = os.getenv('DEBUG',True)
    )
