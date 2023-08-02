'''

file:- logger.py

This file is used for logging all logs or recording all steps execution in a seprate file. 
Here first we create a create a log file at the starting of code execution and this file will now takes record of all logs which is generted during program execution.

'''

# required modules
import os
import logging
from datetime import datetime

# defining new folder for all log files "Project_logs"
LOGS_PATH = os.path.join(os.getcwd(), 'LOGS\Projects_logs')

# checking whether a folder exists or not in project folder if not just create this folder directory
if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH, exist_ok = True)

# log file name and it's path 
log_file_name = f"{datetime.now().strftime('%Y_%m_%d %H_%M_%S')}.log"
log_file_path = os.path.join(LOGS_PATH, log_file_name)

# creating logfile 
with open(log_file_path, 'w') as f:
    pass

# configuring logs format with logging.basicConfig()
logging.basicConfig(
    filename = log_file_path, 
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level = logging.INFO
)