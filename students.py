class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname, rates = 0):
        super().__init__(name, surname)
        self.rates = {}
    def __str__(self):
        return (f"Имя: {self.name} \n Фамилия {self.surname} \n Средняя оценка за лекции {sum(self.rates.values())/len(self.rates)}")
        #return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {sum(self.rates.values())}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecture: Lecture, course, rate):
        if 0 <= rate <= 10:
            # for l in lecture.courses_attached:
            #     if l == course:
            #         Lecture.rates = {course: rate}
            #     else:
            #         print(f"Этот преподователь не ведет данный курс")
            if course in lecture.courses_attached and course in self.courses_in_progress:
                if course in lecture.rates:
                    average_rate = (sum(lecture.rates.values())+rate) / (len(lecture.rates)+1)
                    lecture.rates[course] = average_rate
                else:
                    lecture.rates[course] = rate
                print(f"преподователь {lecture.name} {lecture.surname} за ведение курса {course} получил оценку {rate}")
            else:
                print(f"преподователь {lecture.name} {lecture.surname} не ведет данный курс {course}")
        else:
            print(f"оценки выставляются по 10-балльной шкале, вы ввели {rate}")

student1 = Student('Ivan', 'Nikitin', 'male')
student2 = Student('Gwido', 'van Rossum', 'male')
student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Linux']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['FreeBSD']
lecture1 = Lecture("Mark", "Lutz")
lecture2 = Lecture("Michael", "Lucas")
lecture1.courses_attached += ['Python']
lecture2.courses_attached += ['Linux']
lecture2.courses_attached += ['FreeBSD']
student1.rate_lecture(lecture1, 'Python', 10)
student2.rate_lecture(lecture1, 'Python', 3)
student1.rate_lecture(lecture2, 'Python', 10)
student2.rate_lecture(lecture2, 'Linux', 3)
student2.rate_lecture(lecture2, 'FreeBSD', 8)
print(lecture1.rates)
print(lecture2.rates)
print(lecture1)
print(lecture2)