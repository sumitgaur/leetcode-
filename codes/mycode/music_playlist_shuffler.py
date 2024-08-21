import random
from collections import deque


class MusicPlaylistShuffler:
    def __init__(self, songs, k):
        self.songs = songs
        self.K = k
        self.k = 0
        self.j = 0

    def pick_song(self):
        """
        It should return some randomly chosen song which was not played in last K plays
        """
        idx = random.randint(self.j, len(self.songs) - 1)
        song = self.songs[idx]
        self.songs[self.k], self.songs[idx] = self.songs[idx], self.songs[self.k]
        if self.k == self.K:
            self.k = 0
        else:
            self.j += 1
            self.k += 1
        return song


# [1, 2, 3, 4, 5, 6, 7, 8]
# K == 3, i = 0, n - 1
# [5, 2, 3, 4, 1, 6, 7, 8]
# play = 5, i = 1, n - 1
# [5, 4, 3, 2, 1, 6, 7, 8]
# play = 4, i = 2, n - 1
# [5, 4, 7, 2, 1, 6, 3, 8]
# play = 7, i = 2
#
# [5, 4, 7]
shuffler = MusicPlaylistShuffler([1, 2, 3, 4, 5, 6, 7, 8], 3)
i = 0
while i < 10:
    print(shuffler.pick_song())
    i += 1
