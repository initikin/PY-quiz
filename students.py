from itertools import chain


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
        return (f"Имя: {self.name} \nФамилия {self.surname} \nСредняя оценка за лекции {sum(self.rates.values())/len(self.rates)}")

    def __eq__(self, other):
        if isinstance(other, Lecture):
            return sum(self.rates.values())/len(self.rates) == sum(other.rates.values())/len(other.rates)
        return False

    def __lt__(self, other):
        if isinstance(other, Lecture):
            return sum(self.rates.values())/len(self.rates) < sum(other.rates.values())/len(other.rates)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecture):
            return sum(self.rates.values()) / len(self.rates) <= sum(other.rates.values()) / len(other.rates)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecture):
            return sum(self.rates.values()) / len(self.rates) > sum(other.rates.values()) / len(other.rates)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecture):
            return sum(self.rates.values()) / len(self.rates) >= sum(other.rates.values()) / len(other.rates)
        return NotImplemented

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
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


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

    def __str__(self):
        all_grades = list(chain.from_iterable(self.grades.values()))
        average_rate = sum(all_grades)/len(self.grades)
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{average_rate }\n'
                   f'Курсы в процессе{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses}')
        return result

    def __eq__(self, other):
        if isinstance(other, Student):
            all_grades = list(chain.from_iterable(self.grades.values()))
            average_rate = sum(all_grades) / len(self.grades)
            other_all_grades = list(chain.from_iterable(other.grades.values()))
            other_average_rate = sum(other_all_grades) / len(other.grades)
            return average_rate == other_average_rate
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            all_grades = list(chain.from_iterable(self.grades.values()))
            average_rate = sum(all_grades) / len(self.grades)
            other_all_grades = list(chain.from_iterable(other.grades.values()))
            other_average_rate = sum(other_all_grades) / len(other.grades)
            return average_rate < other_average_rate
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            all_grades = list(chain.from_iterable(self.grades.values()))
            average_rate = sum(all_grades) / len(self.grades)
            other_all_grades = list(chain.from_iterable(other.grades.values()))
            other_average_rate = sum(other_all_grades) / len(other.grades)
            return average_rate <= other_average_rate
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            all_grades = list(chain.from_iterable(self.grades.values()))
            average_rate = sum(all_grades) / len(self.grades)
            other_all_grades = list(chain.from_iterable(other.grades.values()))
            other_average_rate = sum(other_all_grades) / len(other.grades)
            return average_rate > other_average_rate
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            all_grades = list(chain.from_iterable(self.grades.values()))
            average_rate = sum(all_grades) / len(self.grades)
            other_all_grades = list(chain.from_iterable(other.grades.values()))
            other_average_rate = sum(other_all_grades) / len(other.grades)
            return average_rate >= other_average_rate
        return NotImplemented


def compare_student (students, course):
    total_average = 0
    i = 0
    if isinstance(students, list):
        for e in students:
            if isinstance(e, Student):
                total_average += sum(e.grades[course])
                i += 1
    return total_average / i


def compare_lectors(lectors, course):
    total_average = 0
    i = 0
    if isinstance(lectors, list):
        for e in lectors:
            if isinstance(e, Lecture):
                if course in e.rates:
                    #print(e.rates[course])
                    total_average += e.rates[course]
                    i += 1
    return total_average / i

delimiter = "******************************************"
student1 = Student('Ivan', 'Nikitin', 'male')
student2 = Student('Gwido', 'van Rossum', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['HTML']
student2.courses_in_progress += ['Linux']
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['FreeBSD']
student2.finished_courses += ['Network']
lecture1 = Lecture("Mark", "Lutz")
lecture2 = Lecture("Michael", "Lucas")
lecture1.courses_attached += ['Python']
lecture2.courses_attached += ['Linux']
lecture2.courses_attached += ['FreeBSD']
reviewer1 = Reviewer("Bjarne", "Staroustrup")
reviewer2 = Reviewer("Richard", "Stallman")
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Linux']
reviewer1.courses_attached += ['FreeBSD']
reviewer1.courses_attached += ['HTML']
reviewer2.courses_attached += ['HTML']
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Linux']
student1.rate_lecture(lecture1, 'Python', 10)
student2.rate_lecture(lecture1, 'Python', 7)
student1.rate_lecture(lecture2, 'Python', 9)
student2.rate_lecture(lecture2, 'Linux', 3)
student2.rate_lecture(lecture2, 'FreeBSD', 8)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'HTML', 8)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer2.rate_hw(student2, 'Linux', 6)
print(lecture1.rates)
print(lecture2.rates)
print(delimiter)
print(lecture1)
print(lecture2)
print(delimiter)
print(reviewer1)
print(reviewer2)
print(delimiter)
print(student1)
print(student2)
list_of_students = []
list_of_lectors = []
print(delimiter)
print (lecture2 < lecture1)
print (lecture2 > lecture1)
print(student1 == student2)
print(student1 > student2)
print(student1 < student2)
print(delimiter)
list_of_students.append(student1)
list_of_students.append(student2)
print(compare_student(list_of_students, 'Python'))
list_of_lectors.append(lecture1)
list_of_lectors.append(lecture2)
print(delimiter)
print(compare_lectors(list_of_lectors, 'Python'))