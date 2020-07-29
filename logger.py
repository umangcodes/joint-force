"""
Project: Individual project but based on employee management system(Joint Force)

Author: Umang A
Description: This file generates a log from the available data and creates a csv format file.

In this case, available data is created by day_end function

"""

import datetime
import authorization
class Logger_data():
    def __init__(self,supervisor):
        self.filename = datetime.date
        self.creation_time = datetime.datetime.now()
        self.supervisor = supervisor

    def __repr__(self):
        return f" File : {self.filename} created at {self.creation_time} submitted by {self.supervisor}"

    def generate_output_file(self):
        """
        This function will take all the data and convert the data into output file format while saving it.
        :return:
        """
        pass
    @staticmethod
    def log_entry():
        sup_id = input("Supervisor/Manger ID: ")
        sup_pass = input("Supervisor/Manager Password: ")
        if authorization.authorize(sup_id,sup_pass) == True:
            print("Authorized")
            return sup_id
        elif authorization.authorize(sup_id,sup_pass) == False:
            print("Please try again!")