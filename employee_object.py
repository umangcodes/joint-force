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
        """
        self.break_info = [{"break_estimate_1": 0, "break_estimate_2": 0, "break_estimate_long": 0},
                           {"break_actual_1": 0, "break_actual_2": 0, "break_actual_long": 0}]
        """#TODO: use this dictonary to track the object attributes instead of using the attributes.
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

    def estimate_break_time_with_dict(self):
        if self.punch_status == "NOT SIGNED IN":
            if self.shift_type == "full time":#TODO: another if loop which will check if the actual time is available or not and if not then calculate using admin data start time
                estimate_break_time_dict = self.break_info[1]
                estimate_break_time_dict["break_estimate_1"]= datetime.timedelta(hours=2)
                estimate_break_time_dict["break_estimate_1"] = self.start_time + estimate_break_time_dict["break_estimate_1"]#TODO: Fault....function present to add self.actual_start_time also contains date.
                estimate_break_time_dict["break_estimate_long"] = estimate_break_time_dict["break_estimate_1"] + datetime.timedelta(hours=2)
                estimate_break_time_dict["break_estimate_2"] = estimate_break_time_dict["break_estimate_long"] + datetime.timedelta(hours=2, minutes=30)
            elif self.shift_type == "half time":
                estimate_break_time_dict = self.break_info[1]
                estimate_break_time_dict["break_estimate_1"] = datetime.timedelta(hours=2,minutes=30)
                estimate_break_time_dict["break_estimate_1"] = self.start_time + estimate_break_time_dict["break_estimate_1"]
                estimate_break_time_dict["break_estimate_2"] = f"N/A"
                estimate_break_time_dict["break_estimate_long"] = f"N/A"
            else:
                print(f"ERROR: cannot find value of <object> attribute shift_type\n\t\t\t|object.shift_type = {self.punch_status}| ")
        elif self.punch_status == "SIGNED IN":
            if self.shift_type == "full time":#TODO: another if loop which will check if the actual time is available or not and if not then calculate using admin data start time
                estimate_break_time_dict = self.break_info[1]
                estimate_break_time_dict["break_estimate_1"] = datetime.timedelta(hours=2)
                estimate_break_time_dict["break_estimate_1"] = self.actual_start_time + estimate_break_time_dict["break_estimate_1"]#TODO: Fault....function present to add self.actual_start_time also contains date.
                estimate_break_time_dict["break_estimate_long"] = estimate_break_time_dict["break_estimate_1"] + datetime.timedelta(hours=2)
                estimate_break_time_dict["break_estimate_2"] = estimate_break_time_dict["break_estimate_long"] + datetime.timedelta(hours=2, minutes=30)
            elif self.shift_type == "half time":
                estimate_break_time_dict = self.break_info[1]
                estimate_break_time_dict["break_estimate_1"] = datetime.timedelta(hours=2,minutes=30)
                estimate_break_time_dict["break_estimate_1"] = self.actual_start_time + estimate_break_time_dict["break_estimate_long"]
                estimate_break_time_dict["break_estimate_2"] = f"N/A"
                estimate_break_time_dict["break_estimate_long"] = f"N/A"
            else:
                print(f"ERROR: cannot find value of <object> attribute shift_type\n\t\t\t|object.shift_type = {self.punch_status}| ")
                #TODO: fault the punch in will provide a timestamp instead of time. The time stamp is essential so do not remove it, instead find a way to trim down the date from timestamp
        if self.punch_status == "SIGNED OUT":
            estimate_break_time_dict = self.break_info[1]
            print(f"shift over! breaks taken at \n break 1 at: {estimate_break_time_dict['break_estimate_1']}\n break 2 at: {estimate_break_time_dict['break_estimate_2']}\n long break at: {estimate_break_time_dict['break_estimate_long']}")
    def change_start_time_feasibility(self):
        """
        This function will compare two times for authorizing the change in global variables which in turn will change the start & end time
        while also providing the logic.
        - start time must not be > end time
        - difference between start and end must not be < 1 hour(use global variables for this)
        - difference between start and end time must not be > 12 hours(use global variables for this)
        - authorization from sup/mgr to change time if LATE condition occurs
        :return:
        """
        current_time = datetime.datetime.now()
        current_time_hour = current_time.second
        print(type(current_time_hour))
        print(self.start_time.seconds//3600)
        start_time_h = self.start_time.seconds//3600
        if current_time_hour <= start_time_h:
            print("Possible")

        else:
            print("you are late for this operation")