

def get_neighbours(point, board, filter_obj):
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

        # Add empty node if available
        if node is None:
            node = board.add_blank(point)

        #Configurable check to see if move is open
        if filter_obj.is_neighbour(node):
            neighbours.append(node)
    
    return neighbours






