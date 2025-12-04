def test_rate_lecture_and_hw():
    s = Student('Ivan', 'Petrov', 'm')
    l = Lecturer('Anna', 'Sidorova')
    r = Reviewer('Petr', 'Petrov')

    # настройка курсов
    s.courses_in_progress += ['Python']
    l.courses_attached += ['Python']
    r.courses_attached += ['Python']

    # студент ставит оценку лектору
    res1 = s.rate_lecture(l, 'Python', 9)
    assert res1 is None
    assert l.grades['Python'] == [9]

    # проверяем оценку ревьюера
    res2 = r.rate_hw(s, 'Python', 8)
    assert res2 is None
    assert s.grades['Python'] == [8]
