from datetime import datetime
import os


def dt_now():
    return datetime.now().strftime('%Y/%m/%d %H:%M:%S')


def error(error_message):
    message = str("[" + dt_now() + "] [ERROR]   " + error_message)
    print(message)
    log_message(message)


def notice(notice_message):
    message = str("[" + dt_now() + "] [NOTICE]  " + notice_message)
    print(message)
    log_message(message)


def warning(warning_message):
    message = str("[" + dt_now() + "] [WARNING] " + warning_message)
    print(message)
    log_message(message)


def debug(debug_message):
    message = str("[" + dt_now() + "] [DEBUG]   " + debug_message)
    print(message)
    log_message(message)


def initalise(module_name):
    message = str("[" + dt_now() + "] [INIT]    " + module_name)
    print(message)
    log_message(message)


def log_message(message):
    with open("FateGameLog.txt", "a") as log_file:
        message = str(message + "\n")
        log_file.write(message)


os.remove("FateGameLog.txt")
initalise(__file__)
