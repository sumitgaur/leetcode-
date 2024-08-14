# we have 1 producer and 1 consumer
import random
import threading
from threading import Thread
from time import sleep
from queue import Queue
import hashlib

buffer = [Queue(), Queue()]  # partitions
K = 2
num_of_events = 0


# [
# []  consumer 1  kafka key
# []  consumer 2
# ]

def kafka_key(s):
    global num_of_events
    # return (int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10 ** 8)) % K
    # round robin
    num_of_events = num_of_events + 1
    return num_of_events % 2 == 0


def producer(i):
    """
    producing the data and putting in the buffer
    :return:
    """
    print("producing data ")
    buffer[0].put(i) if kafka_key(i) == 0 else buffer[1].put(i)


def consumer():
    """
    continuosly consuming the data from the buffer
    :return:
    """
    while True:
        partition = int(threading.currentThread().getName()) - 1
        print(buffer[partition].get(), "consumed data by thread ", threading.currentThread().getName())
        sleep(1)


producer("a")
producer("b")
producer("c")
producer("d")
producer("e")
producer("f")
producer("g")
t1 = Thread(target=consumer, name='1')
t2 = Thread(target=consumer, name='2')
t1.start()
t2.start()
