"""
this file will hold functions which will generate remarks

types of  remarks.
late
early

special notes

"""
import input_time_converter
import extract_time_attributes
import datetime

def initial_remark(start_time, actual_start_time):
    # deprecated function. Make a new one
    print(f"start time seconds:(punch in) {start_time}")
    print(f"start time seconds:(actual punch {actual_start_time})")
    stamp_time = extract_time_attributes.extract_time_with_attributes(1, actual_start_time)
    delta_time = extract_time_attributes.extract_time_with_attributes(2, start_time)
    actual_start_time = input_time_converter.Format_time.convert_to_timedelta(1, input_hours=stamp_time[0],
                                                                              input_minutes=stamp_time[1])
    # stamp_time[0] = hour
    # stamp_time[1] = min
    # transferring values
    # start_time = delta_time
    # actual_start_time = stamp_time
    print(f"\n\n\t\t\tprocessed start time: {start_time}")
    input()  # TODO: issue with calculating the delay or early time.
    print(f"start_time = {type(start_time)}\nactual_start_time = {type(actual_start_time)}")
    if abs(start_time - actual_start_time) >= datetime.timedelta(minutes=5):
        # 300 seconds == 5 mins
        if start_time > actual_start_time:
            return f"early by {abs(start_time - actual_start_time)} mins"
        elif start_time < actual_start_time:
            return f"late by {abs(start_time - actual_start_time)} mins"
    else:
        return f"on time"


def shift_end_remark(end_time, actual_end_time):
    print(f"start time seconds:(punch in) {end_time}")
    print(f"start time seconds:(actual punch {actual_end_time})")
    stamp_time = extract_time_attributes.extract_time_with_attributes(1, actual_end_time)
    delta_time = extract_time_attributes.extract_time_with_attributes(2, end_time)
    actual_end_time = input_time_converter.Format_time.convert_to_timedelta(1, input_hours=stamp_time[0],
                                                                              input_minutes=stamp_time[1])
    # stamp_time[0] = hour
    # stamp_time[1] = min
    # transferring values
    # start_time = delta_time
    # actual_start_time = stamp_time
    print(f"\n\n\t\t\tprocessed start time: {end_time}")
    input()  # TODO: issue with calculating the delay or early time.
    print(f"start_time = {type(end_time)}\nactual_start_time = {type(actual_end_time)}")
    if abs(end_time - actual_end_time) >= datetime.timedelta(minutes=5):
        # 300 seconds == 5 mins
        if end_time > actual_end_time:
            return f"early by {abs(end_time - actual_end_time)} mins"
        elif end_time < actual_end_time:
            return f"late by {abs(end_time - actual_end_time)} mins"
    else:
        return f"on time"


def special_notes(message_code, special_note_string):
    if special_note_string == "Late":  # remark if the employee has already informed about being late.
        pass
    elif special_note_string == "Early":  # remark if manager wants employee to start early.
        pass
    elif special_note_string == "Help":  # remark for helper shifts
        pass
    elif special_note_string == "Issue":  # remark for any issues
        pass
    elif special_note_string == "Special":  # any special remarks
        pass


"""
a = input_time_converter.Format_time.convert_to_timedelta()
b = input_time_converter.Format_time.convert_to_timedelta()
print(a.seconds)
print(b.seconds)
initial_remark(a.seconds,b.seconds)
"""
