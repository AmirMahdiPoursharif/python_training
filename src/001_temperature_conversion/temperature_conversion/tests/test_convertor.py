import pytest

from ..convertor import to_celsius, to_fahrenheit


@pytest.mark.parametrize(
    ("fahrenheit", "expected"),
    [
        (32, 0),
        (212, 100),
        (77, 25),
        (-40, -40),
        (98.6, 37),
    ],
)
def test_to_celsius(fahrenheit, expected):
    assert to_celsius(fahrenheit) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("celsius", "expected"),
    [
        (0, 32),
        (100, 212),
        (25, 77),
        (-40, -40),
        (37, 98.6),
    ],
)
def test_to_fahrenheit(celsius, expected):
    assert to_fahrenheit(celsius) == pytest.approx(expected)