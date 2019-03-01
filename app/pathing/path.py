from astar import aStar
from SnakeNode import SnakeNode
from Neighbours import get_neighbours
from filters import FoodFilter, SnakePartFilter

# This class to be fazed out into sub classes
class Path:
    def __init__(self, board):
        self.board = board
        self.food_list = board.get_food_list()
    
    def food_path(self):
        snake_heads = [info.get_head() for info in self.board.get_enemies()]
        snake_heads.append(self.board.get_our_snake().get_head())
        for food in self.food_list:
            food_to_head = aStar(food,snake_heads,self.board,SnakePartFilter(snake_heads))
            if not food_to_head: continue
            if food_to_head[-1] == self.board.get_our_snake().get_head(): 
                return food_to_head
        return None

    def path_to_tail(self):
        snake_tails = [info.get_tail() for info in self.board.get_enemies()]
        snake_tails.append(self.board.get_our_snake().get_tail())
        path_to_tail = aStar(self.board.get_our_snake().get_head(),snake_tails,self.board,SnakePartFilter(snake_tails))
        return path_to_tail
    
    def find_path(self):
        fpath = self.food_path()
        if not fpath:
                return self.stall()
        fpath.reverse()

        while not self.is_viable(fpath) :
            idx = self.food_list.index(fpath[-1])
            if idx >= len(self.food_list): return self.stall()
            else: self.food_list = self.food_list[idx+1:]
            fpath = self.food_path()
            if not fpath:
                return self.stall()
            fpath.reverse()
            
        return fpath

    def stall(self):
        
        us = self.board.get_our_snake()
        path= self.path_to_tail()
        
        if path and isinstance(path[-1],SnakeNode) and path[-1].get_snake_info().health == 100 and len(path)<=2:
            return None


        return path


    def is_viable(self,path):
        us = self.board.get_our_snake()
        path_check = aStar(path[1],us.get_tail(),self.board,SnakePartFilter([us.get_tail()]))

        if not path_check:
            return False
        
        return path_check
