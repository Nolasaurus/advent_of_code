import re
import numpy as np

def main():
    with open('day2.txt') as file:
        data = file.readlines()
        data = [x.strip('\n') for x in data]

        safe_reports = 0
        dampened_reports = 0
        for level in data:
            if sliding_window(level):
                safe_reports += 1
            elif dampener_sliding_window(level):
                dampened_reports += 1

        print('Number of safe reports:', safe_reports)
        print('Number of safe reports with damping:', safe_reports+dampened_reports)
        # level = '47 46 43 41 40 38 36 33'
        # level = '1 3 2 4 5'
        # level = '9 7 6 2 1'

        # print(sliding_window(level))
        # print('should be false', dampener_sliding_window(level))


    # 7 6 4 2 1: Safe without removing any level.
    # 1 2 7 8 9: Unsafe regardless of which level is removed.
    # 9 7 6 2 1: Unsafe regardless of which level is removed.
    # 1 3 2 4 5: Safe by removing the second level, 3.
    # 8 6 4 4 1: Safe by removing the third level, 4.
    # 1 3 6 7 9: Safe without removing any level.

def dampener_sliding_window(level):
    # list of all combinations of skipping one # in a level
    possibilities = generate_possible_dampened(level)
    for candidate in possibilities:
        if sliding_window(candidate):
            return True
    return False

def generate_possible_dampened(level):
    level = level.split(' ')
    candidates = []
    for i in range(len(level)):
        if i == 0:
            new_level = level[1:]
        elif i == range(len(level)):
            new_level = level[:-1]
        else:
            before = level[:i]
            after = level[i+1:]
            new_level = before + after
        candidates.append(' '.join(new_level))
    return candidates

        
def sliding_window(level):
    if len(level) < 3:
        return False

    level = level.split()
    level = [int(x) for x in level]

    for i in range(1, len(level)-1):
        # slide along level, 3 numbers at a time
        # aka kernel = 3
        window = level[i-1:i+2]
        
        if are_equal(*window):
            return False
        
        if exceeds_max_diff(*window):
            return False
        
        if not is_increasing_or_decreasing(*window):
            return False

    return True

def are_equal(prev_num, curr_num, next_num):
    return (prev_num == curr_num) or (curr_num == next_num)

def is_increasing_or_decreasing(prev_num, curr_num, next_num):
    increasing_0_to_1 = prev_num < curr_num
    increasing_1_to_2 = curr_num < next_num
    is_increasing = increasing_0_to_1 and increasing_1_to_2
    is_decreasing = not increasing_0_to_1 and not increasing_1_to_2
    return is_increasing or is_decreasing

def exceeds_max_diff(prev_num, curr_num, next_num):
    prev_not_within_3 = np.abs(prev_num-curr_num) > 3
    next_not_within_3 = np.abs(next_num-curr_num) > 3
    return prev_not_within_3 or next_not_within_3

if __name__ == '__main__':
    main()