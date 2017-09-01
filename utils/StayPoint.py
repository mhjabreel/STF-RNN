from datetime import datetime
import math

class StayPoint(object):
    def __init__(self, lat, long, arv_time, lev_time):
        self.lat = lat
        self.long = long
        self.arv_time = arv_time
        self.lev_time = lev_time

    def __repr__(self):

        return "({}, {}, {})".format(self.lat,
                                    self.long,
                                    int(math.fabs((self.arv_time - 
                                                   self.lev_time)
                                                  .total_seconds())))


