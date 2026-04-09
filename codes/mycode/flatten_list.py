class NestedList:
    def __init__(self, l):
        self.list_generator = self.flatten(l)

    def __iter__(self):
        return self.list_generator

    def next(self):
        return next(self.list_generator)

    def flatten(self, l):
        for item in l:
            if isinstance(item, int):
                yield item
            else:
                yield from self.flatten(item)


l = [1, [2, [3]], 4]
nested_list = NestedList(l)

while True:
    try:
        print(nested_list.next())
    except StopIteration as e:
        print("stop")
        break
