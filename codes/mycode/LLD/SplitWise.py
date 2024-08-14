import heapq
import uuid
from collections import defaultdict

from typing import Dict


class User:
    def __init__(self, name, details):
        self.id = str(uuid.uuid4())
        self.name = name
        self.details = details


class Group:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.users = []
        self.title = None

    def give_title(self, t):
        self.title = t

    def add_user(self, user: User):
        self.users.append(user)

    def remove_user(self, user: User):
        self.users.remove(user)


class Expense:
    def __init__(self, amount, user1, user2, details):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.from_ = user1
        self.to_ = user2
        self.details = details


class PaymentGraph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_node(self, u, v, w):
        self.adj_list[u].append((v, w))

    def net_weight(self) -> Dict[User]:
        nodes_net_weight = defaultdict(int)
        for u, vs in self.adj_list:
            for v in vs:
                nodes_net_weight[u] -= v[1]
                nodes_net_weight[v] += v[1]
        return nodes_net_weight


class HeapNode:
    def __init__(self, user, c):
        self.user = user
        self.change = c


class MinHeapNode(HeapNode):
    def __init__(self, user, c):
        super().__init__(user, c)

    def __lt__(self, other):
        return self.change < other.change


class MaxHeapNode(HeapNode):
    def __init__(self, user, c):
        super().__init__(user, c)

    def __lt__(self, other):
        return self.change > other.change


class PaymentService:
    def __init__(self):
        self.payment_graph = PaymentGraph()

    def add_expense(self, expense: Expense):
        self.payment_graph.add_node(expense.from_, expense.to_, expense.amount)

    def make_settlement(self):
        user_net_change = self.payment_graph.net_weight()
        giver_heap = []
        receiver_heap = []
        for user, change in user_net_change:
            if change > 0:
                heapq.heappush(receiver_heap, MaxHeapNode(user, change))
            elif change < 0:
                heapq.heappush(giver_heap, MinHeapNode(user, change))

        while receiver_heap and giver_heap:
            receiver = receiver_heap.pop()
            sender = giver_heap.pop()
            at_transferred = min(sender.change, receiver.change)
            print("User {} paid User {} amount {}", sender.user, receiver.user, at_transferred)
            sender.change += at_transferred
            receiver.change -= at_transferred
            if sender.change != 0:
                heapq.heappush(giver_heap, sender)
            if receiver.change != 0:
                heapq.heappush(receiver_heap, receiver)
