# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        q = []
        for i in range(len(lists)):
            while lists[i]:
                q.append(lists[i]),
                lists[i] = lists[i].next
        root = cur = ListNode(0)
        for h in sorted(q, key=lambda x: x.val):
            cur.next = cur = h
        return root.next

    def merge_list(self, lists):
        heap = []
        head = cur = ListNode(-1)
        for l in lists:
            heap.append(l.val, l.next)
        heapq.heapify(heap)
        while heap:
            x, l = heap.pop()
            cur.next = ListNode(x)
            if l:
                heapq.heappush(heap, (l.val, l.next))
        return head.next

l = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = []
for x in l:
    ll = ListNode(-1)
    h = ll
    for i in x:
        ll.next = ListNode(i)
        ll = ll.next
    lists.append(h.next)
res = Solution().mergeKLists(lists)
while res:
    print(res.val)
    res = res.next
