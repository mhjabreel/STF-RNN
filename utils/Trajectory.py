from . import Point
from copy import copy, deepcopy 

class Trajectory(object):
    
    def __init__(self, points=None, **kwargs):
        
        if points is None:
            self.points = []
        elif isinstance(points, list):
            assert all([isinstance(p, Point) for p in points])
            self.points = copy(points)
        else:
            raise Exception("Unsupported type %s." % type(points))

    def add(self, p):
        if not isinstance(p, Point):
            raise Exception("Unsupported type, expected Point, got %s." % type(points))
        self.points.append(p)

    def insert(self, index, p):
        if not isinstance(p, Point):
            raise Exception("Unsupported type, expected Point, got %s." % type(points))
        self.points.insert(index, p)

    def remove_at(self, index):
        del self.points[index]

    def remove(self, p):
        if not isinstance(p, Point):
            raise Exception("Unsupported type, expected Point, got %s." % type(points))
        self.points.remove(p)

    def clear(self):
        self.points = []

    def __iter__(self):
        return iter(self.points)

    def __getitem__(self,index):
        return self.points[index]

    def __len__(self):
        return len(self.points)

    def __repr__(self, **kwargs):
        s = "["
        p = [str(p_) for p_ in self.points]

        return "[" + "=>".join(p) + "]"

    def __str__(self, **kwargs):
        return self.__repr__(**kwargs)


