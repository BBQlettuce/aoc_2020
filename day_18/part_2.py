import re

with open("./input.txt") as f:
    rows = f.read().strip().split('\n')

# all single digit numbers lol
# only + and *
    
# evaluate something wrapped
# this takes something non-nested
def parse_group(exp_string):
    # remove start/end parens
    exp_string = exp_string.replace('(','').replace(')','')
    
    # split on * first
    items_to_mult = exp_string.split(' * ')
    running_total = 1
    
    for item in items_to_mult:
        summed = sum_group(item)
        running_total *= summed
    
    return str(running_total)

# evaluates something with only +s
def sum_group(exp_string):
    items_to_add = exp_string.split(' + ')
    return sum([int(i) for i in items_to_add])


def parse_whole_exp(exp_string):
    p = re.compile("\([^\(\)]+\)")
    groups = p.findall(exp_string)
    if not groups:
        return parse_group(exp_string)
    # evaluate groups, then string replace, then go through again
    for group in groups:
        parsed_group = parse_group(group)
        exp_string = exp_string.replace(group, parsed_group)
    return parse_whole_exp(exp_string)


# solve all
print(sum([int(parse_whole_exp(row)) for row in rows]))