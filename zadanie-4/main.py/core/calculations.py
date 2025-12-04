from typing import List
from models.student import Student
from models.lecturer import Lecturer

def average_homework_by_course(students: List[Student], course: str) -> float:
    total = 0.0
    count = 0
    for s in students:
        grades = s.homeworks.get(course, [])
        total += sum(grades)
        count += len(grades)
    return total / count if count else 0.0

def average_lectures_by_course(lecturers: List[Lecturer], course: str) -> float:
    total = 0.0
    count = 0
    for l in lecturers:
        grades = l.lectures.get(course, [])
        total += sum(grades)
        count += len(grades)
    return total / count if count else 0.0
