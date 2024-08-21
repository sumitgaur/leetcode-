import heapq
def build_master_playlist(playlists):
    heap=[]
    master_playlist=[]
    for i,playlist in enumerate(playlists):
        if playlist:
            heap.append((playlist.pop(0),i))
    heapq.heapify(heap)
    # print(heap)
    while heap:
        song,playlist_ind = heapq.heappop(heap)
        master_playlist.append(song)
        if len(playlists[playlist_ind]):
            heapq.heappush(heap,(playlists[playlist_ind].pop(0),playlist_ind))
    return master_playlist
# playlists = [["2024-01-01", "2024-01-04", "2024-01-07"],["2024-01-02", "2024-01-05", "2024-01-08"],["2024-01-03", "2024-01-06", "2024-01-09"]]
# playlists = [["2024-01-01"],["2024-01-01", "2024-01-05", "2024-01-08"],["2024-01-03", "2024-01-06", "2024-01-09"]]
# playlists = [["2024-01-01", "2024-01-01", "2024-01-01"],["2024-01-02", "2024-01-05", "2024-01-08"],["2024-01-03", "2024-01-06", "2024-01-09"]]
# playlists = [["2024-01-01", "2024-01-01", "2024-01-01"],["2024-01-02", "2024-01-05", "2024-01-08"],[]]
playlists = [["2024-01-01", "2024-01-01", "2024-01-01"],["2024-01-02", "2024-01-05", "2024-01-08"],["2024-01-03", "2024-01-06", "2024-01-09"]]
m = build_master_playlist(playlists)
print(m)