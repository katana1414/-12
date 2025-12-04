class Lecturer:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached: List[str] = []
        self.grades: Dict[str, List[float]] = {}

    def average_grade(self) -> float:
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        avg = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg:.1f}"

    def __lt__(self, other: 'Lecturer') -> bool:
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()
