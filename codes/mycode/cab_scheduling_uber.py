import math


def make_ntrips(n, cab_travel_time):
    max_time = n * cab_travel_time[0]
    i, j = 1, max_time
    best = max_time
    while i <= j:
        m = (i + j) // 2
        t = 0
        for x in cab_travel_time:
            t += (m // x)
        if t < n:
            i = m + 1
        else:
            best = m
            j = m - 1
    print(best)
    return best


# [1-10]
# [6-10] 8
# [6-8] 7

n = 3
cabTravelTime = [3, 4, 8]
n = 10
cabTravelTime = [1, 3, 5, 7, 8]
make_ntrips(n, cabTravelTime)
