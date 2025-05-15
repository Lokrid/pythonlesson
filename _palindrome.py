import string


def is_palindrome(text):
    cleaned = "".join(letter.lower() for letter in text if letter.isalnum())
    return cleaned == cleaned[::-1]


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
