'''
This script brings together logparser and email trigger modules. It acts as a glue - connecting different modules and drives this
mini framework.
'''

from Logfileparser import *
from emailtrigger import *
def driver_function(filenames, parse_index, datetime_const):
    for filename in filenames:
        (parse_index,error_count) = func_finding_error(filename,parse_index)
        if len(filenames) > 1:
            parse_index = 0
        error_msg = "There have been " + str(error_count) + " errors when the script was run at " + str(datetime_const) + " in the file " + str(filename)
        print(error_msg)                #Printing the error message which would be sent as an email to the relevant team
        #if error_count > 0:
            #send_email(error_msg)      #Commenting this part out as this sends out an email
    return parse_index
