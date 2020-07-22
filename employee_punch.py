"""
Project: joint-force, employee management system.

Author: Umang A
Date: 22 July 2020

Description: This program provides functions for logging punch in and punch out of employees.


TODO: documentation
TODO: sample on how to use this file
"""
import datetime
def display_current_time():
    current_time = datetime.datetime.now()
    print(f"The time now is {current_time}.")

def punch():
    current_time = datetime.datetime.now()
    print(f"The time now is {current_time}.")
    return current_time