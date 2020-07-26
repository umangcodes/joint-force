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
        self.punch_status = "NOT SIGNED IN"
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
        if self.punch_status == "NOT SIGNED IN":
            if self.shift_type == "full time":#TODO: another if loop which will check if the actual time is available or not and if not then calculate using admin data start time
                self.break_est_1 = datetime.timedelta(hours=2)
                self.break_est_1 = self.start_time + self.break_est_1#TODO: Fault....function present to add self.actual_start_time also contains date.
                self.break_est_long = self.break_est_1 + datetime.timedelta(hours=2)
                self.break_est_2 = self.break_est_long + datetime.timedelta(hours=2, minutes=30)
            elif self.shift_type == "half time":
                self.break_est_1 = datetime.timedelta(hours=2,minutes=30)
                self.break_est_1 = self.start_time + self.break_est_1
                self.break_est_2 = f"N/A"
                self.break_est_long = f"N/A"
            else:
                print(f"ERROR: cannot find value of <object> attribute shift_type\n\t\t\t|object.shift_type = {self.punch_status}| ")
        elif self.punch_status == "SIGNED IN":
            if self.shift_type == "full time":#TODO: another if loop which will check if the actual time is available or not and if not then calculate using admin data start time
                self.break_est_1 = datetime.timedelta(hours=2)
                self.break_est_1 = self.actual_start_time + self.break_est_1#TODO: Fault....function present to add self.actual_start_time also contains date.
                self.break_est_long = self.break_est_1 + datetime.timedelta(hours=2)
                self.break_est_2 = self.break_est_long + datetime.timedelta(hours=2, minutes=30)
            elif self.shift_type == "half time":
                self.break_est_1 = datetime.timedelta(hours=2,minutes=30)
                self.break_est_1 = self.actual_start_time + self.break_est_1
                self.break_est_2 = f"N/A"
                self.break_est_long = f"N/A"
            else:
                print(f"ERROR: cannot find value of <object> attribute shift_type\n\t\t\t|object.shift_type = {self.punch_status}| ")
                #TODO: fault the punch in will provide a timestamp instead of time. The time stamp is essential so do not remove it, instead find a way to trim down the date from timestamp
        if self.punch_status == "SIGNED OUT":
            print(f"shift over! breaks taken at \n break 1 at: {self.break_actual_1}\n break 2 at: {self.break_actual_2}\n long break at: {self.break_actual_long}")