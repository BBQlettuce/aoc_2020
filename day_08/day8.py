with open("./day8.txt") as f:
    steps = f.read().strip().split("\n")


accumulator = 0
current_step = 0
visited_steps = set()

while current_step not in visited_steps:
    print(current_step)
    print(accumulator)
    visited_steps.add(current_step)
    # execute step
    step = steps[current_step]
    [operation, units] = step.split(" ")
    units = int(units)
    if operation == "nop":
        current_step += 1
    if operation == "acc":
        accumulator += units
        current_step += 1
    if operation == "jmp":
        current_step += units


print(accumulator)


# PART 2

def run_steps(steps):
    accumulator = 0
    current_step = 0
    visited_steps = set()
    has_infinite_loop = True

    while current_step not in visited_steps:
        if current_step >= len(steps):
            has_infinite_loop = False
            break
        visited_steps.add(current_step)
        # execute step
        step = steps[current_step]
        [operation, units] = step.split(" ")
        units = int(units)
        if operation == "nop":
            current_step += 1
        if operation == "acc":
            accumulator += units
            current_step += 1
        if operation == "jmp":
            current_step += units

    return {
        'has_infinite_loop': has_infinite_loop,
        'accumulator': accumulator
    }


for step_idx in range(len(steps)):
    step = steps[step_idx]
    [operation, _] = step.split(" ")
    if operation == "acc":
        continue
    modified_steps = steps.copy()
    swapped_step = step.replace("nop", "jmp") if operation == "nop" else step.replace("jmp", "nop")
    modified_steps[step_idx] = swapped_step
    run = run_steps(modified_steps)
    if run['has_infinite_loop']:
        continue
    else:
        print("found answer")
        print(f"step to swap: {step_idx}")
        print(run['accumulator'])
