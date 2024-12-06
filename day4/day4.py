import re
import numpy as np

def main():
    with open('day4.txt') as file:
        data = file.read().splitlines()
        data = [list(line) for line in data]

        text_array = np.array(data)
        total = 0
        for line in text_array:
            new_line = ''.join(line)
            # pass
            # print(line)
            # print(check_horizontal(new_line))
            total += check_line(new_line)
        print(total)
        for line in text_array.transpose():
            new_line = ''.join(line)
            # pass
            # print(line)
            total += check_line(new_line)

    print(total)
    total += check_diagonal(text_array)
    print(total)
    print(check_X(text_array))

def check_line(line):
    forward = len(re.findall('XMAS', line))
    backward = len(re.findall('SAMX', line))
    return forward + backward


def check_diagonal(grid):
    width, height = grid.shape
    total = 0
    for i in range(width-3):
        for j in range(height-3):
            offsets = [(0, 0), (1, 1), (2, 2), (3, 3)]
            offsets_2 = [(0, 3), (1, 2), (2, 1), (3, 0)]
            

            coords = [(coord[0]+i, coord[1]+j) for coord in offsets]
            coords_2 = [(coord[0]+i, coord[1]+j) for coord in offsets_2]

            forward_slash = ''.join([grid[coord[1]][coord[0]] for coord in coords])
            backward_slash = ''.join([grid[coord[1]][coord[0]] for coord in coords_2])

            total += check_line(forward_slash) + check_line(backward_slash)

    return total
def check_X(grid):
    width, height = grid.shape
    total = 0
    for i in range(width-2):
        for j in range(height-2):
            MAS_offsets_1 = [(0, 0), (1, 1), (2, 2)]
            MAS_offsets_2 = [(2, 0), (1, 1), (0, 2),]
            MAS_coords_1 = [(coord[0]+i, coord[1]+j) for coord in MAS_offsets_1]
            MAS_coords_2 = [(coord[0]+i, coord[1]+j) for coord in MAS_offsets_2]

            forward_slash = ''.join([grid[coord[1]][coord[0]] for coord in MAS_coords_1])
            backward_slash = ''.join([grid[coord[1]][coord[0]] for coord in MAS_coords_2])

            if forward_slash in ['MAS', 'SAM']:
                if backward_slash in ['MAS', 'SAM']:
                    total += 1

    return total 

if __name__ == '__main__':
    main()