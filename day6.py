def answers_in_group(group):
    group_answers = set()
    for item in group:
        answers = list(item)
        for char in answers:
            group_answers.add(char)
    return len(group_answers)


def answers_in_group(group):
    group_answers = {}
    for item in group:
        answers = list(item)
        for char in answers:
            if not group_answers.get(char):
                group_answers[char] = 1
            else:
                group_answers[char] = group_answers[char] + 1
    items_in_group = len(group)
    values = list(group_answers.values())
    return len([v for v in values if v == items_in_group])

sum = reduce(lambda x, y: x + answers_in_group(y), groups, 0)
