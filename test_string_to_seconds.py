from string_to_seconds import all_to_seconds, check_data_format

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
