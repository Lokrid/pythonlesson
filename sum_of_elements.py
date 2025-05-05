from pprint import pprint

# [1, 3, 5] => 30
# [6] => 36
# [] => 0

some_list = [[1, 3, 5], [6], []]


def sum_and_mult_of_end(lst):
    if not lst:
        return 0
    return sum(lst[some_list] for some_list in range(0, len(lst), 2)) * lst[-1]


result = []
for lst in some_list:
    result.append(sum_and_mult_of_end(lst))
pprint(result)
pass
