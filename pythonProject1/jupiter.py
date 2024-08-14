# City with infinite number of lakes, initially lakes are all empty, lakes have  states - full or empty
# rains = [1, 2, 0, 0, 2, 1]  n days  ith value represent lake number
#  1. you can dry out any lake, one lake can be dried out in a day
#  2. if rain is falling on the same lake, then we have flood
#
# We can avoid the flood
#
import heapq


# rains = [1, 2, 0, 2, 0, 1]
# l1- 1
# l2-1
# l2-0
# l2-1
# l1-0
# l1-1
#
# l1,l2-1  none is flood
#
#
# lake state map
# {
#     1:1,
#     2:1
# }
#
# {
#     1:0,5  // avoid flood here
#     2:1,3   // avoid flood
#     3:2  // sorted
# }
#
# next = [5,3]
#
#
# 1. For each A[i] compute next[i] which is the index of the element equals to A[i], if no such element then next[i]=-1
#
# 2.  Maintain a set of active lakes, min heap to keep the next of active lakes


def avoidFlood(A):
    days = len(A)
    next = [-1] * days
    m = {}
    for i in range(days):
        if A[i] > 0:
            if A[i] in m:
                next[m[A[i]]]=i
            else:
                m[A[i]]=i
    s=set()
    mh=[]
    for i in range(days):
        if A[i]>0:
            if next[i]==-1: continue
            heapq.heappush(mh,next[i])
            s.add(A[i])
        else:
            if not mh:
                return False
            else:
                j=mh[0]
                heapq.heappop(mh)
                s.remove(A[j])

    return True





