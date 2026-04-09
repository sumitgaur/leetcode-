import heapq
from collections import defaultdict, Counter, OrderedDict, deque


def longest_subarraywithksum(arr, k):
    cur_sum = 0
    max_len = 0
    prefix_sum_mp = {0: -1}
    for r in range(len(arr)):
        cur_sum += arr[r]
        if cur_sum - k in prefix_sum_mp:
            max_len = max(r - prefix_sum_mp[cur_sum - k], max_len)
        prefix_sum_mp.setdefault(cur_sum - k, r)

    return max_len


# nums = [1, -1, 5, -2, 3]
# k = 5
#
# print(longest_subarraywithksum(nums, k))


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    max_len, cur_cons = 0, 0
    for x in nums:
        while x in num_set:
            cur_cons += 1
            max_len = max(max_len, cur_cons)
            x = x + 1

    return max_len


# nums = [100, 4, 200, 1, 3, 2]
# print(longest_consecutive_sequence(nums))


def topkfrequentelement(nums, k):
    '''
    complexity O(nlgk)
    :param nums:
    :param k:
    :return:
    '''
    freq_mp = Counter(nums)
    heap = []
    for num, freq in freq_mp.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]


def topkfrequentelement_bucket(nums, k):
    '''
    complexity O(n)
    maximum frequency - m
    O(mk)
    :param nums:
    :param k:
    :return:
    '''
    freq_to_nums_mp = defaultdict(list)
    freq_mp = Counter(nums)
    top_k = []
    for num, freq in freq_mp.items():
        freq_to_nums_mp[freq].append(num)
    max_freq = max(freq_to_nums_mp.keys())
    for freq in range(max_freq, -1, -1):
        for x in freq_to_nums_mp.get(freq):
            top_k.append(x)
            k -= 1
            if k == 0: return top_k


# print(topkfrequentelement_bucket([1, 1, 1, 2, 2, 3], 2))


class LRUCache:
    def __init__(self, k):
        self.capacity = k
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            print(-1)
            return
        self.cache.move_to_end(key)
        print(self.cache[key])

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# lru_cache = LRUCache(2)
# lru_cache.put(1, 1)
# lru_cache.put(2, 2)
# lru_cache.get(1)
# lru_cache.put(3, 3)
# lru_cache.get(2)
# lru_cache.put(4, 4)
# lru_cache.get(1)
# lru_cache.get(3)
# lru_cache.get(4)


def longest_substring_without_repeat(s):
    l = 0
    chars_seen = set()
    max_len = 0
    for r, ch in enumerate(s):
        while ch in chars_seen:
            chars_seen.remove(s[l])
            l += 1
        chars_seen.add(ch)
        max_len = max(max_len, r - l + 1)
    return max_len


#
# s = "abcabcbb"
# print(longest_substring_without_repeat(s))


class StreamMedian:
    left = []
    right = []

    def addNum(self, num):
        popped = heapq.heappushpop(self.left, -num)
        heapq.heappush(self.right, -popped)
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


# stream_median = StreamMedian()
# stream_median.addNum(1)
# stream_median.addNum(2)
# print(stream_median.findMedian())
#
# stream_median.addNum(3)
# print(stream_median.findMedian())

def sliding_window_max_k(nums, k):
    dq = deque()
    res = []
    for i in range(len(nums)):
        if dq and i - k > dq[0]: dq.popleft()
        while dq and nums[dq[0]] < nums[i]: dq.popleft()
        dq.append(i)
        if i >= k - 1: res.append(nums[dq[0]])
    return res


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
# k = 3
# print(sliding_window_max_k(nums, k))

def merge_k_lists(lists):
    min_heap = []
    res = []
    for i, list_ in enumerate(lists):
        if list_:
            heapq.heappush(min_heap, (list_[0], i, 0))
    while min_heap:
        min_elt, array_index, elt_index = heapq.heappop(min_heap)
        res.append(min_elt)
        if elt_index + 1 < len(lists[array_index]):
            heapq.heappush(min_heap, (lists[array_index][elt_index + 1], array_index, elt_index + 1))
    return res


# lists = [
#     [1, 4, 5],
#     [1, 3, 4],
#     [2, 6]
# ]
# print(merge_k_lists(lists))
from collections import deque


def word_ladder(begin_word, end_word, wordlist):
    word_set = set(wordlist)
    queue = deque([begin_word])
    level = 1

    while queue:
        for _ in range(len(queue)):
            word = queue.popleft()

            if word == end_word:
                return level

            for w in list(word_set):
                diff = sum(c1 != c2 for c1, c2 in zip(word, w))
                if diff == 1:
                    queue.append(w)
                    word_set.remove(w)

        level += 1

    return 0


# beginWord = "hit"
# endWord = "cog"
#
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(word_ladder(beginWord, endWord, wordList))


def alien_lang_dict(word_list):
    in_degree = defaultdict(int)
    graph = defaultdict(set)
    for w1, w2 in zip(word_list, word_list[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    in_degree[c2] += 1
                break
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    res = []
    while queue:
        c = queue.popleft()
        res.append(c)
        for nei in graph[c]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    return res


# word_list = ["wrt", "wrf", "er", "ett", "rftt"]
# print(alien_lang_dict(word_list))


def rollTheString(s, roll):
    n = len(s)
    count = [0] * n
    for r in roll:
        count[r - 1] += 1

    for i in range(n - 2, -1, -1):
        count[i] += count[i + 1]

    res = []
    for i, c in enumerate(s):
        new_chr = chr((ord(c) - 97 + count[i]) % 26 + 97)
        res.append(new_chr)
    return ''.join(res)


# s = "abz"
# roll = [3, 2, 1]

# print(rollTheString(s, roll))


from multiprocessing import Process, Event, Value
import multiprocessing

def search_chunk(arr, target, start, end, found_event, result):
    for i in range(start, end):

        # Stop if another process already found it
        if found_event.is_set():
            return

        if arr[i] == target:
            result.value = i
            found_event.set()
            return


def parallel_search(arr, target, num_processes=4):
    n = len(arr)
    chunk = n // num_processes

    found_event = Event()
    result = Value('i', -1)

    processes = []

    for i in range(num_processes):
        start = i * chunk
        end = n if i == num_processes - 1 else (i + 1) * chunk

        p = Process(
            target=search_chunk,
            args=(arr, target, start, end, found_event, result)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return result.value


# if __name__ == "__main__":
#     arr = [5, 8, 2, 9, 3, 7, 10, 1, 6]
#     target = 7
#
#     print(parallel_search(arr, target))
