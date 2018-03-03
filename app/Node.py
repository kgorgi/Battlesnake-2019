class Node(object):
    def __init__(self, point):

        self._point = point

        # Absolute Distance To Goal
        self._goal_dist = 0

        # Path Distance to Start
        self._start_dist = 0

        self._parent = None

    def get_point(self):
        return self._point

    def get_distance_to_start(self):
        return self._start_dist

    def get_distance_to_goal(self):
        return self._goal_dist

    def set_distance_to_start(self, value):
        self._start_dist = value

    def set_distance_to_goal(self, value):
        self._goal_dist = value

    def get_parent(self):
        return self._parent

    def set_parent(self, value):
        self._parent = value
    
    def reset_astar(self):
        self._goal_dist = 0
        self._start_dist = 0
        self._parent = None
