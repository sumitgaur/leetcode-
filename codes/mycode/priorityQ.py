from queue import PriorityQueue


class PQEntity:
    def __init__(self, x, n):
        self.p = x
        self.n = n

    def __lt__(self, other):
        return self.p > other.p


customers = PriorityQueue()  # we initialise the PQ class instead of using a function to operate upon a list.
customers.put(PQEntity(2, "Harry"))
customers.put(PQEntity(3, "Charles"))
customers.put(PQEntity(1, "Riya"))
customers.put(PQEntity(4, "Stacy"))
while customers:
    print(customers.get().n)
