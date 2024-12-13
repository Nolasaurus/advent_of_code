import pytest
from day6 import get_avatar_line, get_avatar_char_num, get_avatar_direction, get_avatar_row_num, get_line_by_num, look_ahead_is_empty



grid = '...', '.V.', '...'
def test_get_avatar_line():
    assert get_avatar_line(grid) == '.V.'
    grid_2 = '.....', '.....', '.....', '...V.', '.....'
    assert get_avatar_line(grid_2) == '...V.'

def test_get_avatar_char_num():
    grid_1 = '...', '.V.', '...'
    line = get_avatar_line(grid_1)
    assert get_avatar_char_num(line) == 1

    line_2 = '....V...........'
    assert get_avatar_char_num(line_2) == 4


def test_get_avatar_direction():
    line_0 = '....V...........'
    assert get_avatar_direction(line_0) == 'V'
    line_1 = '....^...........'
    assert get_avatar_direction(line_1) == '^'
    line_2 = '....<...........'
    assert get_avatar_direction(line_2) == '<'
    line_3 = '....>...........'
    assert get_avatar_direction(line_3) == '>'

def test_get_avatar_row_num():
    grid = '.....', '.test.', '.....', '...V.', '.....'
    assert get_avatar_row_num(grid) == 3

def test_get_line_by_num():
    n = 1
    grid = '.....', '.test.', '.....', '...V.', '.....'
    assert get_line_by_num(n, grid) == '.test.'

def test_look_ahead_is_empty():
    # OPEN
    grid = '....<...........', '................'
    assert look_ahead_is_empty(grid) == True
    grid_2 = '....>...........', '................'
    assert look_ahead_is_empty(grid_2) == True
    grid_3 = '...............', '.........^.......'
    assert look_ahead_is_empty(grid_3) == True
    grid_4 = '....V...........', '................'
    assert look_ahead_is_empty(grid_4) == True

    # BLOCKED 
    grid = '...#<...........', '................'
    assert look_ahead_is_empty(grid) == False
    grid_2 = '....>#..........', '................'
    assert look_ahead_is_empty(grid_2) == False
    grid_3 = '.........#.......', '.........^.......'
    assert look_ahead_is_empty(grid_3) == False
    grid_4 = '....V...........', '....#...........'
    assert look_ahead_is_empty(grid_4) == False