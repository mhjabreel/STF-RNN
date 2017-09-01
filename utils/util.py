from . import *
from sklearn.cluster import DBSCAN
from glob import glob

def get_interest_point_candidates(trajectory, min_dist, min_time):

    i = 0
    pointNum = len(trajectory)
    interestPoints = []
    

    while i < pointNum:
        j = i + 1
        token = False

        pi = trajectory[i]
        while j < pointNum:

            pj = trajectory[j]
            dist, tm = pi - pj

            if dist > min_dist:
                if tm > min_time:
                    l = 0.0
                    g = 0.0
                    n = 0.0
                    for p in trajectory[i:j + 1]:
                        l += p.lat
                        g += p.long
                        n += 1
                    l /= n
                    g /= n
                    
                    interestPoints.append(StayPoint(l, g, pi.datetime, pj.datetime))
                    i = j
                    token = True
                # End if

                break
            # End if

            j += 1

        # End while
        if not token: i += 1

    # End while

    return interestPoints
# End function

def read_data(data_path):
    traj = Trajectory()
    for file_name in glob(data_path):
        with open(file_name) as fin:

            lines = list(fin)
        
            for line in lines[6:]:
                vals = line.split(',')
                traj.add(Point(vals[0], vals[1], vals[-2], vals[-1]))
    return traj

def prpare_data(traj, window_size=3, min_dist=0.2, min_time=1800):
    candidate_points = get_interest_point_candidates(traj, min_dist, min_time)

    #print(candidate_points)
    #print(len(candidate_points))

    s = [(p.lat, p.long) for p in candidate_points]

    db = DBSCAN(eps=0.1, min_samples=10).fit(s)
    #print(len(set(db.labels_)))

    #label_points = {}
    point2lbl = {}

    for l, p in zip(db.labels_, candidate_points):
        l += 1
        point2lbl[p] = l

        #if not l in label_points:
        #    label_points[l] = []

        #label_points[l].append(p)

    time_input = []
    space_input = []

    p = candidate_points[0]
    curr_label = point2lbl[p]

    for p in candidate_points:
        l = point2lbl[p]
        if l != curr_label:
            space_input.append(l)
            time_input.append(p.lev_time.hour - 1)
            curr_label = l

    n = len(space_input)
    space_inputs = []
    time_inputs = []
    outputs = []

    for i in range(n - window_size):
        space_inputs.append(space_input[i: i + window_size])
        time_inputs.append(time_input[i: i + window_size])
        outputs.append(space_input[i + window_size ]) 

    return space_inputs, time_inputs, outputs, len(set(db.labels_))


