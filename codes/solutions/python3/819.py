import re
from collections import Counter

from mycode.tree import Solution


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.findall(r"\u005Cw+", paragraph)
        dic = {}
        mx = [0, 0]
        for char in paragraph:
            char = char.lower()
            if char not in banned:
                if char not in dic:
                    dic[char] = 1
                else:
                    dic[char] += 1
                mx[0] = max(mx[0], dic[char])
                if mx[0] == dic[char]: mx[1] = char
        return mx[1]

    def mostCommon(self, para, banned):
        para_words = re.split(', |\. | ',para.lower().rstrip('.'))
        return Counter(filter(lambda x: x not in banned, para_words)).most_common(n=1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommon(paragraph, banned))
