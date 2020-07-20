class Employee():
    def __init__(self,name,start_time,end_time,location):
        self.employee_name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.shift_type = ""
    def __repr__(self):
        return f"Employee {self.employee_name} is working for {self.shift_type} today from {self.start_time} till {self.end_time} at {self.location}"
    def calculate_shift_type(self):
        time_difference = self.end_time - self.start_time
        if time_difference > 4.30:
            self.shift_type = "full time"
        else:
            self.shift_type = "half time"