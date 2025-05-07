import string


def create_hashtag(text):

    cleaned = "".join(char for char in text if char not in string.punctuation)

    words = cleaned.split()

    hashtag = "#" + "".join(word.capitalize() for word in words)

    return hashtag[:140]


result = create_hashtag(input("Enter hashtag: "))

print(result)
