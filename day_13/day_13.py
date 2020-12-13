with open('./input.txt') as f:
    lines = f.readlines()
    start_time = int(lines[0].strip())
    schedule = lines[1].strip().split(',')
    bus_ids = [int(id) for id in schedule if id != 'x']

def wait_time(start_time, id):
    return id - (start_time % id)

wait_times = [wait_time(start_time, id) for id in bus_ids]

# part 2
indexes = [schedule.index(str(id)) for id in bus_ids]
offset_rules = list(zip(bus_ids, indexes))

# algorithm
# start with 2 rules
# find smallest X that satisfies 2 rules
# X is new starting point
# product of 2 nums is new increment
# then add rule
# find next X that satisfies 3 rules
# set new X, set new increment
def find_smallest_t(rules):
    current, _ = rules[0]
    increment, _ = rules[0]
    answer = None
    current_active_rule = 1 # index of currently tested rule
    while current_active_rule < len(rules):
        divisor, offset = rules[current_active_rule]
        if (current + offset) % divisor != 0:
            current += increment
        else:
            increment *= divisor
            print(f'new current: {current}')
            print(f'new increment: {increment}')
            current_active_rule += 1
    print(current)
    return current
