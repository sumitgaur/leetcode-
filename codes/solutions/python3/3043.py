class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_map = set()

        def build_prefixes():
            for each in map(str, arr1):
                for i in range(len(each)):
                    prefix_map.add(each[: i + 1])

        build_prefixes()
        mx = 0
        for each in map(str, arr2):
            for i in range(len(each)):
                if each[: i + 1] in prefix_map:
                    mx = max(mx, len(each[: i + 1]))

        return mx
