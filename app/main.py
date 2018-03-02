import bottle
import os
import random
import json
import pprint
from Board import Board
from Food import Food
from Snake import Snake


@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

def init_food(data, snake):
    list = []
    for food in data['food']['data']:
        list.append(Food(food, snake))

    return list

def dir(snake, food):
    if snake.x > food.x:
        return 'left'
    elif snake.x<food.x:
        return 'right'
    if snake.y > food.y:
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
    #enemy_list = init_enemies(data['snakes'])
    snake = Snake(data['you'])
    food = init_food(data, snake) #list of food in ordered by closest distance to snake
    
    
    directions = ['up', 'down', 'left', 'right']
    direction = dir(snake, food[0]) #passing in first item of food list for testing
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
