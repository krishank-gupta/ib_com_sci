# Functional Programming
Emp_1 = { "Name": "Frank Murphy", "Email": "frank.murphy@company.xy", "Work": "Driver", "Age": 39, "Salary": 30000 }
Emp_2 = { "Name": "Krishank Gupta", "Email": "krish.gupta@gmail.com", "Work": "Programmer", "Age": 17, "Salary": 1000000 }
Emp_3 = { "Name": "Chris Price", "Email": "chris.price@company.xy", "Work": "Hotel Owner", "Age": 60, "Salary": 5000000 }
Emp_4 = { "Name": "John Doe", "Email": "john.doe@company.xy", "Work": "Receptionalist", "Age": 25, "Salary": 20000 }
Emp_5 = { "Name": "Jane Doe", "Email": "jane.doe@company.xy", "Work": "Data Analyst", "Age": 23, "Salary": 100000 }

def greet(employee_data):
    return f"Hello {employee_data['Name']}, you are {employee_data['Age']} years old and work as a {employee_data['Work']} in our company. Your email address is {employee_data['Email']}, address."

database = [Emp_1, Emp_2, Emp_3, Emp_4, Emp_5]

for i in database:
    print(greet(i))

