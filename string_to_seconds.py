import re


def check_data_format(time_str: str) -> None:
    pattern = r"^\d{2}:\d{2}:\d{2}$"
    if not re.match(pattern, time_str):
        raise ValueError(
            "Given string does not match the required format (HH:MM:SS)"
        )

    hh, mm, ss = map(int, time_str.split(":"))

    if hh not in range(0, 24):
        raise ValueError("Hours must be between 0 and 23")

    if mm not in range(0, 60):
        raise ValueError("Minutes must be between 0 and 59")

    if ss not in range(0, 60):
        raise ValueError("Seconds must be between 0 and 59")


def all_to_seconds(time_str: str) -> int:
    check_data_format(time_str)
    hh, mm, ss = map(int, time_str.split(":"))
    result = hh * 3600 + mm * 60 + ss
    return result
