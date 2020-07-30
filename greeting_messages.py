attribute_change = """
To change start time press 1
To change end time press 2
To change role press 3
==> """

find_employee = """
To find by name press 1
To find by start time press 2
To find by end time press 3
==> """

greeting_message = """
Please input from the following options:
1. add employee
2. remove employee
3. change employee attributes
4. find employee
5. display information
6. day end(Admin rights required)
7. punch options
8. breaks options

0. quit
==> """

punch_options = """
Press 1 to Punch in
Press 2 to Punch out
"""

time_overflow = "Time you entered is invalid!"

break_options = """
Options available:
1. break punch in
2. break punch out
"""
break_options_error = "INVALID.\n No such option found. Please enter correct option."
#TODO: check whether multi line f strings exist or not?
#TODO: if they do place a multiline f string which can display the punch status
