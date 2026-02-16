# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root, i, last, first = head, 1, None, None
        if head and head.next: first = head.next
        while head:
            latter = head.next
            if i % 2 != 0: last = head
            if head.next: head.next = head.next.next
            head, i = latter, i + 1
        if last: last.next = first
        return root


a = [2, 1, 3, 5, 6, 4, 7]
res = [2, 3, 6, 7, 1, 5, 4]
assert a == res
j=0
for i in range(len(a)):
    if i%2!=0:



