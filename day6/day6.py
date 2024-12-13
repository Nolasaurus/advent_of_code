import re
import numpy as np

def main():
    with open('day6.txt') as file:
        data = file.read().splitlines()
        data_dict = {}
        for i, line in enumerate(data):
            data_dict[i] = line

        # for i in range(5):
        #     data_dict = step_forward(data_dict)


# def step_forward(grid_dict):
#     row_number, col_number, direction = get_avatar_position(grid_dict)
#     if look_ahead_is_empty
#     new_line = move_forward(row_number, col_number, direction)

#     # grid[row_number] updated to new line
#     grid_dict[row_number] = new_line

#     return grid_dict

#     for dir in ['<', '>', 'V', '^']:

    

# def get_avatar_position(grid):
#     row_number, line = get_avatar_line(grid)
#     direction = get_avatar_direction(line)
#     column_number = get_avatar_column(line)
#     return row_number, column_number, direction

def get_avatar_line(grid):
    for line in grid:
        for dir in ['<', '>', 'V', '^']:
            if dir in line:
                return line
    raise ValueError('direction not found')

def get_avatar_char_num(line):
    for i, char in enumerate(line):
        if char in ['<', '>', 'V', '^']:
            return i

def get_avatar_direction(line):
    for char in line:
        if char in ['<', '>', 'V', '^']:
            return char
    raise ValueError('direction not in line')

def get_avatar_row_num(grid):
    count = 0
    for line in grid:
        for dir in ['<', '>', 'V', '^']:
            if dir in line:
                return count
        count += 1

def get_line_by_num(n, grid):
    return grid[n]

def look_ahead_is_empty(grid):
    avatar_row_num = get_avatar_row_num(grid)
    avatar_line = get_line_by_num(avatar_row_num, grid)
    avatar_dir = get_avatar_direction(avatar_line)
    avatar_char_num = get_avatar_char_num(avatar_line)
    print(avatar_row_num)
    print(avatar_dir)
    print(avatar_char_num)
    print('line', avatar_line)

    if avatar_dir == '<':
        if avatar_char_num == 0:
            return False
        return avatar_line[avatar_char_num-1] == '.'

    if avatar_dir == '>':
        print('dir >')

        if avatar_char_num == (len(avatar_line)-1):
            return False

        return avatar_line[avatar_char_num+1] == '.'
    
    if avatar_dir == '^':
        # get line, line before
        prev_row_num = avatar_row_num - 1
        previous_line = get_line_by_num(prev_row_num, grid)
        spot_ahead = previous_line[avatar_char_num]
        return spot_ahead == '.'

    if avatar_dir == 'V':
        # get line, line after
        next_row_num = avatar_row_num + 1
        next_line = get_line_by_num(next_row_num, grid)
        spot_ahead = next_line[avatar_char_num]
        return spot_ahead == '.'


    # print(row_number, col_number, direction)
    raise ValueError('direction not valid')

if __name__ == '__main__':
    main()