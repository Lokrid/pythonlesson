import string


def range_letters(input_str):
    all_letters = string.ascii_letters
    start, end = input_str.split("-")
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)
    return all_letters[start_index : end_index + 1]


user_input = input("Enter hyphenated letters (a-c): ")
print(range_letters(user_input))
