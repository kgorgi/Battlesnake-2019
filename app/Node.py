class Node:
    def __init__(self,value,point):
        #if the node is visitable
        self.value=value

        self.point=point

        #abs dist to goal
        self.H=0

        #path dist fom start
        self.G=0

        self.parent=None

        def __str__(self):
            return self.point

        def moveCost(self, node):
            return 1
