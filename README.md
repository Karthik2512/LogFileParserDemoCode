# LogFileParserDemoCode
This is a DemoCode for parsing through large log files and triggering an email whenever there's an error.
#Work In Progress

Currently there are four scripts in place:

Logfileparser.py -> Here i wrote a function which uses regex to match the error tring and parse through the file. Triggered by Driver_code.py

Email_trigger.py - > Contains the function where the total error count for each run of the script is mailed to a user. Triggered by Driver_code.py

Driver_code.py - > This is the main driver script which controls where the logfile is read at and also triggers an email. Triggered by Scheduler.py script

Scheduler.py -> This is to schedule the Driver_code.py script in the given time interval for every 5 mins.

Also i need to write a couple of more functionalities which i'm working on.
