

def sum(a, b):
    return a + b


class curry:
    def __init__(self, fn):
        self.fn = fn

    def csum(self, *args):
        if len(args) >= self.fn.__code__.co_argcount:
            return self.fn(*args)

        def collect_args(*next_args):
            return self.csum(*args, *next_args)

        return collect_args


c = curry(sum)
c.csum(1, 2, )
print(c.csum(1)(2))
