import re
import numpy as np

def main():
    with open('day5.txt') as file:
        data = file.read().splitlines()
        page_ordering_rules = [(x.split('|')) for x in data if '|' in x]
        update_page_numbers = [(x.split(',')) for x in data if '|' not in x]
        update_page_numbers = [x for x in update_page_numbers if x != ['']]
        
        rules_dict = {}
        for pair in page_ordering_rules:
            # key must always be before value(s) in updates
            if pair[0] in rules_dict.keys():
                rules_dict[pair[0]].append(pair[1])
            else:
                rules_dict[pair[0]] = [pair[1]]

        valid_updates = []
        for update in update_page_numbers:
            if validate_update(update, rules_dict):
                valid_updates.append(update)

        # test_update = ['64', '44', '17', '25', '44', '28', '98', '47']
        # print(validate_update(test_update, rules_dict))
        # print(len(valid_updates))
        total = 0
        for update in valid_updates:
            total += get_middle_page(update)
        
        print(total)


def validate_update(update, rules_dict):
    for i, num in enumerate(update):
        if update:
            # if earlier pages break rules dict
            # i.e. if values (aka "follower" pages) precede key ("num")
            pages_before_num = update[:i]
            must_be_follower_pages = rules_dict.get(num, [])

            for page in pages_before_num:
                if page in must_be_follower_pages:
                    return False
    return True

def get_middle_page(update):
    if len(update) > 0:
        num_pages = len(update)
        middle = int(num_pages//2)
        return int(update[middle])
    else:
        return 0

if __name__ == '__main__':
    main()