import datetime
import time
from Driver_code import driver_function

now = datetime.datetime.now()
parse_index = 0

initial_time_string = "01:20:33"
initial_datetime = datetime.datetime.strptime(initial_time_string, "%H:%M:%S")

initial_datetime = now.replace(hour = 8, minute=0, second=0, microsecond=0)
final_datetime = now.replace(hour=18, minute=0, second=0, microsecond=0)

while(now > initial_datetime and now < final_datetime):
    driver_function(parse_index, now)
    time.sleep(300)