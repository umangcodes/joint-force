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
import input_time_converter
import employee_punch
import sys
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
    elif method == 2:#feature implement all employees after that time
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
    try:
        start_time = input_time_converter.Format_time.convert_to_timedelta()
        end_time = input_time_converter.Format_time.convert_to_timedelta()
    except:
        print("Enter numerical values (hhmm) format only!")
    duty = input("please enter employee duty: ")
    new_employee = add_employee.title()
    new_employee = Employee(new_employee,start_time,end_time,duty)
    new_employee.calculate_shift_type()
    employee_list.append(new_employee)

def remove_employee():
    index_of_employee = find_employee(1)
    remove_employee = employee_list[index_of_employee]
    employee_list.pop(index_of_employee)
    print(f"employee removed.\n Details of employee removed: {remove_employee}")

def inquire_employee_attributes():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    print(employee_object)
    print(employee_list)

def change_employee_shift_start_time():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    try:
        changed_start_time = int(input("Please enter change in start time (hhmm): "))
        employee_object.start_time = changed_start_time
        employee_object.calculate_shift_type()

        print("Updated shift schedule")
        print(employee_object.shift_type)
    except:
        print("Oops! something went wrong")

def change_employee_shift_end_time():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    try:
        changed_end_time = int(input("Please enter change in end time (hhmm): "))
        employee_object.end_time = changed_end_time
        employee_object.calculate_shift_type()
    except:
        print("Oops! something went wrong.")

def change_employee_role():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    changed_role = input("Please enter change in role: ")
    employee_object.location = changed_role

def change_employee_attributes(change_attribute_option):
    if change_attribute_option == 1:
        change_employee_shift_start_time()
    elif change_attribute_option == 2:
        change_employee_shift_end_time()
    elif change_attribute_option == 3:
        change_employee_role()
    else:
        print("invalid command")

def display_employees():
    for employee in employee_list:
        print(f"{employee.employee_name}\t||\t{employee.start_time}\t||\t{employee.end_time}\t||\t{employee.shift_type}\t||\t{employee.location}\t||\t{employee.actual_start_time}\t||\t{employee.actual_end_time}")

def day_end():
    for _ in employee_list:
        print(_)

def employee_punch_record(punch_type):
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    if punch_type == 1:
        employee_punch.display_current_time()# module name and function name were same.
        employee_object.actual_start_time = employee_punch.punch()
    elif punch_type == 2:
        employee_punch.display_current_time()
        employee_object.actual_end_time = employee_punch.punch()

