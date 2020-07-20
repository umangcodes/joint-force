"""
Project: Joint_Force_1

Authors: Umang A, Devam A
Date & Time: 20 July 2020 || 1415 EST

Description: To be updated. See Scope
"""

"""
1. make employee objects
2. shift start time
3. break time
4. shift end time
5. employee location/duty

6. remark/s

7. break_time_dictonary 

[{"break_type": "", "break_start_time": , "break_end_time": , "actual_break_start_time": ,"actual_break_end_time": },
                           "break_type": "", "break_start_time": , "break_end_time": , "actual_break_start_time": ,"actual_break_end_time": },
                           "break_type": "", "break_start_time": , "break_end_time": , "actual_break_start_time": ,"actual_break_end_time": }]
"""
employee_list = []
class Employee():
    def __init__(self,name,start_time,end_time,location):
        self.employee_name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.break_time = []
        self.shift_type = ""
    def __repr__(self):
        return f"Employee {self.employee_name} is working for {self.shift_type} today from {self.start_time} till {self.end_time} at {self.location}"
    def calculate_shift_type(self):
        time_difference = self.end_time - self.start_time
        if time_difference > 4.30:
            self.shift_type = "full time"
        else:
            self.shift_type = "half time"
def menu_for_admin():


    """
    give options to the admin
    options:
    - add employee
    - remove employee
    - change employee params
    - inquire employee params
    - submit day end data
    - break intimation
    - change employee location/role
    :return:
    """
def add_employee():
    add_employee = input("enter employee name: ")
    start_time = int(input("please enter start time: "))
    end_time = int(input("please enter end time: "))
    duty = input("please enter employee duty: ")
    new_employee = add_employee.title()
    new_employee = Employee(new_employee,start_time,end_time,duty)
    new_employee.calculate_shift_type()
    employee_list.append(new_employee)

while(1):
    add_employee()
    find_employee = input("please enter employee you are looking for:")
    for element in employee_list:
        if find_employee.title() == element.employee_name.title():
            print(element)
            break
    else:
        print("employee not found")

