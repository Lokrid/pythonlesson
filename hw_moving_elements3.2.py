examples = [[12, 3, 4, 10], [1], [], [12, 3, 4, 10, 8]]


def move_last_to_front(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]


results = []

for example in examples:
    new_list = move_last_to_front(example)
    results.append(new_list)

print(results)
