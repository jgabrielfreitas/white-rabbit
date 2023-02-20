import logging
import time
from white_rabbit.stopwatch import stopwatch

logging.basicConfig(level=logging.INFO)


@stopwatch(logger=logging)
def my_function():
    time.sleep(1)
    print("My function was executed.")


my_function()
