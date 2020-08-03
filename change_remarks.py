"""
this file will hold functions which will generate remarks

types of  remarks.
late
early

special notes

"""
import input_time_converter
def initial_remark(start_time,actual_start_time):
    # deprecated function. Make a new one
    print(f"start time seconds:(punch in) {start_time}")
    print(f"start time seconds:(actual punch {actual_start_time})")
    start_time = (start_time % 3600)//60
    actual_start_time = actual_start_time // 60
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
def shift_end_remark(end_time,actual_end_time):

    pass
def special_notes(message_code,special_note_string):
    if special_note_string == "Late":# remark if the employee has already informed about being late.
        pass
    elif special_note_string == "Early":# remark if manager wants employee to start early.
        pass
    elif special_note_string == "Help":# remark for helper shifts
        pass
    elif special_note_string == "Issue":# remark for any issues
        pass
    elif special_note_string == "Special":# any special remarks
        pass

"""
a = input_time_converter.Format_time.convert_to_timedelta()
b = input_time_converter.Format_time.convert_to_timedelta()
print(a.seconds)
print(b.seconds)
initial_remark(a.seconds,b.seconds)
"""