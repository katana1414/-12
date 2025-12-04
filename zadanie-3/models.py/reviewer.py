class Reviewer:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached: list[str] = []

    def rate_hw(self, student, course: str, grade: float):
        if course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"
