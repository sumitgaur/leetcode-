# import threading
#
#
# class ZeroEvenOdd:
#     def __init__(self, n):
#         self.n = n
#         self.z = threading.Semaphore()
#         self.e = threading.Semaphore()
#         self.o = threading.Semaphore()
#         self.e.acquire()
#         self.o.acquire()
#         self.cur = 1
#
# 	# printNumber(x) outputs "x", where x is an integer.
#     def zero(self, ) -> None:
#         for _ in range(self.n):
#             self.z.acquire()
#             printNumber(0)
#             if self.cur % 2:
#                 self.o.release()
#             else:
#                 self.e.release()
#
#
#     def even(self, ) -> None:
#         for _ in range(self.n // 2):
#             self.e.acquire()
#             printNumber(self.cur)
#             self.cur += 1
#             self.z.release()
#
#     def odd(self, ) -> None:
#         for _ in range(self.n // 2 + self.n % 2):
#             self.o.acquire()
#             printNumber(self.cur)
#             self.cur += 1
#             self.z.release()

import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, ) -> None:
        pass

    def even(self, ) -> None:n
        for i in range(2, 2 * self.n + 1, 2):
            self.even_sem.acquire()
            print("0" + str(i), end='')
            self.odd_sem.release()

    def odd(self, ) -> None:
        for i in range(1, 2 * self.n, 2):
            self.odd_sem.acquire()
            print("0" + str(i), end='')
            self.even_sem.release()


#
# from threading import Semaphore
# class ZeroEvenOdd:
#     def __init__(self, n):
#         self.n = n
#         self.semOdd  = Semaphore(0) # Permission to write an Odd  Number
#         self.semEven = Semaphore(0) # Permission to write an Even Number
#         self.semZero = Semaphore(1) # Permission to write a  Zero
# 	# printNumber(x) outputs "x", where x is an integer.
#     def zero(self, printNumber):
#         for i in range(1,self.n+1):
#             # A) Request Permission to Write a Zero
#             self.semZero.acquire()
#             printNumber(0)
#             # B) Check if "i" if Odd or Even, and give permission to write the number
#             if i&1:
#                 self.semOdd.release()
#             else:
#                 self.semEven.release()
#             # C) Permission to write a zero is returned by another Thread ( release triggers a change)
#     def even(self, printNumber):
#         # A) Iterate only through Even numbers
#         for i in range(2,self.n+1,2):
#             # B) Request Permission to Write Current Number
#             self.semEven.acquire()
#             printNumber(i)
#             # C) Return Permission to Write a Zero (if applicable)
#             self.semZero.release()
#     def odd(self, printNumber):
#         # A) Iterate only through Odd numbers
#         for i in range(1,self.n+1,2):
#             # B) Request Permission to Write Current Number
#             self.semOdd.acquire()
#             printNumber(i)
#             # C) Return Permission to Write a Zero (if applicable)
#             self.semZero.release()
# @lc code=end

z = ZeroEvenOdd(10)
threading.Thread(target=z.zero, args=[]).start()
threading.Thread(target=z.even, args=[]).start()
threading.Thread(target=z.odd, args=[]).start()
