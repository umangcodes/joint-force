"""
TODO: documentation
TODO: sample on how to use this file
"""
import datetime
class Employee():
    def __init__(self,name,start_time,end_time,location,actual_start_time = "NA",actual_end_time = "NA"):
        self.employee_name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.shift_type = ""
        self.actual_start_time = actual_start_time
        self.actual_end_time = actual_end_time
        self.break_est_1 = 0
        self.break_est_2 = 0
        self.break_est_long = 0
        self.break_actual_1 = 0
        self.break_actual_2 = 0
        self.break_actual_long = 0
        self.remark = ""
    def __repr__(self):
        return f"Employee {self.employee_name} is working for {self.shift_type} today from {self.start_time} till {self.end_time} at {self.location}"
    def calculate_shift_type(self):
        time_difference = self.end_time - self.start_time
        print(self.start_time, self.end_time)
        print(time_difference)
        try:
            if time_difference >= datetime.timedelta(hours=4):
                self.shift_type = "full time"
                print("------------------------------------")
            else:
                self.shift_type = "half time"
        except:
            print("Oops! Could not process shift type.\nPlease make sure you enter time in start and end time.")
    def estimate_break_time(self):
        if self.shift_type == "full time":
            datetime.timedelta(hours=2)
        elif self.shift_type == "half time":
            datetime.timedelta(hours=2,minutes=30)