class Mentor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}  # {'Python': [7, 9], ...}

    def average_grade(self) -> float:
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        avg = self.average_grade()
        return f"Lecturer: {self.name} {self.surname}\n" \
               f"Average grade: {avg:.2f}"


class Reviewer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course: str, grade: int):
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in self.courses_attached or course not in student.courses_in_progress:
            return 'Ошибка'
        student.grades.setdefault(course, []).append(grade)


class Student:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}  # {'Python': [9, 8], ...}

    def rate_lecture(self, lecturer: Lecturer, course: str, grade: int):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return 'Ошибка'
        lecturer.grades.setdefault(course, []).append(grade)

    def average_grade(self) -> float:
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        avg = self.average_grade()
        return (f"Student: {self.name} {self.surname}\n"
                f"Gender: {self.gender}\n"
                f"Average grade: {avg:.2f}\n"
                f"Courses in progress: {', '.join(self.courses_in_progress)}\n"
                f"Finished courses: {', '.join(self.finished_courses)}")
