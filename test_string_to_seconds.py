from string_to_seconds import all_to_seconds, check_data_format

import pytest


@pytest.mark.parametrize(
    "value, expected",
    [
        ("01:00:01", 3601),
        ("00:01:00", 60),
        ("10:00:00", 36000),
        ("00:00:00", 0),
        ("23:59:59", 86399),
    ],
)
def test_valid_input(value, expected):
    assert all_to_seconds(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        "",
        "second",
        "hours:00:00",
        "00:minutes:00",
        "00:00:seconds",
        "25:01:01",
        "01:61:01",
        "01:01:61",
        "01:01:01:01",
        "01:01:01  Second",
        "01 :01 :01 :01",
        "01:01:01:::::",
    ],
)
def test_invalid_strings_raise_value_error(value):
    with pytest.raises(ValueError):
        check_data_format(value)


@pytest.mark.parametrize(
    "value",
    [
        "24:60:60",
        "23:59:60",
        "23:60:59",
        "23:60:-1",
    ],
)
def test_all_to_seconds_raises_value_error(value):
    with pytest.raises(ValueError):
        all_to_seconds(value)
