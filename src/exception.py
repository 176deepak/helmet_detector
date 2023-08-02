'''

file:- exception.py

This file handles all exceptions which is occured during program execution and tell us exception in a single line "Error occured in python script name [{0}], line number [{1}], error  message [{2}]"

'''

#required modules
import sys
from src.logger import logging


# function for error details, gives us error message in a single line
# returns a message string
def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    meassage = 'Error occured in python script name [{0}], line number [{1}], error  message [{2}]'.format(file_name, exc_tb.tb_lineno, str(error))

    return meassage


# CustomException class which inherits from Exception class for handling CustomExceptions
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error = error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message