"""
give options to the admin
    options:
    - add employee
    - remove employee
    - change employee params
    - inquire employee params
    - submit day end data
    - break intimation(feature)
    - change employee location/role
    :return:
    """
from employee_object import Employee
employee_list = []
def find_employee(method):
    """

    :param method:  value 1 for finding employee by name
                    value 2 for finding employee by start time
                    value 3 for finding employee by end time
    :return:
    """
    if method == 1:
        find_employee_name = input("please enter employee you are looking for:")
        for element in employee_list:
            if find_employee_name.title() == element.employee_name.title():
                print(element)
                return employee_list.index(element)
                break
        else:
            print("employee not found")
    elif method == 2:
        find_employee_by_start_time = int(input("Please enter start time: "))
        for element in employee_list:
            if find_employee_by_start_time == element.start_time:
                print(element)
    elif method == 3:
        find_employee_by_end_time = int(input("Please enter end time: "))
        for element in employee_list:
            if find_employee_by_end_time == element.end_time:
                print(element)

def add_employee():
    add_employee = input("enter employee name: ")
    start_time = int(input("please enter start time: "))
    end_time = int(input("please enter end time: "))
    duty = input("please enter employee duty: ")
    new_employee = add_employee.title()
    new_employee = Employee(new_employee,start_time,end_time,duty)
    new_employee.calculate_shift_type()
    employee_list.append(new_employee)

def remove_employee():
    index_of_employee = find_employee(1)
    remove_employee = employee_list[index_of_employee]
    employee_list.pop(index_of_employee)
    print("employee removed.\n Details of employee removed: {remove_employee}")

def inquire_employee_attributes():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    print(employee_object)
    print(employee_list)
    
def change_employee_shift_start_time():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    changed_start_time = int(input("Please enter change in start time (hhmm): "))
    employee_object.start_time = changed_start_time
    employee_object.calculate_shift_type()

def change_employee_shift_end_time():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    changed_end_time = int(input("Please enter change in end time (hhmm): "))
    employee_object.start_time = changed_end_time
    employee_object.calculate_shift_type()

def change_employee_role():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    changed_role = input("Please enter change in end time (hhmm): ")
    employee_object.start_time = changed_role

def change_employee_attributes(change_attribute_option):
    if change_attribute_option == 1:
        change_employee_shift_start_time()
    elif change_attribute_option == 2:
        change_employee_shift_end_time()
    elif change_attribute_option == 3:
        change_employee_role()
    else:
        print("invalid command")


def day_end():
    for _ in employee_list:
        print(_)