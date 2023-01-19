class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        if not isinstance(name, str) or not isinstance(age, int):
            raise TypeError

    def __repr__(self):
        return f"[Person Class] with person: {self.name, self.age}"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __repr__(self) -> str:
        return f"[Student Class] with student: {self.name,self.age,self.grade}"

    def get_grade(self):
        return self.grade


class Classroom:
    def __init__(self):
        self.students = []

    def __repr__(self) -> str:
        return f"[Classroom Class] with students: {self.students}"

    def add(self, new_student):
        self.students.append(new_student)

    def remove(self, student):
        self.students = [value for value in self.students if value != student]

    def average(self):
        total = 0

        for i in self.students:
            total += int(i.grade)

        return total / len(self.students)

    
comsci = Classroom()
bob = Student(name='John Doe', age=16, grade='78')
angel = Student(name="Angel", age=23, grade='34')

comsci.add(new_student=bob)
comsci.add(new_student=angel)

print(comsci.average())


