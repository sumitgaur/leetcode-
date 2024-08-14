from collections import defaultdict, Counter


class Solution:
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        for s in strs:
            dic["".join(sorted(s))].append(s)
        return list(dic.values())

    def groupAnagrams2(self, strs):
        anagrams = defaultdict(list)
        for word in strs:
            hash_ = tuple(sorted(Counter(word).items()))
            anagrams[hash_].append(word)
        return list(anagrams.values())


Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
