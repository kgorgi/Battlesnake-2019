from pathing.astar import aStar
from pathing.Neighbours import get_neighbours, FoodFilter, SnakePartFilter

class Tails:
    def __init__(self, board):
        self.board = board
        self.food_list = board.get_food_list()
    
    def path_to_tail(self):
        snake_tails = [info.get_tail() for info in self.board.get_enemies()]
        snake_tails.append(self.board.get_our_snake().get_tail())
        path_to_tail = aStar(self.board.get_our_snake().get_head(),snake_tails,self.board,SnakePartFilter(snake_tails))
        return None
    
    def find_path(self):
        fpath = self.path_to_tail()
        if not fpath:
                return self.stall()
        fpath.reverse()

        while not self.is_viable(fpath) :
            idx = self.food_list.index(fpath[-1])
            if idx >= len(self.food_list): return self.stall()
            else: self.food_list = self.food_list[idx+1:]
            fpath = self.path_to_tail()
            if not fpath:
                return self.stall()
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
