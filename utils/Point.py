from datetime import datetime, date, time
from haversine import haversine
import math

class Point(object):
    
    def __init__(self, lat, long=None, the_date=None, the_time=None, **kwargs):

        if isinstance(lat, Point):
            self.lat = lat.lat
            self.long = lat.long
            self.date = lat.date
            self.time = lat.time
            self.datetime = lat.datetime
        elif isinstance(the_date, datetime):
            self.lat = float(lat)
            self.long = float(long)
            self.datetime = the_date
        else:
            self.lat = float(lat)
            self.long = float(long)
        
            d = list(map(int, the_date.split('-')))  
            t = list(map(int, the_time.split(':')))
            dt = d + t
            self.time = time(*t)
            self.date = date(*d)
            self.datetime = datetime(*dt)

    def __sub__(self, p):
        if not isinstance(p, Point): 
            raise Exception("Unexpected type of argument, expected Point, got %s." % type(p))
        return haversine((self.lat, self.long), (p.lat, p.long)), math.fabs((self.datetime - p.datetime).total_seconds())

    def __repr__(self, **kwargs):
        return '({},{})@{}'.format(self.lat, self.long, str(self.datetime))

    def __str__(self, **kwargs):
        return self.__repr__(**kwargs)

    def __eq__(self, p):
        if not isinstance(p, Point): 
            return False

        return self.lat == p.lat and self.long == p.long

    def __hash__(self, **kwargs):
        return hash(self.lat) + hash(self.long)
        





