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

def has_invalid_values(ticket, possible_values):
    invalid_values = []
    values = [int(val) for val in ticket.split(',')]
    for val in values:
        if val not in possible_values:
            return True
    return False

all_possible_values = get_all_possible_values(rules)

# part 2
valid_tickets = [ticket for ticket in tickets if not has_invalid_values(ticket, all_possible_values)]

cleaned_tickets = [[int(v) for v in t.split(',')] for t in valid_tickets]

num_rules = len(rules)

def parsed_rules(rules):
    output = {}
    for rule in rules:
        p = re.compile('(\D+): (\d+)\-(\d+) or (\d+)\-(\d+)')
        m = p.findall(rule)
        rule_name, min_1, max_1, min_2, max_2 = m[0]
        output[rule_name] = [
            {'min': int(min_1), 'max': int(max_1)},
            {'min': int(min_2), 'max': int(max_2)},
        ]
    return output

PARSED_RULES = parsed_rules(rules)
rule_names = PARSED_RULES.keys()
# find all the impossible rules per index by going through each ticket and
# deleting when an impossible condition is met
possible_configs = {i: set(rule_names) for i in range(num_rules)}
for ticket in cleaned_tickets:
    print(ticket)
    for idx in range(num_rules):
        value = ticket[idx]
        for rule_name in rule_names:
            # if rule is impossible, ignore
            if rule_name not in possible_configs[idx]:
                continue
            # check if rule is possible at this position
            [rule1, rule2] = PARSED_RULES[rule_name]
            if not (
                (value >= rule1['min'] and value <= rule1['max']) or
                (value >= rule2['min'] and value <= rule2['max'])
            ):
                print(f'removing {rule_name} from {idx}')
                possible_configs[idx].remove(rule_name)

print(possible_configs)

# find a combo that fits all the remaining possible_configs
# try option, if it leads to an impossible situation, can remove it
