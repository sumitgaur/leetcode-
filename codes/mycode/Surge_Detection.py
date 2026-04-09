from collections import defaultdict, deque


class SurgeTracker:
    city_order = defaultdict(deque)
    TimeWindow = 60

    def __init__(self, threshold):
        self.Threshold = threshold

    def add_order(self, order_id, city, timestamp):
        self.city_order[city].append([order_id, timestamp])

    def get_city_status(self, city, timestamp):
        city_orders = self.city_order.get(city, None)
        while city_orders and city_orders[0][1] < timestamp - self.TimeWindow:
            city_orders.popleft()
        return 'HIGH_DEMAND' if len(city_orders) > self.Threshold else 'NORMAL'


tracker = SurgeTracker(threshold=3)

tracker.add_order(1, "Barcelona", 10)
tracker.add_order(2, "Barcelona", 20)
tracker.add_order(3, "Barcelona", 30)
tracker.add_order(4, "Barcelona", 40)

print(tracker.get_city_status("Barcelona", 80))

