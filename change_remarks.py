"""
this file will hold functions which will generate remarks

types of  remarks.
late
early

special notes

"""
import input_time_converter
def initial_remark(start_time,actual_start_time):
    start_time = start_time // 3600
    actual_start_time = actual_start_time // 3600
    print(f"\n\n\t\t\tprocessed start time: {start_time}")
    input()# TODO: issue with calculating the delay or early time.
    if abs(start_time - actual_start_time) >= 5:
        # 300 seconds == 5 mins
        if start_time > actual_start_time:
            return f"early by {abs(start_time - actual_start_time)} mins"
        elif start_time < actual_start_time:
            return f"late by {abs(start_time - actual_start_time)} mins"
    else:
        return f"on time"

"""
a = input_time_converter.Format_time.convert_to_timedelta()
b = input_time_converter.Format_time.convert_to_timedelta()
print(a.seconds)
print(b.seconds)
initial_remark(a.seconds,b.seconds)
"""