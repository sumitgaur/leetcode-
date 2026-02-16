from collections import defaultdict

from sortedcontainers import SortedDict
from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = defaultdict(int)
        for msg, sender in zip(messages, senders):
            d[sender] += len(msg.split())

        max_words = max(d.values())
        return max(sender for sender, cnt in d.items() if cnt == max_words)


messages = ["How is leetcode for everyone", "Leetcode is useful for practice"]
senders = ["Bob", "Charlie"]
print(Solution().largestWordCount(messages, senders))
