class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GlobalLocalMinima:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.local_minimas = []
        self._local_minimas()
        self._global_minima()

    def _local_minimas(self):

        for i in range(1, len(self.coordinates) - 1):
            if self.coordinates[i + 1][1] > self.coordinates[i][1] < self.coordinates[i - 1][1]:
                self.local_minimas.append(self.coordinates[i])

    def _global_minima(self):
        self.global_minima = max(self.local_minimas, key=lambda x: x[1])

    def get_local_minimas(self):
        return self.local_minimas

    def get_global_minimas(self):
        return self.global_minima


if __name__ == '__main__':
    coordinates = [(0, 5), (1, 3), (2, 2), (3, 4), (4, 6), (5, 3), (6, 7)]
    obj = GlobalLocalMinima(coordinates)
    print(obj.get_local_minimas())
    print(obj.get_global_minimas())
