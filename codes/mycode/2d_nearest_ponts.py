import heapq
from collections import defaultdict


def nearest_drivers(drivers, rider, k):
    '''
    # O(k+nlogk)
    :param drivers:
    :param rider:
    :param k:
    :return:
    '''
    heap = []

    for id_, driver in enumerate(drivers):
        dx = driver[0] - rider[0]
        dy = driver[1] - rider[1]
        dist = dx * dx + dy * dy
        if len(heap) < k:
            heapq.heappush(heap, (-dist, id_))
        else:
            heapq.heappushpop(heap, (-dist, id_))
    return heap


def nearest_drivers_grid(drivers, rider, k):
    cell_width = 100
    cell_height = 100
    min_lat, min_lon = 0, 0
    mp = defaultdict(list)
    for i, driver in enumerate(drivers):
        row = (driver[0] - min_lat) // cell_height
        col = (driver[1] - min_lon) // cell_width
        mp[(row, col)] = i
    row = (rider[0] - min_lat) // cell_height
    col = (rider[1] - min_lon) // cell_width

    return nearest_drivers(mp[(row, col)], rider, k)


drivers = [
    (0, 0),
    (1, 1),
    (5, 5)
]
rider = (0, 0)
k = 2
res = (nearest_drivers(drivers, rider, k))
print(res)


