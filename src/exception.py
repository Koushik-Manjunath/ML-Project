import sys
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def error_message_detail(error, error_detail: sys):
    """
    Captures detailed error information, including file name and line number.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script [{0}], line number [{1}], error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Custom Exception class for structured error reporting.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0  # Will trigger ZeroDivisionError
    except Exception as e:
        logging.error(error_message_detail(e, sys))  # Logs error details
        raise CustomException(e, sys)  # Raises custom exception
