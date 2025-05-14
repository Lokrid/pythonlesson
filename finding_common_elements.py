def common_elements():
    multiples_of_3 = {number for number in range(100) if number % 3 == 0}
    multiples_of_5 = {number for number in range(100) if number % 5 == 0}
    return multiples_of_3 & multiples_of_5


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
