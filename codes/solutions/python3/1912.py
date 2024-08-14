from typing import List

from sortedcontainers import SortedList
from collections import defaultdict


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie_shop_map = defaultdict(SortedList)
        self.shop_map = defaultdict(dict)
        self.rented_movies = SortedList()
        for s, m, p in entries:
            self.movie_shop_map[m].add([p, s, m])
            self.shop_map[s][m] = p

    def search(self, movie: int) -> List[int]:
        return [s for p, s, m in self.movie_shop_map[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        shops = self.movie_shop_map[movie]
        p = self.shop_map[shop][movie]
        shops.remove([p, shop, movie])
        self.rented_movies.add([p, shop, movie])

    def drop(self, shop: int, movie: int) -> None:
        p = self.shop_map[shop][movie]
        self.movie_shop_map[movie].add([p, shop, movie])
        self.rented_movies.remove([p, shop, movie])

    def report(self) -> List[List[int]]:
        return [[s, m] for _, s, m in self.rented_movies[:5]]


entries = [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]
movie_renting_system = MovieRentingSystem(len(entries), entries)
print(movie_renting_system.search(1))
movie_renting_system.rent(0, 1)
movie_renting_system.rent(1, 2)
print(movie_renting_system.report())
movie_renting_system.drop(1, 2)
print(movie_renting_system.search(2))
