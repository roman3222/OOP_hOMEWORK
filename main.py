class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __counting_grades(self):
        mid_grades_py = sum(self.grades['Python']) / len(self.grades['Python'])
        mid_grades_git = sum(self.grades['Git']) / len(self.grades['Git'])
        grades_py_git = (mid_grades_py + mid_grades_git) / len(self.grades)
        return round(grades_py_git, 1)






    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return student_best.__counting_grades() > student_2.__counting_grades()


    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: ' \
                       f'{self.__counting_grades()}\n' \
                       f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: ' \
                       f'{" ".join(self.finished_courses)}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}

    def __calculation_grades(self):
        midle_grades_py = sum(self.course_grades['Python']) / len(self.course_grades['Python'])
        midle_grades_git = sum(self.course_grades['Git']) / len(self.course_grades['Git'])
        midle_grades_py_git = (midle_grades_py + midle_grades_git) / len(self.course_grades)
        return round(midle_grades_py_git, 1)


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return cool_lecturer.__calculation_grades() < lecturer_2.__calculation_grades()

    def __str__(self):
        self.some_lecturer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: ' \
                             f'{self.__calculation_grades()}'
        return self.some_lecturer


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.some_reviever = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return self.some_reviever



student_best = Student('John', 'Salivan')
student_best.courses_in_progress += ['Python', 'Git']
student_best.finished_courses += ['Files']

student_2 = Student('Linda', 'Mazovski')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Files']

cool_lecturer = Lecturer('Mike', 'Vazovski')
cool_lecturer.courses_attached += ['Python', 'Git']

lecturer_2 = Lecturer('Denzel', 'Washington')
lecturer_2.courses_attached += ['Python', 'Git']

student_best.rate(cool_lecturer, 'Python', 10)
student_best.rate(cool_lecturer, 'Python', 8)
student_best.rate(cool_lecturer, 'Python', 9)
student_best.rate(cool_lecturer, 'Git', 8)
student_best.rate(cool_lecturer, 'Git', 7)
student_best.rate(cool_lecturer, 'Git', 9)

student_2.rate(lecturer_2, 'Python', 8)
student_2.rate(lecturer_2, 'Python', 7)
student_2.rate(lecturer_2, 'Python', 5)
student_2.rate(lecturer_2, 'Git', 9)
student_2.rate(lecturer_2, 'Git', 7)
student_2.rate(lecturer_2, 'Git', 7)


some_reviewer = Reviewer('Jimi', 'Acha-Acha')
some_reviewer.courses_attached += ['Python', 'Git']

reviewer_2 = Reviewer('Jeronimo', 'Junior')
reviewer_2.courses_attached += ['Python', 'Git']


some_reviewer.rate_hw(student_best, 'Python', 7)
some_reviewer.rate_hw(student_best, 'Python', 9)
some_reviewer.rate_hw(student_best, 'Python', 10)
some_reviewer.rate_hw(student_best, 'Git', 10)
some_reviewer.rate_hw(student_best, 'Git', 7)
some_reviewer.rate_hw(student_best, 'Git', 10)


some_reviewer.rate_hw(student_2, 'Python', 5)
some_reviewer.rate_hw(student_2, 'Python', 9)
some_reviewer.rate_hw(student_2, 'Python', 10)
some_reviewer.rate_hw(student_2, 'Git', 9)
some_reviewer.rate_hw(student_2, 'Git', 9)
some_reviewer.rate_hw(student_2, 'Git', 9)











print('Student:')
print(student_best.__str__())
print(student_2.__str__())
print('Lecturer:')
print(cool_lecturer.__str__())
print(lecturer_2.__str__())
print('Reviewer:')
print(some_reviewer.__str__())
print(reviewer_2.__str__())
print(f'Средняя оценка   John Salivan больше чем у  Linda Mazovski ?: {student_best.__lt__(student_2)}')
print(f'Средняя оценка у лектора Mike Vazovski меньше чем у Denzel Washington ?: {cool_lecturer.__lt__(lecturer_2)}')
print(len(student_best.grades))


