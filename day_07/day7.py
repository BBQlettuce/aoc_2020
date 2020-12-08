with open("./day7.txt") as f:
    rules = f.read().strip().split("\n")

# final structure
# {
#     color: {
#         color: count,
#         color: count
#     }, etc
# }


rules_map = {}
for rule in rules:
    parent_pattern = re.compile("^(.+) bags contain")
    parent_match = parent_pattern.match(rule)
    parent = parent_match.group(1)
    rules_map[parent] = {}

    children_pattern = re.compile("(\d) (\D+) bag")
    children_matches = children_pattern.findall(rule)
    for cm in children_matches:
        [count, color] = cm
        parent_rules = rules_map[parent]
        parent_rules[color] = int(count)
        rules_map[parent] = parent_rules


def possible_children(color):
    children = rules_map[color]
    if not children:
        return set()
    else:
        children_keys = list(children.keys())
        children_set = set(children_keys)
        subchildren_sets = [possible_children(c) for c in children_set]
        return children_set.union(*subchildren_sets)

def possible_parents(color):
    pps = set()
    for parent_color in rules_map:
        if color in possible_children(parent_color):
            pps.add(parent_color)
    return pps

def num_sub_bags(color):
    children = rules_map[color]
    if not children:
        return 0
    else:
        return sum([children[child] * num_sub_bags(child) + children[child] for child in children])
