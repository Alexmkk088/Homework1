class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in
            lecturer.courses_attached and course in 
            self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def value_s(self):
        rate = 0
        if len(self.grades.values()) == 0:
            return 'Ошибка'
        else:
            for rate_s in self.grades.values():
                for i in rate_s:
                    rate += i
                    average_rate_s = rate / len(rate_s)
                return average_rate_s

    def __str__(self):
        infr = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {self.value_s()}\n'
               f'Курсы в процессе изучения: '
               f'{", ".join(self.courses_in_progress)}\n'
               f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return infr

    def __lt__(self, other):
        if not isinstance(other, Student) and isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        if (Student.rate_l(self, other) < 
            Reviewer.rate_hw(self, other)):
            return 'Оценка студента выше оценки лектора'
        elif (Student.rate_l(self, other) > 
              Reviewer.rate_hw(self, other)):
            return 'Оценка лектора выше оценки студента'
        else:
            return 'Оценки равны'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def value_l(self):
        rate = 0
        if len(self.grades.values()) == 0:
            return 'Ошибка'
        else:
            for rate_l in self.grades.values():
                for i in rate_l:
                    rate += i
                    average_rate_l = rate / len(rate_l)
                return average_rate_l

    def __str__(self):
        infr = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {self.value_l()}')
        return infr


class Reviewer(Mentor): 
    def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []

    def __str__(self):
        infr = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return infr

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman ', 'man')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['C++']
student_1.finished_courses += ['Java']

student_2 = Student('Lelik', 'Bolik', 'man')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['C++']
student_2.finished_courses += ['Java']

lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached += ['C++']

lecturer_2 = Lecturer('Bob', 'Braun')
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewer('Thomas', 'Dyson')
reviewer_1.courses_attached += ['C++']
reviewer_1.courses_attached += ['Java']

reviewer_2 = Reviewer('Harry', 'Potter')
reviewer_2.courses_attached += ['C++']
reviewer_2.courses_attached += ['Java']

reviewer_1.rate_hw(student_1, 'C++', 9)
reviewer_2.rate_hw(student_1, 'Java', 7)

reviewer_1.rate_hw(student_2, 'C++', 8)
reviewer_2.rate_hw(student_2, 'Java', 9)

student_1.rate_l(lecturer_1, 'C++', 8)
student_1.rate_l(lecturer_2, 'Java', 10)

student_2.rate_l(lecturer_1, 'C++', 6)
student_2.rate_l(lecturer_2, 'Java', 7)

print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(student_1)
print()
print(student_2)
