from Node import Node
from SnakeNode import SnakeNode
from .neighbours import get_neighbours

def chooseNext(node):
    return node.get_distance_to_start() + node.get_distance_to_goal()

def manhattan(start, end):
    x, y = start.get_point()
    xf, yf = end.get_point()
    return abs(x - xf) + abs(y - yf)

def dist_to_closest(start_node, end_node_list):
    smallest_d = None
    for each in end_node_list:
        d = manhattan(start_node,each)
        if(smallest_d is None or d<smallest_d):
            smallest_d = d
    
    return smallest_d

'''
returns list of nodes to the closest end node from start node

filter_obj parameter:

    Basically a lambda function that defines if a node is an 
    available space that the snake can move onto and through.

    Essentially defines what is a "wall" that the astar needs
    to path around.

    ex:
        FoodFilter = makes it so all snake nodes are walls
        SnakePartFilter = Same as Foodfilter but adds exceptions
            for nodes in the snakes_nodes list
'''
def aStar(start_node, end_node_list, board, filter_obj):
    if(not isinstance(end_node_list,list)):
        end_node_list = [end_node_list]

    #nodes connected to cloud
    not_visited = set()
    
    #nodes in cloud
    visited = set()

    current = start_node
    not_visited.add(current)

    while not_visited:
        #find next node to visit
        current = min(not_visited , key = chooseNext)

        if(current.get_point() in [ x.get_point() for x in end_node_list]):
            path = []
            
            while current.get_parent():
                path.append(current)
                current = current.get_parent()
            
            path.append(current)
            #reverses list

            for each in visited:
                each.reset_astar()
            for each in not_visited:
                each.reset_astar()
            return path[::-1]
        
        not_visited.remove(current)
        visited.add(current)
        
        for node in get_neighbours(current.get_point(), board, filter_obj):
            if node in visited:
                continue

            dist_to_start = current.get_distance_to_start() + (node.get_move_cost()/(current.get_distance_to_start()+1))
            if node in not_visited:
                #updating move cost
                new_g = dist_to_start
                if node.get_distance_to_start() > new_g:
                    node.set_distance_to_start(new_g)
                    node.set_parent(current)
            else:
                node.set_distance_to_start(dist_to_start)
                node.set_distance_to_goal(dist_to_closest(node,end_node_list))
                node.set_parent(current)
                not_visited.add(node)

    for each in visited:
        each.reset_astar()
    for each in not_visited:
        each.reset_astar()
    
    return None           
