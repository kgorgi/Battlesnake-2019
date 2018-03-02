from Node import Node

def getNeighbours(point,grid):
    
    x,y=point
    width = len(grid[0])
    height = len(grid)

    valid_adjecent=[]
    if x-1>=0:
        valid_adjecent.append((x-1,y))
    if y-1>=0:
        valid_adjecent.append((x,y-1))
    if x+1<width:
        valid_adjecent.append((x+1,y))
    if y+1<height:
        valid_adjecent.append((x,y+1))        

    neighbours = [grid[d[0]][d[1]] for d in valid_adjecent]
    
    return neighbours

def chooseNext(node):
    return node.G+node.H

def manhattan(node,food):
    x, y = node.point
    xf, yf = food.point
    return abs(x - xf) + abs(y - yf)
        


#returns list of nodes
def aStar(start,end,grid):

    #nodes connected to cloud
    not_visited = set()
    #nodes in cloud
    visited = set()

    current = start
    not_visited.add(current)

    while not_visited:
        #find next node to visit
        current =min(not_visited,key=chooseNext)

        if(current==end):
            path=[]
            while current.parent:
                path.append(current)
                current=current.parent
            path.append(current)
            #reverses list
            return path[::-1]
        not_visited.remove(current)
        visited.add(current)
        for node in getNeighbours(current.point,grid):
            if node in visited:
                continue
            if node in not_visited:
                #updating move cost
                new_g = current.G+1  #put move cost
                if node.G>new_g:
                    node.G = new_g
                    node.parent=current
            else:
                node.G=current.G+1 #put move cost
                node.H=manhattan(node,end)
                node.parent=current
                not_visited.add(node)
                



def main():
    grid = [['a','b','c'],['d','e','f'],['g','h','i']]
    getNeighbours((0,0),grid)
    getNeighbours((1,1),grid)
    getNeighbours((2,0),grid)
    

if __name__=="__main__":
    main()