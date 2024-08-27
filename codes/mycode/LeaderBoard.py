import heapq


class Runner:
    def __init__(self, r_id, s_id):
        self.ts = -1
        self.runner_id = r_id
        self.sensor_id = s_id

    def __lt__(self, other):
        return self.ts > other.ts

    def finished_ts(self, ts):
        self.ts = ts


class LeaderBoard:
    def __init__(self, k):
        self.top_k = k
        self.heap = []
        self.sensor_runner = {}

    def add_runner(self, runner):
        self.sensor_runner[runner.sensor_id] = runner

    def event(self, r_id, s_id, ts):
        runner = self.sensor_runner[s_id]
        runner.finished_ts(ts)
        if len(self.heap) < self.top_k:
            heapq.heappush(self.heap, runner)
        else:
            if self.heap[0].ts > runner.ts:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, runner)

    def top_k_runner(self):
        return [[top.runner_id, top.sensor_id, top.ts] for top in self.heap]


leader_board = LeaderBoard(3)

leader_board.add_runner(Runner('r_1', 's_1'))
leader_board.add_runner(Runner('r_2', 's_2'))
leader_board.add_runner(Runner('r_3', 's_3'))
leader_board.add_runner(Runner('r_4', 's_4'))
leader_board.add_runner(Runner('r_5', 's_5'))

leader_board.event('r_1', 's_1', 2)
leader_board.event('r_2', 's_2', 5)
leader_board.event('r_5', 's_5', 3)
leader_board.event('r_4', 's_4', 4)
leader_board.event('r_3', 's_3', 8)
print(leader_board.top_k_runner())
