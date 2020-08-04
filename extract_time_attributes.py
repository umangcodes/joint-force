"""
Project: Generic
Author: Umang A
Date: 03 August 2020

Description:    This module provides functions to extract time attributes such as hour and minutes from a
                time stamp or time delta objects.
        ========================================================================================================
                                                    How it works?
        ========================================================================================================
        1. Import module
        2. use function extract_time_with_attributes(ARG1,ARG2)

        3. ARG1 = 1 for extracting information from time stamp
        4. ARG2 = timestamp
                                OR
        3. ARG1 = for extracting information from time delta object
        4. ARG2 = timedelta.seconds

Modified: NONE
"""

import global_logic_flags
import datetime


def extract_attributes_from_timestamp(input_timestamp):
    """
    This function returns two values. The input to the function is timestamp
    :return:
    value 1 = hour
    value 2 = min
    """
    output_hour = input_timestamp.hour
    output_min = input_timestamp.minute
    return output_hour, output_min


def extract_attributes_from_timedelta(input_seconds):
    """
    This function returns two values. The input tot he function is the seconds attribute of timedelta object
    :return:
    value 1 = hour
    value 2 = min
    """
    output_hour = input_seconds // 3600
    output_min = input_seconds // 60 - (output_hour * 60)
    # To extract minutes of an hour from the total minutes of a day.
    return output_hour, output_min


def extract_time_with_attributes(extraction_method, input_value):
    """

    :param extraction_method:   1 for extraction from timestamp
                                2 for extraction from timedelta
    :param input_value:         timestamp for method 1
                                seconds for timedelta
    :return:
    value 1 = hour
    value 2 = min
    """
    try:
        if extraction_method == 1:
            if global_logic_flags.system_debug == 1:
                print("Extracting time attributes using timestamp method")
            output = extract_attributes_from_timestamp(input_value)
            return output[0],output[1]
        elif extraction_method == 2:
            if global_logic_flags.system_debug == 1:
                print("Extracting time attributes using timedelta method")
            output = extract_attributes_from_timedelta(input_value)
            return output[0], output[1]
        else:
            print(f"wrong method selected ==> {extraction_method}")
    except:
        print("Something went wrong with the extraction process.")

"""
time_now = datetime.datetime.now()

b = extract_attributes_from_timestamp(time_now)
print(b)
print(b[0])
print(b[1])
"""