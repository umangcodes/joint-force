import datetime
import time

current_time = datetime.datetime.now()

print(current_time + datetime.timedelta(hours=2,minutes=30))
print(current_time)
current_time = current_time.strftime("%H:%M:%S")

print(current_time)
current_time = time.strptime(current_time, "%H:%M:%S")
#datetime.timedelta(current_time)
print(current_time)



