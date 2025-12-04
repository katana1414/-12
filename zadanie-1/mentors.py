class Mentor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}  # по желанию можно использовать позже

class Reviewer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
