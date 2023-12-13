from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employee = Employee.get_all()
    for person in employee:
        print(person)


def find_employee_by_name():
    name = input("Please enter Employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print("No employee found")


def find_employee_by_id():
    employee_id = input("Please enter Employee ID: ")
    employee = Employee.find_by_id(employee_id)
    print(employee) if employee else print("Not a valid ID")


def create_employee():
    name = input("Please input Employee name: ")
    job = input("What is your job?: ")
    department_id = int(input("What is your department ID?: "))
    try:
        Employee.create(name,job,department_id)
        print(f"{name} was created")
    except:
        print(f"Error creating {name}")


def update_employee():
    name = input("Please input Employee name: ")
    job = input("What is your job?: ")
    department_id = int(input("What is your department ID?: "))
    print(name,job,department_id)
    print(Department.find_by_id(department_id))
    if Department.find_by_id(department_id):
        try:
            Employee.update(name,job,department_id)
        except:
            print("Error occurred")
    else:
        print("Department not found")


def delete_employee():
    employee_id = int(input("Which Employee id do you want gone?: "))

    if employee := Employee.find_by_id(employee_id):
        employee.delete()
        print(f'Employee {employee_id} deleted')
    else:
        print(f'Employee {employee_id} not found')
        



def list_department_employees():
    department_id = int(input("Please input your department ID: "))
    if department := Department.find_by_id(department_id):
    #     employees = Employee.get_all()
    #     # print(employees)
    #     for employee in employees:
    #         # print(employee)
    #         # print(type(employee.department_id))
    #         # print(type(department_id))
    #         if employee.department_id == department_id:
    #             print(employee) 
    # else:
    #     print("This Department does not exist")
        for employee in department.employees():
            print(employee)
    else: 
        print("This Department does not exist")