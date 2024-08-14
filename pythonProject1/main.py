# implement LRU cache

# 2 APIs
# get(key)
# put(key,value)

from collections import OrderedDict


class LRU:
    def __init__(self, capacity):
        self.cache = OrderedDict() # DLL remove
        self.n = capacity

    def get(self, key):
        """
        Complexity O(1)
        :param key:
        :return:
        """
        if key in self.cache:
            self.cache.move_to_end(key)  # removing O(1) using DLL in ordered dict
            return self.cache[key]
        return None

    def put(self, key, value):
        """
        O(1)
        :param key:
        :param value:
        :return:
        """
        self.cache[key] = value
        self.cache.move_to_end(key)    # removing O(1) using DLL in ordered Dict
        if len(self.cache) > self.n:
            self.cache.popitem(last=False)

    def print_cache(self):
        """
        O(n)
        :return:
        """
        print(self.cache)


if __name__ == '__main__':
    lru_cache = LRU(capacity=5)
    lru_cache.put('a', 1)  # a:1
    lru_cache.put('b', 2)  # a:1,b:2
    lru_cache.put('c', 3)  # a:1,b:2,c:3
    assert lru_cache.get('b') == 2  # a:1,c:3,b:2
    lru_cache.put('d', 4)  # a:1,c:3,b:2,d:4
    lru_cache.put('e', 5)  # a:1,c:3,b:2,d:4,e:5
    assert lru_cache.get('d') == 4  # a:1,c:3,b:2,e:5,d:4
    assert lru_cache.get('a') == 1  # c:3,b:2,e:5,d:4,a:1
    lru_cache.put('f', 6)  # b:2,e:5,d:4,a:1,f:6
    assert lru_cache.get('c') == None

    lru_cache.print_cache()
