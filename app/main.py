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
from pathing.astar import aStar
from pathing.Neighbours import get_neighbours, FoodFilter, SnakePartFilter
from pathing.Path import Path
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

    path = Path(board).find_path()

    direction = ""
    if path is None or snake.length < 2 or data['turn'] < 2:
        neighbours = get_neighbours(snake.get_head().get_point(), board, FoodFilter())
        if len(neighbours) <= 0:
            return "down"
        direction = dir(snake.get_head(), neighbours[0])
    else:
        direction = dir(snake.get_head(), path[1])
    
    print direction

    return HTTPResponse(
        status = 200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
        'move': direction,
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
