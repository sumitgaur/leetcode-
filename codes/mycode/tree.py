import unittest
from collections import defaultdict, deque
from typing import Optional


# O(N * logN) + O(2 * N) time
# O(3 * N) space
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        def leaf_order(root):
            if root:
                if root.left is None and root.right is None:
                    yield root.val
                yield from leaf_order(root.left)
                yield from leaf_order(root.right)

        itr1 = leaf_order(root1)
        itr2 = leaf_order(root2)
        for i, j in zip(itr1, itr2):
            print(i, j)
            if i != j:
                return False
        return zip(itr1, itr2)


def deepestLeavesSum(root: Optional[TreeNode]) -> int:
    def populate_level_map(root, l_map, l=0):
        if root:
            l_map[l].append(root.val)
            populate_level_map(root.left, l_map, l + 1)
            populate_level_map(root.right, l_map, l + 1)

    l_map = defaultdict(list)
    populate_level_map(root, l_map)
    return sum(l_map[max(l_map)])


def deepestLeavesSum2(root: Optional[TreeNode]) -> int:
    queue = deque()
    queue.append(root)
    while queue:
        level_sum = 0
        s = len(queue)
        while s:
            x = queue.popleft()
            level_sum += x.val
            queue.append(x.left) if x.left else None
            queue.append(x.right) if x.right else None
            s -= 1
    return level_sum


# root=TreeNode(1)
# root.left=TreeNode(2)
# root.right=TreeNode(3)
# root1=TreeNode(1)
# root1.left=TreeNode(3)
# root1.right=TreeNode(2)
# Solution().leafSimilar(root,root1)
def find_available_times(schedules):
    ret = []

    intervals = [list(x) for personal in schedules for x in personal]

    intervals.sort(key=lambda x: x[0], reverse=True)  # O(N * logN)

    tmp = []

    while intervals:
        pair = intervals.pop()

        if tmp and tmp[-1][1] >= pair[0]:
            tmp[-1][1] = max(pair[1], tmp[-1][1])

        else:
            tmp.append(pair)

    for i in range(len(tmp) - 1):  # find gaps
        ret.append([tmp[i][1], tmp[i + 1][0]])

    return ret


class CalendarTests(unittest.TestCase):

    def test_find_available_times(self):
        p1_meetings = [
            (845, 900),
            (1230, 1300),
            (1300, 1500),
        ]

        p2_meetings = [
            (0, 844),
            (845, 1200),
            (1515, 1546),
            (1600, 2400),
        ]

        p3_meetings = [
            (845, 915),
            (1235, 1245),
            (1515, 1545),
        ]

        schedules = [p1_meetings, p2_meetings, p3_meetings]

        availability = [[844, 845], [1200, 1230], [1500, 1515], [1546, 1600]]

        self.assertEqual(
            find_available_times(schedules),
            availability
        )


def find_depth(s): # from preorder
    def do(s):
        if s[0] == 'l': return 0
        s.pop(0);ld = do(s)
        s.pop(0);rd = do(s)
        return max(ld, rd) + 1
    return do(list(s))


# find_depth("nlnnlll")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
