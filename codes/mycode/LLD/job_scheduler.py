import datetime
import heapq
import time
from threading import Thread
import queue


class TaskInterface:

    def run(self):
        raise NotImplementedError


class ProcessPdf(TaskInterface):
    def __init__(self, pdf_name):
        super().__init__()

        self.name = pdf_name

    def run(self):
        print("Processing pdf parsing {}".format(self.name))


class ProcessEmailMessage(TaskInterface):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("Processing email parsing {}".format(self.name))


class TaskSchedulerInterface:
    def __init__(self):
        pass

    def scheduleTask(self, task, time):
        raise NotImplementedError

    def scheduleAtFixedInterval(self, task, interval):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError


class TaskSchedulerImpl(TaskSchedulerInterface):
    def __init__(self):
        super().__init__()
        self.tasks_pq = queue.PriorityQueue()

    def scheduleTask(self, task, time_):
        self.tasks_pq.put((time_, task), block=True)

    def produceIntervalTask(self, task, interval):
        i = 0
        while True:
            self.tasks_pq.put((time.time() + i * interval, task), block=True)
            i += 1

    def scheduleAtFixedInterval(self, task, interval):
        thread = Thread(target=self.produceIntervalTask, args=(task, interval,))
        thread.start()
        thread.join()

    def start(self):
        while True:
            if self.tasks_pq and self.tasks_pq.queue[0][0] <= time.time():
                time_, task = self.tasks_pq.get(block=True)
                print("Running the task at approx scheduled time {}. Current time {}".format(
                    datetime.datetime.fromtimestamp(time_), datetime.datetime.fromtimestamp(time.time())))
                task.run()


if __name__ == '__main__':
    task_scheduler = TaskSchedulerImpl()
    task_scheduler.scheduleTask(ProcessPdf("PDF-1"), time.time() + 5)
    task_scheduler.scheduleAtFixedInterval(ProcessEmailMessage("EMAIL-1"), 2)
    thread = Thread(target=task_scheduler.start)
    thread.start()
    task_scheduler.scheduleAtFixedInterval(ProcessEmailMessage("EMAIL-2"), 10)
    thread.join()
