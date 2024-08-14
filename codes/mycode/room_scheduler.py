"""
Design a Room Book Scheduler for an Office Building with 50 Rooms. Every room would be associated with a Calendar. We can add a new event if adding the event will not cause a double booking. A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.). The event can be represented as start and end time that represents a booking on the interval [start, end], the range of real numbers x such that start <= x < end. * Must Haves * -
User should be able to request to book a room based on User's input start and End time. If the Room booking is possible, the User would get the Room allocated, if it is not possible to get any rooms for that time interval, return false. - Ensure No Double booking happens for a Room. - More than One User can request for booking for Meeting rooms at a time. System should ensure not double booking can occur. * Good to haves * - User should be able to able to get all available rooms for the User's input start and End Time. - User should be able to un-book an already booked room. - User need to check-in the room before the grace period : (startTime + 5min). If the User doesn't checks in before the grace period, the room would be auto unbooked.



Assumption
- all the room are same type
- No capacity
- start and end are within Same day
MosCow
Must have
- user should be able to book a room if available based on input start and end
- No double booking

API
book_room(start_time,end_time)


"""
import threading
import time
import uuid
from sortedcontainers import SortedList


class MeetingRoom:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.meetings = SortedList()
        self.lock = threading.Semaphore(1)

    def book(self, start, end) -> bool:
        """
        write and update requires lock
        :param start:
        :param end:
        :return:
        """
        self.lock.acquire()
        idx = self.meetings.bisect((start, end))  # b search
        if (idx > 0 and self.meetings[idx - 1][1] > start) or (
                idx < len(self.meetings) and self.meetings[idx][0] < end):  # overlap for that particular room
            self.lock.release()
            return False
        else:
            self.meetings.add((start, end))
            self.lock.release()
            return True

    def is_available(self, start, end) -> bool:
        idx = self.meetings.bisect((start, end))  # b search
        if (idx > 0 and self.meetings[idx - 1][1] > start) or (
                idx < len(self.meetings) and self.meetings[idx][0] < end):  # overlap for that particular room
            return False
        else:
            return True

    def get_id(self):
        return self.id

    def un_book(self, start, end):
        self.meetings.remove((start, end))

    def start_clean_up(self):
        """
        Daemon thread has to be thread safe
        1. old meetings
        2. Grace period meeting whicha re not checked in on time.
        :return:
        """


class Meeting:
    def __init__(self, start, end):
        self.id = str(uuid.uuid4())
        self.start_time = start
        self.end_time = end
        # attendees notifications to the attendees


class Scheduler:
    ROOM_COUNT = 2
    GRACE_PERIOD = 5 * 60

    def __init__(self):
        self.meeting_rooms = [MeetingRoom() for _ in range(Scheduler.ROOM_COUNT)]
        map(lambda room: room.start_clean_up, self.meeting_rooms) # start the cleanup per room
        # self.sempahores = [threading.Semaphore(1) for _ in range(Scheduler.ROOM_COUNT)]

    def book(self, start, end) -> int:
        """
        nlg(m)  - m - avarage booked meeting
        :param start:  epoch time
        :param end:  epoch time
        :return:  room id which is booked, -1 if nothing is available
        """
        for meet_room in self.meeting_rooms:
            # if not self.sempahores[i].acquire(blocking=False):
            #     continue
            if meet_room.book(start, end) != -1:
                print(f'Allotted room {meet_room.get_id()} for {start} to {end}')

        print(f'No room available')
        return -1

    def un_book(self, room_id, start, end):
        """

        :param start:
        :param end:
        :return:
        """
        room = [x for x in self.meeting_rooms if x.get_id() == room_id]
        room.un_book(start, end)

    def get_available_rooms(self, start, end):
        return list(map(lambda x: x.get_id, [x for x in self.meeting_rooms if x.is_available(start, end)]))

    def check_in(self, room_id, start, end):
        if time.time() > start + Scheduler.GRACE_PERIOD:
            self.un_book(room_id, start, end)


if __name__ == '__main__':
    scheduler = Scheduler()

    threading.Thread(target=scheduler.book, args=(1030, 1100)).start()
    threading.Thread(target=scheduler.book, args=(1030, 1100)).start()
    threading.Thread(target=scheduler.book, args=(1130, 1200)).start()
    threading.Thread(target=scheduler.book, args=(1130, 1200)).start()
    threading.Thread(target=scheduler.book, args=(1030, 1100)).start()
