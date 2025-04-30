slice1 = [[1, 2, 3, 4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5], [1], []]

results = []

for lst in slice1:
    length = len(lst)
    middle = (length + 1) // 2
    first_half = lst[:middle]
    second_half = lst[middle:]
    results.append([first_half, second_half])

for result in results:
    print(result)
pass
