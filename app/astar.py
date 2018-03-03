from Node import Node
from Snake import Snake

def getNeighbours(point, board):
    x,y = point

    valid_adjacent = []

    if x - 1 >= 0:
        valid_adjacent.append((x-1,y))
    if y-1 >= 0:
        valid_adjacent.append((x,y-1))
    if x + 1 < board.get_width():
        valid_adjacent.append((x+1,y))
    if y + 1 < board.get_height():
        valid_adjacent.append((x,y+1))        

    neighbours = []
    for point in valid_adjacent:
        node = board.get_node(point)

        if node is None:
            node = board.add_blank(point)

        if not isinstance(node, Snake):
            neighbours.append(node)
    
    return neighbours



def chooseNext(node):
    return node.get_distance_to_start() + node.get_distance_to_goal()

def manhattan(node, food):
    x, y = node.get_point()
    xf, yf = food.get_point()
    return abs(x - xf) + abs(y - yf)
        
#returns list of nodes
def aStar( start, end, board):

    #nodes connected to cloud
    not_visited = set()
    
    #nodes in cloud
    visited = set()

    current = board.get_node(start)
    not_visited.add(current)

    while not_visited:
        #find next node to visit
        current = min(not_visited , key = chooseNext)

        if(current.get_point() == end.get_point()):
            path = []
            while current.get_parent():
                path.append(current)
                current = current.get_parent()
            
            path.append(current)
            #reverses list
            return path[::-1]
        
        not_visited.remove(current)
        visited.add(current)
        
        for node in getNeighbours(current.get_point(), board):
            if node in visited:
                continue
            if node in not_visited:
                #updating move cost
                new_g = current.get_distance_to_start() + 1  #put move cost
                if node.get_distance_to_start() > new_g:
                    node.set_distance_to_start(new_g)
                    node.set_parent(current)
            else:
                node.set_distance_to_start(current.get_distance_to_start() + 1) #put move cost
                node.set_distance_to_goal(manhattan(node,end))
                node.set_parent(current)
                not_visited.add(node)
    
    return None           
