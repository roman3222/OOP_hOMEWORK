class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        course_grades = {}
        courses_attached = []


class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



student_best = Student('John', 'Salivan', 'Famale')
student_best.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Mike', 'Vazovski')
cool_lecturer.courses_attached += ['Python']

student_best.rate(cool_lecturer, 'Python', 9)
student_best.rate(cool_lecturer, 'Python', 9)
student_best.rate(cool_lecturer, 'Python', 9)



rate_reviewer = Reviewer('Jimi', 'Acha-Acha')
rate_reviewer.courses_attached += ['Python']

rate_reviewer.rate_hw(student_best, 'Python', 10)
rate_reviewer.rate_hw(student_best, 'Python', 10)
rate_reviewer.rate_hw(student_best, 'Python', 10)

print(student_best.grades)
print(cool_lecturer.course_grades)


