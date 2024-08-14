class Solution:
    def middleNode(self, head):
        root, n = head, 0
        while head:
            head = head.next
            n += 1
        for _ in range(n // 2):
            root = root.next
        return root
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow