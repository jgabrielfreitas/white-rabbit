import time


class StopWatch:
    def __init__(self):
        self.__start_time = time.time()
        self.__stop_time = None

    def stop(self):
        self.__stop_time = time.time()

    def diff(self):
        return self.__stop_time - self.__start_time
