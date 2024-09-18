import re


def check_data_format(time_str):
    pattern = r"^\d{2}:\d{2}:\d{2}$"
    if not re.match(pattern, time_str):
        return False

    hh, mm, ss = map(int, time_str.split(":"))

    if hh in range(0, 24) and mm in range(0, 60) and ss in range(0, 60):
        return time_str

    return False


def all_to_seconds(time_str):
    if not check_data_format(time_str):
        return False
    else:
        hh, mm, ss = map(int, time_str.split(":"))
        result = hh * 3600 + mm * 60 + ss
        return result
