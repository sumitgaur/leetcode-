import hashlib
import bisect
from typing import List, Optional


class Node:
    def __init__(self, hash_value: int, node_id: str):
        self.hash = hash_value
        self.node_id = node_id

    def __lt__(self, other):
        return self.hash < other.hash


class ConsistentHashRing:
    def __init__(self, virtual_nodes: int = 100):
        self.virtual_nodes = virtual_nodes
        self.ring: List[Node] = []

    def _hash(self, key: str) -> int:
        digest = hashlib.md5(key.encode("utf-8")).hexdigest()
        return int(digest[:16], 16)

    def add_node(self, node_id: str) -> None:
        for i in range(self.virtual_nodes):
            vnode_key = f"{node_id}#VN{i}"
            h = self._hash(vnode_key)

            node = Node(h, node_id)
            bisect.insort(self.ring, node)

    def remove_node(self, node_id: str) -> None:
        self.ring = [node for node in self.ring if node.node_id != node_id]

    def get_node(self, key: str) -> Optional[str]:
        if not self.ring:
            return None

        h = self._hash(key)
        dummy = Node(h, "")  # only hash matters for comparison

        idx = bisect.bisect_left(self.ring, dummy)
        if idx == len(self.ring):
            idx = 0

        return self.ring[idx].node_id
ring = ConsistentHashRing(virtual_nodes=50)

ring.add_node("node-A")
ring.add_node("node-B")
ring.add_node("node-C")

print(ring.get_node("user:123"))
print(ring.get_node("order:999"))

ring.remove_node("node-B")
