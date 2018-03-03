from Node import Node
from Food import Food
from SnakeNode import SnakeNode
from SnakeInfo import SnakeInfo

class Board:
    def __init__(self, data):
        self._width = data['width']
        self._height = data['height']
        self._nodes = dict()

        self._food_list = []
        self._enemy_list = []

        self._our_snake = None

        our_id = data['you']['id']
        
        # Process Snakes
        for snake in data['snakes']['data']:
            snake_info = SnakeInfo(snake, self,our_id)

            if snake_info.is_enemy():
                self._enemy_list.append(snake_info)
            else:
                self._our_snake = snake_info

            for point in snake['body']['data']:
                new_snake = SnakeNode(point, snake_info)
                self._nodes[new_snake.get_point()] = new_snake

        # Process Food
        for raw_data in data['food']['data']:
            new_food = Food(raw_data)
            self._food_list.append(new_food)
            self._nodes[new_food.get_point()] = new_food
        
    def get_node(self, point):
        x, y = point
        if x < 0 or x > self._width or y < 0 or y > self._height:
            raise Exception("Invalid Location")
        elif (x,y) in self._nodes:
            return self._nodes[(x, y)]
        else:
            return None

    def get_enemies(self):
        return self._enemy_list

    def get_food_list(self):
        return self._food_list

    def get_our_snake(self):
        return self._our_snake  

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def add_blank(self, point):
        new_node = Node(point)
        self._nodes[point] = new_node
        return new_node

    # Legend: 
    # F = Food
    # S = Snake  
    # X = Enemy Snakes
    # N = Empty Node
    # 0 = Uninitalized
    def __str__(self, show_empty_nodes = False):
        lines = []

        for j in range(0, self._height):
            line = []
            for i in range(0, self._width):
                loc = (i,j)
                if loc in self._nodes:
                    node = self._nodes[loc]
                    if isinstance(node, Food):
                        line.append("F")
                    elif isinstance(node, SnakeNode):
                        snake_info = node.get_snake_info()
                        if snake_info.is_enemy():
                            line.append("X")
                        else:
                            line.append("S") 
                    else:
                        line.append("N" if show_empty_nodes else "0")
                else:
                    line.append("0")
            lines.append(" ".join(line))
        
        return "\n".join(lines)
    
        

        

