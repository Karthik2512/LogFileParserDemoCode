'''
This script is the main script which  schedules the current framework to run between 8:00 and 18:00 hours during a day
coinciding with the application's runtime and log generation.
Also, it ensures that the script runs every 5 minutes

Developer - Krishna Karthik (KrishnaKarthik2512@gmail.com)
'''
import datetime
import time
from Driver_code import *
from Filehandling import *
now = datetime.datetime.now()
parse_index = 0                 #This variable defines the point at which the log is read - Initially initialised at 0

initial_datetime = now.replace(hour = 8, minute=0, second=0, microsecond=0)
final_datetime = now.replace(hour=18, minute=0, second=0, microsecond=0)

while(now > initial_datetime and now < final_datetime):
    filenames = return_filename(parse_index,now)        #Calling the return filename function from the Filehandling script
    parse_index = driver_function(filenames,parse_index,now)           #Calling the driver function which handles the log parsing and email triggers
    time.sleep(300)
    now = datetime.datetime.now()             #Updating the now variable again with the datetime value post the 5 min wait period