import re

with open('./input.txt') as f:
    [rules, messages] = f.read().strip().split('\n\n')
    rules = rules.split('\n')
    messages = messages.split('\n')

RULES_MAP = {}
for rule in rules:
    [rule_name, codes] = rule.split(': ')
    RULES_MAP[rule_name] = codes

def format_code(code):
    groups = code.split(' | ')
    if len(groups) > 1:
        return ' | '.join([f'({group})' for group in groups])
    return code

for rule in RULES_MAP:
    formatted = format_code(RULES_MAP[rule])
    RULES_MAP[rule] = formatted

# loop through rules, solving more each time

def is_solved(code):
    p = re.compile("\d+")
    m = p.findall(code)
    return len(m) == 0

def rule_found_in_code(rule_name, code):
    p = re.compile(f"(^{rule_name}\Z)|(^{rule_name}\s)|(\s{rule_name}\Z)|(\s{rule_name}\s)")
    m = p.findall(code)
    return len(m) > 0

def solve_rules(rules_map):
    rule_names = list(rules_map.keys())
    num_rules = len(rule_names)
    num_solved_rules = 0
    current_solved_rules = []
    # get first set of already solved
    for rule_name in rules_map:
        if is_solved(rules_map[rule_name]):
            current_solved_rules.append(rule_name)

    # keep going until all solved
    while num_solved_rules < num_rules:
        new_solved_rules = []
        for rule_name in rules_map:
            for solved_rule in current_solved_rules:
                code = rules_map[rule_name]
                if rule_found_in_code(rule_name, code):
                    new_code = code.replace(solved_rule, rules_map[solved_rule]) # this isnt replacing the right part
                    rules_map[rule_name] = new_code
                if is_solved(rules_map[rule_name]):
                    new_solved_rules.append(rule_name)
        current_solved_rules = new_solved_rules

    return rules_map