from collections import deque, Counter
from typing import List


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    students_q = deque(students)
    student_likes = Counter(students)
    while sandwiches and sandwiches[0] in student_likes:
        while sandwiches[0] != students_q[0]:
            students_q.append(students_q.popleft())

        students_q.popleft()
        x = sandwiches.pop(0)
        student_likes[x] -= 1
        if student_likes[x] == 0:
            student_likes.pop(x)

    return len(students_q)


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
countStudents(students, sandwiches)
