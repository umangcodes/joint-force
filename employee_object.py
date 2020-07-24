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