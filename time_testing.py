import datetime
import time
"""
current_time = datetime.datetime.now()

print(current_time + datetime.timedelta(hours=2,minutes=30))
print(current_time)
current_time = current_time.strftime("%H:%M:%S")

print(current_time)
current_time = time.strptime(current_time, "%H:%M:%S")
#datetime.timedelta(current_time)
print(current_time)

"""
hour = int(input("Hour: "))
min = int(input("Minute: "))
time_delta_obj = datetime.timedelta(hours=hour,minutes=min)

time_stamp = datetime.datetime.now()


print(f"tme delta: {time_delta_obj}")
print(f"time stamp: {time_stamp}")

time_stamp_hour = time_stamp.hour
time_stamp_min = time_stamp.minute
time_stamp_sec = time_stamp.second

time_delta_obj_hour = time_delta_obj.seconds // 3600
time_delta_obj_min = time_delta_obj.seconds // 60 - (time_delta_obj_hour * 60)

print("Time stamp details")
print(time_stamp_hour)
print(time_stamp_min)
print(time_stamp_sec)

print("\n\n\n\n")

print("Time delta obj details")
print(time_delta_obj_hour)
print(time_delta_obj_min)