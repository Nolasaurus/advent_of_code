import re
import numpy as np

def main():
    with open('day3.txt') as file:
        data = file.read()
        # print(data[:100])

    # like mul(X,Y), where X and Y are each 1-3 digit numbers
    matches = filter_down(data)

    total = 0
    do = True
    for match in matches:
        if match == "don't()":
            do = False
            continue
        if match == "do()":
            do = True
            continue

        if do:
            left, right = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', match).groups()
            total += int(left) * int(right)

    print(total)


def filter_down(data):
    # delete anything between "don't()" and "do()"
    # [don't, do)
    # Regex pattern to match desired items
    pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"

    # Find all matches
    matches = re.findall(pattern, data)

    return matches

if __name__ == '__main__':
    main()