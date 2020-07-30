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
import greeting_messages
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
        find_employee_by_start_time = int(input("Please enter start time: "))#TODO: this feature does not work as intended as the input is of int type
        for element in employee_list:
            if find_employee_by_start_time == element.start_time:
                print(element)
    elif method == 3:
        find_employee_by_end_time = int(input("Please enter end time: "))#TODO: this feature does not work as intended as the input is of int type
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
    new_employee.estimate_break_time()
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
        # here the original time or the time before the new entry is lost as the attribute
        # is overwritten by the new statement TODO:think about a mechanism to solve this issue[cat: data loss]
        temp_storage = employee_object.start_time
        employee_object.start_time = input_time_converter.Format_time.convert_to_timedelta()
        if employee_object.change_start_time_feasibility() == False:
            employee_object.start_time = temp_storage
        employee_object.calculate_shift_type()

        print("Updated shift schedule")
        print(employee_object.shift_type)
    except:
        print("Oops! something went wrong")

def change_employee_shift_end_time():
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    try:
        temp_storage = employee_object.end_time# same issue as above.
        employee_object.end_time = input_time_converter.Format_time.convert_to_timedelta()
        if employee_object.change_end_time_feasibility() == False:
            employee_object.end_time = temp_storage
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
        employee.estimate_break_time()
        print(f"{employee.employee_name}\t||\t{employee.start_time}\t||\t{employee.end_time}\t||\t{employee.shift_type}\t||\t{employee.location}\t||\t{employee.actual_start_time}\t||\t{employee.actual_end_time}\t||\t{employee.break_est_1}\t||\t{employee.break_est_long}\t||\t{employee.break_est_2}\t||\t{employee.break_est_3}")
        print(f"{employee.break_overflow}")
        print(f"{employee.break_actual_1_start}\t{employee.break_actual_1_end}\t")
        print(f"{employee.break_actual_2_start}\t{employee.break_actual_2_end}\t")
        print(f"{employee.break_actual_long_start}\t{employee.break_actual_long_end}\t")
        print(f"{employee.break_actual_3_start}\t{employee.break_actual_3_end}\t")
def display_employees_with_dict():
    for employee in employee_list:
        employee.estimate_break_time()
        employee_break_time = employee.break_info[1]
        print(f"{employee.employee_name}\t||\t{employee.start_time}\t||\t{employee.end_time}\t||\t{employee.shift_type}\t||\t{employee.location}\t||\t{employee.actual_start_time}\t||\t{employee.actual_end_time}\t||\t{employee_break_time['break_estimate_1']}\t||\t{employee_break_time['break_estimate_long']}\t||\t{employee_break_time['break_estimate_2']}")
def day_end():
    for _ in employee_list:
        print(_)

def employee_punch_record(punch_type):
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]  # TODO:employee_object.py is being overwritten by this particular operation which makes this program actually feasible.
    if punch_type == 1:
        employee_punch.display_current_time()  # module name and function name were same.
        employee_object.actual_start_time = employee_punch.punch()
        employee_object.punch_status = "SIGNED IN"
        employee_object.estimate_break_time()
    elif punch_type == 2:
        employee_punch.display_current_time()
        employee_object.actual_end_time = employee_punch.punch()
        employee_object.punch_status = "SIGNED OUT"

def break_op():
    """
    find employee
    change break_actual_x
    :return:
    """
    print("Break options:")
    index_of_employee = find_employee(1)
    employee_object = employee_list[index_of_employee]
    user_break_choice = "1"
    while user_break_choice != "N/A":
        user_break_choice = int(input(greeting_messages.break_options))
        if user_break_choice == 1:
            employee_object.break_punch_in()
            # punch in
            user_break_choice = "N/A"
        elif user_break_choice == 2:
            employee_object.break_punch_out()
            # punch out
            user_break_choice = "N/A"
        else:
            print(greeting_messages.break_options_error)
    print("punched in/out")
            # TODO: add operations to punch in punch out breaks. add attributes to employee_object.py to log actual break punch out
"""
umang = Employee("umang",input_time_converter.Format_time.convert_to_timedelta(),input_time_converter.Format_time.convert_to_timedelta(),"dev")
employee_list.append(umang)
break_op()
"""