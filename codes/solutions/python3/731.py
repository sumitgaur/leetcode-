class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True


from sortedcontainers import SortedList


class MyCalendarTwo1:

    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        i = self.events.bisect_left([start, end])
        if (i > 1 and self.events[i - 1][1] > start) or (i + 1 < len(self.events) and self.events[i + 1][0] < end):
            return False
        self.events.add([start, end])
        return True


mc = MyCalendarTwo1()
mc.book(10, 20)
mc.book(50, 60)
mc.book(10, 40)
mc.book(5, 15)
mc.book(5, 10)
mc.book(25, 55)
