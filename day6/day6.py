import re
import numpy as np

def main():
    with open('day6.txt') as file:
        grid = file.read().splitlines()
        
    test_grid = '....', '.V..', '....'
    print(count_positions(test_grid))
    # print(count_positions(grid))
    test_grid_2 = ['....#.....',
                    '.........#',
                    '..........',
                    '..#.......',
                    '.......#..',
                    '..........',
                    '.#..^.....',
                    '........#.',
                    '#.........',
                    '......#...']
    
    for i in range(75):
        if i == 0:
            grid = step_forward(test_grid_2)
        else:
            grid = step_forward(grid)
        print(i)        
        print_grid(grid)

def print_grid(grid):
    for line in grid:
        print(line)

def print_visited_locations_on_grid(grid, locations_list):
    grid = list(grid)
    for location in locations_list:
        char_num, row_num = location
        line = grid[row_num]
        grid[row_num] = line[:char_num] + 'X' + line[char_num+1:]
    
    print_grid(grid)


def count_positions(grid):
    # TODO stop counting when "guard" would leave the grid
    visited_locations = []
    visited_coords = set()
    all_sites_visited = False
    new_grid = list(grid)
    print('starting while loop')
    while not all_sites_visited:
        new_grid = step_forward(new_grid)
        new_position = get_avatar_position(new_grid)
        if new_position in visited_locations:
            all_sites_visited = True            
            print_visited_locations_on_grid(grid, visited_coords)
            return len(visited_coords)+1

        else:
            visited_locations.append(new_position)
            visited_coords.add(new_position[1:])

def step_forward(grid):
    if look_ahead_is_empty(grid):
        return move_avatar(grid)

    else:
        return rotate_avatar(grid)
    
def move_avatar(grid):
    grid = list(grid)
    for row_number, line in enumerate(grid):
        for direction in ['<', '>', 'V', '^']:
            if direction in line:
                char_num = get_avatar_char_num(line)
                                
                if direction == '>':
                    new_line = line[:char_num] + '.>' + line[char_num+2:]
                    grid[row_number] = new_line
                    return grid
                if direction == '<':
                    new_line = line[:char_num-1] + '<.' + line[char_num+1:]
                    grid[row_number] = new_line
                    return grid
                if direction == '^':
                    line_above = grid[row_number-1]
                    new_line_above = line_above[:char_num] + '^' + line_above[char_num+1:]
                    new_line = line[:char_num] + '.' + line[char_num+1:]
                    grid[row_number] = new_line
                    grid[row_number-1] = new_line_above
                    return grid
                if direction == 'V':
                    line_below = grid[row_number+1]
                    
                    new_line = line[:char_num] + '.' + line[char_num+1:]
                    new_line_below = line_below[:char_num] + 'V' + line_below[char_num+1:]

                    grid[row_number] = new_line
                    grid[row_number+1] = new_line_below
                    return grid


def rotate_avatar(grid):
    grid = list(grid)
    dir_dict = {'>':'V', 'V':'<', '<':'^', '^':'>'}

    for row_num, line in enumerate(grid):
        for direction in dir_dict.keys():
            if direction in line:
                new_direction = dir_dict[direction]
                grid[row_num] = line.replace(direction, new_direction)
                return grid

def get_avatar_position(grid):
    row_num = get_avatar_row_num(grid)
    line = grid[row_num]
    dir = get_avatar_direction(line)
    char_num = get_avatar_char_num(line)
    
    return  dir, char_num, row_num

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

    if avatar_dir == '<':
        if avatar_char_num == 0:
            return False
        return avatar_line[avatar_char_num-1] == '.'

    if avatar_dir == '>':

        if avatar_char_num == (len(avatar_line)-1):
            return False

        return avatar_line[avatar_char_num+1] == '.'
    
    if avatar_dir == '^':
        if avatar_row_num == 0:
            return False
        # get line, line before
        prev_row_num = avatar_row_num - 1
        previous_line = get_line_by_num(prev_row_num, grid)
        spot_ahead = previous_line[avatar_char_num]
        return spot_ahead == '.'

    if avatar_dir == 'V':
        if avatar_row_num == len(grid)-1:
            return False
        # get line, line after
        next_row_num = avatar_row_num + 1
        next_line = get_line_by_num(next_row_num, grid)
        spot_ahead = next_line[avatar_char_num]
        return spot_ahead == '.'

    raise ValueError('direction not valid')

if __name__ == '__main__':
    main()