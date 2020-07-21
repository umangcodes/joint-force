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

- add break time functionality
"""
import main_menu

#def menu_for_admin():


while(1):
    print("Welcome to employee management system!")
    try:
        user_option = int(input("""
Please input from the following options:
1. add employee
2. remove employee
3. change employee attributes
4. find employee
5. display information
6. day end(Admin rights required)
==> """))
        if user_option == 1:
            main_menu.add_employee()
        elif user_option == 2:
            main_menu.remove_employee()
        elif user_option == 3:
            try:
                user_option = int(input("""
To change start time press 1
To change end time press 2
To change role press 3
"""))
                main_menu.change_employee_attributes(user_option)
            except:
                print("Invalid")
        elif user_option == 4:
            try:
                user_option = int(input("""
To find by name press 1
To find by start time press 2
To find by end time press 3
                    """))
                main_menu.find_employee(user_option)
            except:
                print("invalid")
        elif user_option == 5:
            main_menu.display_employees()
        elif user_option == 6:
            main_menu.day_end()
    except:
        print("Invalid command. Please enter correct type of data.")


