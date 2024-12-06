import re
import numpy as np

def main():
    with open('day5.txt') as file:
        data = file.read().splitlines()
        page_ordering_rules = [(x.split('|')) for x in data if '|' in x]
        update_page_numbers = [(x.split(',')) for x in data if '|' not in x]
        
        rules_dict = {}
        for pair in page_ordering_rules:
            if pair[0] in rules_dict.keys():
                rules_dict[pair[0]].append(pair[1])
            else:
                rules_dict[pair[0]] = [pair[1]]


        

if __name__ == '__main__':
    main()