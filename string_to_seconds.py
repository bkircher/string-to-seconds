import re

def check_data_format(time_str):
    pattern = r'^\d{2}:\d{2}:\d{2}$'
    if not re.match(pattern, time_str):
        return False

    hh,mm,ss = map(int, time_str.split(':'))

    if hh in range(0,24) and mm in range(0,60) and ss in range(0,60):
        return time_str

    return False

def all_to_seconds(time_str):
    if not check_data_format(time_str):
        return False
    else:
        hh,mm,ss = map(int, time_str.split(':'))
        result = hh*3600 + mm*60 + ss
        return result


def test_1():
    assert all_to_seconds("01:00:01") == 3601
    assert all_to_seconds("00:01:00") == 60
    assert all_to_seconds("10:00:00") == 36000
    assert all_to_seconds("00:00:00") == 0
    assert all_to_seconds("23:59:59") == 86399

def test_2():
    assert check_data_format("") is False
    assert check_data_format("second") is False
    assert check_data_format("hours:00:00") is False
    assert check_data_format("00:minutes:00") is False
    assert check_data_format("00:00:seconds") is False
    assert check_data_format("25:01:01") is False
    assert check_data_format("01:61:01") is False
    assert check_data_format("01:01:61") is False

def test_3():
    assert check_data_format("01:01:01:01") is False
    assert check_data_format("01:01:01  Second") is False
    assert check_data_format("01 :01 :01 :01") is False
    assert check_data_format("01:01:01:::::") is False
    assert all_to_seconds("24:60:60") is False
    assert all_to_seconds("23:59:60") is False
    assert all_to_seconds("23:60:59") is False
    assert all_to_seconds("23:60:-1") is False
