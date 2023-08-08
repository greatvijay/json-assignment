import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employee_data_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    employees_data = data['employees']
    employees_list = []

    for emp_data in employees_data:
        employee = Employee(emp_data['Name'], emp_data['DOB'], emp_data['Height'], emp_data['City'], emp_data['State'])
        employees_list.append(employee)

    return employees_list

file_path = 'employee.json'
employee_objects = read_employee_data_from_json(file_path)

# Print the list of Employee objects
for emp in employee_objects:
    print(f"Name: {emp.name}, DOB: {emp.dob}, Height: {emp.height}, City: {emp.city}, State: {emp.state}")
