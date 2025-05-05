from pprint import pprint

# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

some_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7], [8, 4, 1]]

result = [[lst[0], lst[2], lst[-2]] for lst in some_list if len(lst) >= 3]

pprint(result)

pass
