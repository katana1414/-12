# tests/test_calculations.py
from models.student import Student
from models.lecturer import Lecturer
from core.calculations import average_homework_by_course, average_lectures_by_course

def test_averages():
    students = [
        Student("A", {"M": [4, 5], "N": [3]}),
        Student("B", {"M": [5, 3], "N": [4]})
    ]
    lecturers = [
        Lecturer("L1", {"M": [5, 4], "N": [4]}),
        Lecturer("L2", {"M": [3, 5], "N": [5]})
    ]
    assert abs(average_homework_by_course(students, "M") - 4.25) < 1e-6
    assert abs(average_lectures_by_course(lecturers, "M") - 4.25) < 1e-6
