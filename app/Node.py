class Node(object):
    def __init__(self, point):

        self._point = point

        # Absolute Distance To Goal (H)
        self._goal_dist = 0

        # Path Distance to Start (G)
        self._start_dist = 0

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
