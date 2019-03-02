from Node import Node
from Food import Food
from SnakeNode import SnakeNode
from SnakeInfo import SnakeInfo
from FaceNode import FaceNode
import operator

class Board:
    def __init__(self, data):
        self._turn = data['turn']
        self._width = data['board']['width']
        self._height = data['board']['height']
        self._nodes = dict()

        self._food_list = []
        self._enemy_list = []

        self._our_snake = None

        our_id = data['you']['id']
        
        # Process Snakes
        for snake in data['board']['snakes']:
            snake_info = SnakeInfo(snake, self, our_id)

            if snake_info.is_enemy():
                self._enemy_list.append(snake_info)
                head = snake['body'][0]
                for op in [(1,0),(0,1),(0,-1),(-1,0)]:
                    px = head['x']+op[0]
                    py = head['y']+op[1]
                    if px > self.get_width or px < 0 or py < 0 or py > self.get_height:
                        continue
                    else:
                        self._nodes[(px,py)] = FaceNode((px,py),snake_info)

            else:
                self._our_snake = snake_info

            for point in snake['body']:
                new_snake = SnakeNode(point, snake_info)
                self._nodes[new_snake.get_point()] = new_snake

        snake_head = self._our_snake.get_head()
        # Process Food
        for raw_data in data['board']['food']:
            new_food = Food(raw_data, snake_head)
            self._food_list.append(new_food)
            self._nodes[new_food.get_point()] = new_food
        
        self._food_list = sorted(self._food_list, key=operator.attrgetter('_start_distance'))

        for x in range(0,int(self.get_width())-1):
            for y in range(0,int(self.get_height())):
                if(not (x,y) in self._nodes):
                    board.add_blank((x,y))


    def get_node(self, point):
        x, y = point
        if x < 0 or x > self._width or y < 0 or y > self._height:
            raise Exception("Invalid Location")
        elif (x,y) in self._nodes:
            return self._nodes[(x, y)]
        else:
            return None

    # def get_snake_heads(self):
    #     snake_heads = [info.get_head() for info in self.board.get_enemies()]
    #     snake_heads.append(self.board.get_our_snake().get_head())
    #     return snake_heads

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

    def get_turn(self):
        return self._turn

    def add_blank(self, point):
        new_node = Node(point)
        self._nodes[point] = new_node
        return new_node

    #ew
    def is_snake_node(self,node):
        return isinstance(node,SnakeNode)


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
                    elif isinstance(node, SnakeNode) or isinstance(node,FaceNode):
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
    
        

        

