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
import os
import sys
import greeting_messages

while(1):
    print("Welcome to employee management system!")
    try:
        user_option = int(input(f"{greeting_messages.greeting_message}"))
        if user_option == 1:
            os.system('cls')
            main_menu.add_employee()
        elif user_option == 2:
            os.system('cls')
            main_menu.remove_employee()
        elif user_option == 3:
            try:
                os.system('cls')
                user_option = int(input(f"{greeting_messages.attribute_change}"))
                main_menu.change_employee_attributes(user_option)
            except:
                print("Invalid")
        elif user_option == 4:
            try:
                os.system('cls')
                user_option = int(input(f"{greeting_messages.find_employee}"))
                main_menu.find_employee(user_option)
            except:
                print("invalid")
        elif user_option == 5:
            os.system('cls')
            main_menu.display_employees()
        elif user_option == 6:
            os.system('cls')
            main_menu.day_end()
        elif user_option == 7:
            os.system('cls')
            user_option = int(input(greeting_messages.punch_options))
            main_menu.employee_punch_record(user_option)
        elif user_option == 0:
            sys.exit(0)#TODO:not working
    except:
        os.system('cls')
        print("Invalid command. Please enter correct type of data.")
        input("Press any key to continue.")