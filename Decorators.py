import functools
import time
import pickle


def debug(func):
    """Ausgabe der Signatur und des Rückgabewertes der Funktion"""

    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


def log(humanReadable=False, kiReadable=False):
    if humanReadable == True:
        def decorator_human_writeToFile(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                value = func(*args, **kwargs)
                outfile = open("humanLogFile", 'wb')
                pickle.dump(value, outfile)
                outfile.close()

    if kiReadable == True:
        def decorator_ki_writeToFile(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                value = func(*args, **kwargs)
                outfile = open("kiLogFile", 'wb')
                pickle.dump(value, outfile)
                outfile.close()


def timer(func):
    """Ausgabe der Laufzeit einer Funktion"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # Startzeit
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # Endzeit
        run_time = end_time - start_time    # Gesamte Laufzeit
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

