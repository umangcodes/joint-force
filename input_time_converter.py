"""
what this file will do?

take user input

hh & mm in string and convert the string to int

input the values in the datetime.time()

"""
import datetime

class Format_time():
    def __init__(self):
        pass
    def __repr__(self):
        return f"convert user time input into time or timedelta object"
    @staticmethod
    def convert_to_time():
        try:
            user_input_hh = int(input(f"Please enter the hour(hh): "))
            user_input_mm = int(input(f"Please enter the minutes(mm): "))
            user_input_time_formatted = datetime.time(hour=user_input_hh, minute=user_input_mm)
            return user_input_time_formatted
        except:
            print(f"Please input appropriate values.")

    @staticmethod
    def convert_to_timedelta():
        try:
            user_input_hh = int(input(f"Please enter the hour(hh): "))
            user_input_mm = int(input(f"Please enter the minutes(mm): "))
            user_input_timedelta_formatted = datetime.timedelta(hours=user_input_hh, minutes=user_input_mm)
            return user_input_timedelta_formatted
        except:
            print(f"Please input appropriate values.")

"""
a = Format_time.convert_to_timedelta()
b = Format_time.convert_to_timedelta()
time_difference = b-a
if time_difference >= datetime.timedelta(hours=4):
    print("success")
"""