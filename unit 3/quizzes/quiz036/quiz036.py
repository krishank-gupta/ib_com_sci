class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return self.grade

class Classroom:
    def __init__(self):
        self.students = []

    def add(self, new_student):
        self.students.append(new_student)

    def remove(self, student):
        self.students = [value for value in self.students if value != student]

    def average(self):
        return self.students

    
comsci = Classroom()
bob = Student(name='John Doe', age=16, grade='78%')
comsci.add(new_student=bob)
print(comsci.average())

