import functools
import time
import pickle

log_list = []

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


def log(humanReadable=False, aiReadable=False):
    """
    Logs game data for human player and ai player and writes it to a file
    :param humanReadable: line in file: "Move:[ ... , ... ] Board: ..."
    :param aiReadable: line in file: "[row,column]"
    """
    if humanReadable == True:
        def decorator_human_writeToFile(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                value = func(*args, **kwargs)
                outfile = open("humanLogFile.pkl", 'ab')
                pickle.dump(f"Move:{value} Board:{args[1]}\n", outfile)
                outfile.close()
                return value
            return wrapper
        return decorator_human_writeToFile

    if aiReadable == True:
        def decorator_ki_writeToFile(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                value = func(*args, **kwargs)
                log_list.append(value)
                outfile = open("aiLogFile.pkl", 'wb')
                pickle.dump(log_list, outfile)
                outfile.close()
                return value
            return wrapper
    return decorator_ki_writeToFile


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

