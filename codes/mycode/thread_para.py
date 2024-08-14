import threading
import time


class PrintPara:

    def __init__(self, paragraph, m):
        self.paragraph_words = paragraph.split(' ')
        self.n = len(self.paragraph_words)
        self.idx = 0
        self.m = m
        self.semaphores = [threading.Semaphore(0) for _ in range(m)]
        self.semaphores[0].release()

    def print_word(self):
        while self.idx < self.n:
            TID = int(threading.currentThread().getName())
            self.semaphores[TID].acquire()
            if self.idx < self.n:
                print(self.paragraph_words[self.idx] + " printed by " + threading.currentThread().getName())
                self.idx += 1
                self.semaphores[(TID + 1) % self.m].release()
            else:
                self.semaphores[(TID - 1) % self.m].release()
                break


if __name__ == '__main__':
    m = 3
    para_obj = PrintPara("I am helping myself to get rid off these imaginary world", m)
    for i in range(m):
        t = threading.Thread(target=para_obj.print_word, name=str(i))
        t.start()
