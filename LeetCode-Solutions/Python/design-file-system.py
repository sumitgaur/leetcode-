# Time:  create: O(n)
#        get:    O(n)
# Space: O(n)
from collections import defaultdict


class FileSystem(object):

    def __init__(self):
        self.__lookup = {"": -1}

    def create(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        if path[:path.rfind('/')] not in self.__lookup:
            return False
        self.__lookup[path] = value
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path not in self.__lookup:
            return -1
        return self.__lookup[path]


class FileSystemInMemory:
    
    def __init__(self):
        self.root = {}

    def ls(self, path):
        cur = self.root
        for dir in path.split('/')[1:]:
            cur = cur[dir]
        return list(cur.keys())

    def mkdir(self, path):
        cur = self.root
        for dir in path.split('/')[1:]:
            cur = cur.setdefault(dir, {})

    def addContentToFile(self, filepath, content):
        cur = self.root
        for dir in filepath.split('/')[1:]:
            cur = cur.setdefault(dir, {})
        cur['content'] = content

    def readContentFromFile(self, filepath):
        cur = self.root
        for dir in filepath.split('/')[1:]:
            cur = cur.setdefault(dir, {})
        return cur['content']


fs = FileSystemInMemory()
fs.mkdir("/a/b/c")
fs.addContentToFile("/a/b/c/d", "hello")
print(fs.readContentFromFile("/a/b/c/d"))  # hello
# print(fs.ls("/a/b"))  # ['c']
print(fs.ls("/a/b/c/d"))  # ['d']
