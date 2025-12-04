class Student:
    def __init__(self, name: str, surname: str, gender: str):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress: List[str] = []
        self.finished_courses: List[str] = []
        self.grades: Dict[str, List[float]] = {}

    def rate_lecturer(self, lecturer: 'Lecturer', course: str, grade: float):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, []).append(grade)

    def average_grade(self) -> float:
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        avg = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg:.1f}"

    def __lt__(self, other: 'Student') -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
