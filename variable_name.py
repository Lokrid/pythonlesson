import string
import keyword


def name_variable(name):
    if not name:
        return False

    if name[0].isdigit():
        return False

    if any(c.isupper() for c in name):
        return False

    if any(c in string.punctuation.replace("_", "") or c.isspace() for c in name):
        return False

    if name in keyword.kwlist:
        return False

    if set(name) == {"_"} and len(name) > 1:
        return False

    return True


user_input = input("Enter a variable name: ")
print(name_variable(user_input))
