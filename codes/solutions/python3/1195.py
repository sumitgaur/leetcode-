from threading import Semaphore, Thread


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.f_sem = Semaphore(0)
        self.b_sem = Semaphore(0)
        self.fb_sem = Semaphore(0)
        self.n_sem = Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: "Callable[[], None]") -> None:
        for i in range(3, self.n + 1, 3):
            self.f_sem.acquire()
            printFizz()
            self.n_sem.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        for i in range(5, self.n + 1, 5):
            self.b_sem.acquire()
            printBuzz()
            self.n_sem.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        for i in range(15, self.n + 1, 15):
            self.fb_sem.acquire()
            printFizzBuzz()
            self.n_sem.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            self.n_sem.acquire()
            if i % 15 == 0:
                self.fb_sem.release()
            elif i % 3 == 0:
                self.f_sem.release()
            elif i % 5 == 0:
                self.b_sem.release()
            else:
                printNumber(i)
                self.n_sem.release()


if __name__ == '__main__':
    fizz_buzz = FizzBuzz(15)
    Thread(target=fizz_buzz.fizz, args=(lambda: print("Fizz"),)).start()
    Thread(target=fizz_buzz.buzz, args=(lambda: print("Buzz"),)).start()
    Thread(target=fizz_buzz.fizzbuzz, args=(lambda: print("FizzBuzz"),)).start()
    Thread(target=fizz_buzz.number, args=(lambda i: print(i),)).start()
