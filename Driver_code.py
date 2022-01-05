from logfileparser import *
from emailtrigger import *
def driver_function(parse_index, datetime_const):
    (parse_index,error_count) = func_finding_error('F:\Work\Testfiles\sample_error.txt',parse_index)
    error_msg = "There have been " + str(error_count) + " errors when the script was run at " + str(datetime_const)
    print(error_msg)
    #if error_count > 0:
        #send_email(error_msg)
