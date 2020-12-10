with open("./day10.txt") as f:
    rows = f.read().strip().split("\n")
    nums = [int(row) for row in rows]

sorted_nums = sorted(nums)

diff_1s = 0
diff_2s = 0
diff_3s = 0

current = 0
for num in sorted_nums:
    diff = num - current
    if diff == 1:
        diff_1s += 1
    if diff == 2:
        diff_2s += 1
    if diff == 3:
        diff_3s += 1
    current = num
# add one last 3
diff_3s += 1

print(diff_1s)
print(diff_2s)
print(diff_3s)
print(diff_1s * diff_3s)


# part 2

max_num = 179
max_idx = len(nums) - 1

# return list of possible next indexes
def possible_next_idxs(idx):
    if idx == max_idx:
        return []
    output = []
    next_idx = idx + 1
    while next_idx <= max_idx:
        diff = sorted_nums[next_idx] - sorted_nums[idx]
        if diff > 3:
            break
        output.append(next_idx)
        next_idx += 1
    return output

cache = {}

# return num ways of reaching idx
# ways to reach max from idx = sum of ways to reach max from all the possible next_steps of idx
def ways_to_reach_max_from(idx):
    if cache.get(idx):
        return cache.get(idx)
    if idx == max_idx:
        return 1
    possible_next_steps = possible_next_idxs(idx)
    return sum([ways_to_reach_max_from(i) for i in possible_next_steps])

# build cache
for i in reversed(range(len(nums))):
    answer = ways_to_reach_max_from(i)
    cache[i] = answer

final_answer = cache.get(0) + cache.get(1) + cache.get(2)
