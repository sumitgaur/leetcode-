class PhoneDirectory:

    def __init__(self, maxNumbers):
        self.nums = set(range(maxNumbers))

    def get(self):
        return self.nums.pop() if self.nums else -1

    def check(self, number):
        return number in self.nums

    def release(self, number):
        self.nums.add(number)


class PhDir:
    def __init__(self, n):
        self.bits = [False] * n

    def get(self):
        for i in range(len(self.bits)):
            if not self.bits[i]:
                return i

    def

