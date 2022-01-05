'''
In this module, the filename to be parsed through is selected. Initially if there are any appends made to the logfile, the
code returns a tuple defined as 'filenames' containing the logfile path. However if the log file is copied into a backup
and is restarted again, then it returns a tuple 'filenames' with two values - logfile, backup_log.
'''


import os
from temp_config import *               #Here, importing the path values for the log files
from emailtrigger import *
def return_filename(parse_index,datetime_const):
    if parse_index < os.path.getsize(log_file):
        filenames=(log_file,)
    elif parse_index  > os.path.getsize(log_file):
        filenames=(backup_log,log_file)
    elif parse_index == os.path.getsize(log_file):
        error_mail = 'The application has no data to append to the logfile at the time ' + str(datetime_const)
        #send_email(error_mail)   ------->   Triggering this email as to notify the team if there were no writes done to the logfile.
    return filenames

