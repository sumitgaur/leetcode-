# Definition for singly-linked list.
import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        elif not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def merge(self,l1,l2):
        res = ListNode(-1)
        head=res
        while l1 or l2:
            if (l1.val if l1 else sys.maxsize) > (l2.val if l2 else sys.maxsize):
                res.next, l2 = ListNode(l2.val), l2.next
            else:
                res.next, l1 = ListNode(l1.val), l1.next
            res=res.next
        return head.next

head = None
head1 = ListNode(0)
# head1.next = ListNode(3)
# head1.next.next = ListNode(4)

c=Solution().merge(head,head1)
while c:
    print(c.val)
    c=c.next