# [1, 2, 3, 5, 95, 97, 100] - n = 90 %
# 1 - 100, 100
# values, 90
# values
# [5, 95], 91
# values, length
# 2
#
# [5, 10, 25, 35, 40, 45, 55] - n = 50 %
# 5 - 55, 51
# values, 25.5
# values
# [10, 25, 35], 26
# values, length
# 3
#
# (i, j)
# A[j] - A[i] + 1
# expected
# 26
# values
# (5, 55) = 51
# (10, 55) = 46. - -->
# (5, 45) = 41
# (i, j) = min
# {(i - 1, j) if A[j] - A[i] + 1 > EV
# (i, j - 1))}
#
# O(2 ^ n)
import math
import time
from collections import deque, OrderedDict

from sortedcontainers import SortedList


def find_min_window(arr, n):
    """
    n = [0.0,1.0]
    """
    i = 0
    j = i + 1
    ans = len(arr)
    expected_values_count = math.ceil((arr[-1] - arr[0] + 1) * n)
    while j < len(arr):
        if arr[j] - arr[i] + 1 >= expected_values_count:
            ans = min(ans, j - i + 1)
            i += 1
        else:
            j += 1
    return ans


# arr = [1, 2, 3, 5, 95, 97, 100]
#
# n = 0.9
# print(find_min_window(arr, n))


# O(n) time
# space O(1)
#
#
# P1 - red, striped, short
# sleeve
# P2 - red, striped, long
# sleeve
# P3 - red, striped, short
# sleeve
# P4 - blue, striped, short
# sleeve
# P5 - blue, long
# sleeve
# P6 - blue, striped
#
# red - P3
# striped - P2
# short
# sleeve - P1
# blue - P5
# long
# sleeve - P2
#
# long
# sleeve - P2
# short - P1
# red - P3
# striped - p4
# blue - P5
#
# Attributes
# Universe
# Product
# universe
#
# red ->[p1, p2]  ->[p3]
# blue -> [p4, p5, p6] ->[p5, p6]
# striped ->[p1, p2, p4] ->[p4]
# short
# sleeve -> [p1] -> [x2, y2, z2]
# long
# sleeve -> [p2]  -> [x1, y1, z1]
#
# approach
#
# 1.
# Start
# with attributes with single product nodes[]
# 2.
#
#
#
#
# Please consider this class:


class Logger:
    requestid_start_ts_map = {}

    def Started(self, timestamp, request_id):
        Logger.requestid_start_ts_map[request_id] = timestamp

    def Finished(self, timestamp, request_id):
        start_ts = Logger.requestid_start_ts_map[request_id]
        self.Log(request_id, start_ts, timestamp)
        Logger.requestid_start_ts_map.pop(request_id)

    def Log(self, request_id, start_timestamp, end_timestamp):
        pass


# Provided for you; you do not need to implement
#
# “”” You; will; need; to; add; state; to; the; Logger
#
#
# class and fill in Started and Finished so that; Log is called; according; to; certain; requirements.
# This class will run on a server that; runs for a long time, handling requests from end users.It will call Started when; a; request;
# arrives and Finished; when; it is done; processing; that; request.; Many; requests; may; be; pending; at; the; same; time, but;
# you; may; assume; that; it; will; be; few; enough; to; not consume; a; significant; fraction; of; the; machine’s; resources.;
# You; may; assume; that; the; program is single - threaded, that; all; timestamps; passed; to; all; calls; to; Started and Finished;
# are; monotonically; nondecreasing, that; Started is always; called; on; a; request_id; exactly; once, that; Finished is always; called;
# exactly; once for each Started call having the same request_id, and that Finished is never; called; before; Started; on; a; given; request; ID.
# The; time; between; the; Started and Finished; calls for any given request ID will be short enough that the total; of; all; requests; that; come in
# between; the; two; will; not be; enough; to; consume; a; large; fraction; of; the; machine’s; resources.You; may; assume; Log; takes; constant; time; to; run.
# “””

