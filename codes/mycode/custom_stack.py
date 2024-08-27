class stack:
    def __init__(self):
        self.arr = []
        self.increase_arr = []

    def push(self, x):
        self.arr.append(x)
        self.increase_arr.append(0)

    def pop(self):
        if self.arr:
            self.arr.pop()
            x = self.increase_arr.pop()
            if self.increase_arr:
                self.increase_arr[-1] += x

    def peek(self):  # get the topmost element of the stack
        if self.arr:
            return self.arr.pop() + self.increase_arr.pop()

    def increase(self, i, v):  # increase bottom i element of the stack by v
        self.increase_arr[i] += v
