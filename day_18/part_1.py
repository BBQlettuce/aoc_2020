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
    running_total = None
    current_op = None
    items = exp_string.split(' ')
    for item in items:
        if item == '+' or item == '*':
            current_op = item
            continue
        num = int(item)
        if not running_total:
            running_total = num
            continue
        if current_op == '+':
            running_total += num
        if current_op == '*':
            running_total *= num
    return str(running_total)

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