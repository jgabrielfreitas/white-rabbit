from time import time


def stopwatch(logger=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            if logger is not None:
                logger.info(f"Running {func.__name__}...")
            else:
                print(f"Running {func.__name__}...")
            result = func(*args, **kwargs)
            end_time = time()
            if logger is not None:
                logger.info(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
            else:
                print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
            return result

        return wrapper

    return decorator
