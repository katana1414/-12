# Пример использования
# Создаем студентов
student_1 = Student("Ruoy", "Eman", "m")
student_2 = Student("Test", "User", "f")

student_1.courses_in_progress += ["Python", "Git"]
student_2.courses_in_progress += ["Python"]

# Создаем лекторов
lecturer_1 = Lecturer("Some", "Lecturer")
lecturer_2 = Lecturer("Another", "Lecturer")

lecturer_1.courses_attached += ["Python"]
lecturer_2.courses_attached += ["Git"]

# Создаем проверяющего
reviewer_1 = Reviewer("Best", "Reviewer")
reviewer_1.courses_attached += ["Python", "Git"]

# Пример оценивания
reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_2, "Python", 8)

student_1.rate_lecturer(lecturer_1, "Python", 10)
student_2.rate_lecturer(lecturer_1, "Python", 9)

print(student_1)
print()
print(student_2)
print()
print(lecturer_1)
print()
print(reviewer_1)

# Сравнение
print("\nСравнение по средним оценкам:")
print(student_1 < student_2)
print(lecturer_1 < lecturer_2)