# 1: Please implement Started and Finished to call Log on all requests in the order of the time they finished.
# started
# request1, 12: 00
# started
# request2, 12: 01
# finished
# request2, 12: 02
# started
# request3
# 12: 0
# 9
# finished
# request3
# 12: 10
# finished
# request1
# 12: 11
#
# log - request2, request3, request1
# request_start_mp = request->ts
# request1->[start, finish]
# finish-> look
# up in the
# map
# for start time for that request then call log
#
# {}
#
# Log
# req2
# Log
# req3
# Log
# req1
#
# # 2: What are the time and space complexities of your solution?
#
# Time
# complexity
# started
# O(1)
# average
# Finished
# TC
# O(1)
# average
# Space
# Compexity
# O(P) - - number
# of
# request
# which
# are
# not yet
# finished is P


# 3: Please implement Started and Finished so that Log is called in ascending order of the time the requests started.

class Logger:
    requestid_start_ts_map = OrderedDict()

    def Started(self, timestamp, request_id):
        Logger.requestid_start_ts_map[request_id] = [timestamp, -1]

    def Finished(self, timestamp, request_id):
        req_id = next(iter(Logger.requestid_start_ts_map))
        Logger.requestid_start_ts_map[request_id][1] = timestamp
        if req_id == request_id:
            to_be_popped = []
            for k, v in Logger.requestid_start_ts_map.items():
                if v[1] != -1:
                    self.Log(k, v[0], v[1])
                    to_be_popped.append(k)
                else:
                    break
            for k in to_be_popped:
                Logger.requestid_start_ts_map.pop(k)

    def Log(self, request_id, start_timestamp, end_timestamp):
        print(request_id, start_timestamp, end_timestamp)
        # Provided for you; you do not need to implement


logger = Logger()
logger.Started(1200, 'req1')
logger.Started(1205, 'req2')
logger.Finished(1207, 'req2')
logger.Started(1212, 'req3')
logger.Finished(1213, 'req1')
logger.Finished(1215, 'req3')
logger.Started(1217, 'req4')
logger.Started(1220, 'req5')
logger.Finished(1222, 'req5')
logger.Finished(1225, 'req4')


#
# started
# request1, 12: 00
# started
# request2, 12: 01
# finished
# request2, 12: 02
# started
# request3
# 12: 0
# 9
# finished
# request3
# 12: 10
# finished
# request1
# 12: 11
#
# mp = {r1->12: 00, -1,
# r2->12: 01, -1}
# r3->

#
# We have a big log file - several gigabytes. Each line contains request/response log - with columns like REQUEST_ID, TIMESTAMP, START/END FLAG. We need to parse file, and print requests ids that exceeded given time threshold. Some of requests contains start log, but has never completed and do not have log with end time.
#
# i.e.
# 1 1 START
# 2 2 START
# 1 4 END
# 3 8 START
# 3 15 END
# And given timeout threshold as 5.
#
# Request 1 started at 1
# Request 2 started at 2
# Request 1 ended at 4 ->4-1 = 3 < 5 - under threshold - it's ok - do nothing.
# Request 3 started at 8 -> In this place we should already know that request 2 started at 2, and 8-2 = 6 what is > 5, that means we should print here that request 2 is timed out.
# Request 3 ended at 15 - >15-8 =7 > 5 -> we shoud print that request 3 timed out.

class LogStartEndTimeStamp:
    def __init__(self, s=None, e=None):
        self.start = s
        self.end = e


class LogChecker:
    def __init__(self, threshold):
        self.ordered_dict = OrderedDict()
        self.timeout_threshold = threshold
        self.log_file = '/home/log/'

    def check_timeout(self, req_id, ts, start_end_flag):
        if start_end_flag == 'START':
            self.ordered_dict[req_id] = LogStartEndTimeStamp(ts)
        else:
            if ts + self.timeout_threshold < time.time():
                self.ordered_dict.pop(req_id)
        timedout_requests = []
        itr = iter(self.ordered_dict)
        while itr:
            req_ = next(itr)
            ts = self.ordered_dict[req_]
            if ts.start + self.timeout_threshold < time.time():
                timedout_requests.append(req_)
            else:
                break
        for r in timedout_requests:
            self.ordered_dict.pop(r)

    def parse_log(self):
        with open(self.log_file) as f:
            self.check_timeout(f.readline())
