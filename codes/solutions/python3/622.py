class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
class MyCircularQueue:

    def __init__(self, k):
        self.size = k
        self.curSize = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def enQueue(self, value):
        if self.curSize < self.size:
            node = Node(value)
            node.pre = self.tail.pre
            node.next = self.tail
            node.pre.next = node.next.pre = node
            self.curSize += 1
            return True
        return False

    def deQueue(self):
        if self.curSize > 0:
            node = self.head.next
            node.pre.next = node.next
            node.next.pre = node.pre
            self.curSize -= 1
            return True
        return False

    def Front(self):
        return self.head.next.val

    def Rear(self):
        return self.tail.pre.val

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size


class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * 100000
        self.k = k
        self.start = self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.end - self.start == self.k: return False
        self.arr[self.end % self.k] = value
        self.end += 1
        return True

    def deQueue(self) -> bool:
        if self.start == self.end: return False
        val = self.arr[self.start % self.k]
        self.start += 1
        return val

    def Front(self) -> int:
        if self.start == self.end: return -1
        return self.arr[self.start % self.k]

    def Rear(self) -> int:
        if self.start == self.end: return -1
        return self.arr[(self.end - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.start == self.end

    def isFull(self) -> bool:
        return self.end - self.start == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()