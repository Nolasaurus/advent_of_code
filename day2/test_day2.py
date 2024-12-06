import pytest
from day2 import are_equal, is_increasing_or_decreasing, exceeds_max_diff, sliding_window, dampener_sliding_window, generate_possible_dampened
def test_are_equal():
    assert are_equal(13, 13, 14)

def test_increasing():
    assert is_increasing_or_decreasing(13, 14, 15)
    assert is_increasing_or_decreasing(34, 37, 39)
    assert not is_increasing_or_decreasing(14, 15, 11)

def test_decreasing():
    assert is_increasing_or_decreasing(18, 16, 15)
    assert not is_increasing_or_decreasing(14, 15, 11)

def test_max_diff():
    assert exceeds_max_diff(13, 17, 16)
    assert not exceeds_max_diff(13, 12, 11)

def test_generate_possible_dampened():
    input = '46 44 41 44 48'
    output = ['44 41 44 48',
              '46 41 44 48',
              '46 44 44 48',
              '46 44 41 48',
              '46 44 41 44'
              ]
    assert generate_possible_dampened(input) == output

def test_sliding_window():
    assert sliding_window('12 13')
    assert not sliding_window('12 19 21')
    assert not sliding_window('33 34 34 37 39 40 43 43')
    assert sliding_window('35 37 39')
    assert sliding_window('34 37 39')
    assert sliding_window('7 6 4 2 1')
    assert sliding_window('1 3 6 7 9')
    assert not sliding_window('1 2 7 8 9')
    assert not sliding_window('32 29 27 26 24 23 25')


def test_dampener_sliding_window():
    assert dampener_sliding_window('1 3 2 4 5')
    assert dampener_sliding_window('8 6 4 4 1')
    assert dampener_sliding_window('9 6 4 4 1')
    assert dampener_sliding_window('31 29 27 26 24 23 25')
    assert not dampener_sliding_window('33 29 27 26 24 23 25')
    assert not dampener_sliding_window('9 7 6 2 1')
    assert not dampener_sliding_window('1 2 7 8 9')
    assert not dampener_sliding_window('1 2 2 7 8 9')
