import re
from itertools import chain

with open("./input.txt") as f:
    [rules, my_ticket, tickets] = f.read().strip().split('\n\n')
    rules = [rule.strip() for rule in rules.split('\n')]
    my_ticket = my_ticket.split('\n')[1]
    tickets = [ticket.strip() for ticket in tickets.split('\n')[1:]]

def get_all_possible_values(rules):
    ranges = []
    for rule in rules:
        p = re.compile('(\d+)\-(\d+) or (\d+)\-(\d+)')
        m = p.findall(rule)
        min_1, max_1, min_2, max_2 = m[0]
        ranges.append(range(int(min_1), int(max_1) + 1))
        ranges.append(range(int(min_2), int(max_2) + 1))
    merged_ranges = chain(*ranges)
    possible_values = set()
    for num in merged_ranges:
        possible_values.add(num)
    return possible_values

def sum_invalid_values(ticket, possible_values):
    invalid_values = []
    values = [int(val) for val in ticket.split(',')]
    for val in values:
        if val not in possible_values:
            invalid_values.append(val)
    return sum(invalid_values)

all_possible_values = get_all_possible_values(rules)
total_sum = sum([sum_invalid_values(ticket, all_possible_values) for ticket in tickets])
# part 1
print(total_sum)
