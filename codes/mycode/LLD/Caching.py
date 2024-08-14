import abc
from collections import OrderedDict
from enum import Enum


class ICachingManager(abc.ABC):

    @abc.abstractmethod
    def get(self, key: str) -> str:
        pass

    @abc.abstractmethod
    def put(self, key: str, value: str) -> None:
        pass


class IStorageService(abc.ABC):
    @abc.abstractmethod
    def store_data(self, key, val):
        pass

    @abc.abstractmethod
    def retrieve_data(self, key):
        pass

    @abc.abstractmethod
    def remove_data(self, key):
        pass


class IEvictionService(abc.ABC):
    @abc.abstractmethod
    def evict(self) -> str:
        pass

    @abc.abstractmethod
    def set_accessed_key(self, key):
        pass

    @abc.abstractmethod
    def remove(self, key):
        pass


class LRUEvictionService(IEvictionService):
    def __init__(self):
        self.ordered_keys = OrderedDict()

    def evict(self) -> str:
        k, _ = self.ordered_keys.popitem(last=False)
        return k

    def remove(self, key):
        self.ordered_keys.pop(key)

    def set_accessed_key(self, key):
        self.ordered_keys.pop(key, None)
        self.ordered_keys[key] = True


class DefaultStorageService(IStorageService):
    CAPACITY = 2

    def __init__(self, eviction_service: IEvictionService):
        self.eviction_service = eviction_service
        self.map = {}

    def store_data(self, key, val):
        if len(self.map) == DefaultStorageService.CAPACITY:
            k = self.eviction_service.evict()
            self.map.pop(k)
        self.map[key] = val
        self.eviction_service.set_accessed_key(key)

    def retrieve_data(self, key):
        val = self.map.get(key, None)
        self.eviction_service.set_accessed_key(key)
        return val

    def remove_data(self, key):
        self.map.pop(key)
        self.eviction_service.remove(key)


class DefaultCachingManager(ICachingManager):

    def __init__(self):
        self.storage_service = DefaultStorageService(LRUEvictionService())

    def get(self, key: str) -> str:
        return self.storage_service.retrieve_data(key)

    def put(self, key: str, value: str) -> None:
        self.storage_service.store_data(key, value)


class CachingType(Enum):
    LRU = 0
    LFU = 1


class CachingManagerFactory:
    @staticmethod
    def get_caching_manager(type: CachingType) -> ICachingManager:
        if type == CachingType.LRU:
            return DefaultCachingManager()
        


if __name__ == '__main__':
    caching_manager = CachingManagerFactory.get_caching_manager(CachingType.LRU)
    caching_manager.put("s", "sumit")
    caching_manager.put("a", "amit")
    caching_manager.put("l", "lavi")
    caching_manager.put("b", "bro")
    print(caching_manager.get("a"))
    print(caching_manager.get("s"))
    print(caching_manager.get("b"))
    print(caching_manager.get("l"))
