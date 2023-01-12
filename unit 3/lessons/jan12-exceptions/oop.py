# Object Orienting Programming

# UML Diagram for class

class Employee:
    def __init__(self, name, email, age, salary, role):
        self.name = name
        self.email = email
        self.age = age
        self.salary = salary
        self.role = role

    def greet(self):
        return f"Hello {self.name}, you are {self.age} years old and work as a {self.role} in our company. Your email address is {self.email}, address."

    def get_email(self):
        return f"Your email adress is {self.email}"

# Create employees

emp1 = Employee(name="Fred Murphy", age=69, salary=3000, role="driver", email='fred@email.com')
emp2 = Employee(name="Fred Murphy2", age=69, salary=3000, role="driver", email='fred2@email.com')

database = [emp1, emp2]

for i in database:
    print(i.greet())
    print(i.get_email())