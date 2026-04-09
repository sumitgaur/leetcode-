def assign_driver(drivers, riders):
    for rider_id, xr, yr in riders:
        heap = []
        for driver, xd, yd in drivers:
            dx = xr - xd
            dy = yr - yd
            dist = dx*dx+dy*dy

