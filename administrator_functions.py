import greeting_messages
import main_menu
import input_time_converter
# TODO: added authorization for access to this menu
def select_function():
    select_operation = int(input(greeting_messages.admin_functions_message))
    if select_operation == 1:
        select_operation = int(input(greeting_messages.admin_display_options))
        if select_operation == 1:
            index_of_employee = main_menu.find_employee(1)
            employee_object = main_menu.employee_list[index_of_employee]
            print(f"{employee_object.employee_name}\t||\t{employee_object.start_time}\t||\t{employee_object.end_time}")
        elif select_operation == 2:
            for employee in main_menu.employee_list:
                print(employee.employee_name)
        elif select_operation == 3:
            time_filter = input_time_converter.Format_time.convert_to_timedelta()
            for employee in main_menu.employee_list:
                if employee.start_time.seconds//3600 >= time_filter.seconds//3600:
                    print(employee.employee_name)
    else:
        print("try again")