with open("./day9.txt") as f:
    rows = f.read().strip().split("\n")
    nums = [int(row) for row in rows]

window_size = 25

def possible_sums(values):
    sums = set()
    for i in range(0, len(values) - 1):
        for j in range(i + 1, len(values)):
            sums.add(values[i] + values[j])
    return sums

def get_window(idx):
    if idx < window_size:
        return []
    else:
        return nums[(idx - window_size):idx]

for idx in range(len(nums)):
    window = get_window(idx)
    possible_values = possible_sums(window)
    if not possible_values:
        continue
    if not nums[idx] in possible_values:
        print(idx)
        print(nums[idx])
        break

bad_idx = 502
bad_num = 15353384

# part 2

range_start = 0
answer = None
while range_start < len(nums):
    range_end = range_start + 2
    while range_end < len(nums):
        range_to_sum = nums[range_start:range_end]
        range_sum = sum(range_to_sum)
        if range_sum > bad_num:
            break
        if range_sum < bad_num:
            range_end += 1
        if range_sum == bad_num:
            answer = range_to_sum
            break
    if answer:
        print(answer)
        sorted_answer = sorted(answer)
        print(sorted_answer)
        print(sorted_answer[0] + sorted_answer[len(sorted_answer) - 1])
        break
    range_start += 1

