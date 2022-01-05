# LogFileParserDemoCode
This is a DemoCode for parsing through large log files and triggering an email whenever there's an error.

There are a total of five scripts in place: (The 6th one temp_config.py is just for declaring the filepath variables)

Scheduler.py -> This is to schedule the Driver_code.py script in the given time interval for every 5 mins.

Filehandling.py -> This selects the required logfile/backup file and returns it in a tuple. Triggered by Scheduler.py

Driver_code.py - > This is the main driver script which controls where the logfile is read at and also triggers an email. Triggered by Scheduler.py script

Logfileparser.py -> Here i wrote a function which uses regex to match the error string and parse through the file. Triggered by Driver_code.py

Email_trigger.py - > Contains the function where the total error count for each run of the script is mailed to a user. Triggered by Driver_code.py

temp_config.py --> A temporary config file with variables of file paths

DemoLogFileParserCode.mkv --> Audio/screen recording to help explain the scripts and show how it works when tested with sample code.
