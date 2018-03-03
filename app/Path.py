from astar import aStar
from Neighbours import get_neighbours, FoodFilter, SnakePartFilter

class Path:
    def __init__(self, board):
        self.board = board
        self.food_list = board.get_food_list()
    
    def food_path(self):
        snake_heads = [info.get_head() for info in self.board.get_enemies()]
        snake_heads.append(self.board.get_our_snake().get_head())
        for food in self.food_list:
            food_to_head = aStar(food,snake_heads,self.board,SnakePartFilter(snake_heads))
            if food_to_head[-1] == self.board.get_our_snake().get_head(): 
                return food_to_head
        return None
    
    def find_path(self):
        fpath = self.food_path()
        fpath.reverse()

        while not self.is_viable(fpath) :
            if not fpath:
                return self.stall()
            self.food_list = self.food_list[self.food_list.index(fpath[0])+1:]
            fpath = self.food_path()
            fpath.reverse()
            
        return fpath

    def stall(self):
        us = self.board.get_our_snake()
        return aStar(us.get_head(),us.get_tail(),self.board,SnakePartFilter([us.get_tail]))


    def is_viable(self,path):
        us = self.board.get_our_snake()
        path_check = aStar(path[1],us.get_tail(),self.board,SnakePartFilter([us.get_tail()]))

        if not path_check:
            return False
        
        return path_check
