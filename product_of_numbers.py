def multiply_digits_until_single(n):
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n


# Отримання числа від користувача
try:
    number = int(input("Enter a whole number: "))
    result = multiply_digits_until_single(number)
    print(result)
except ValueError:
    print("Please enter a valid integer.")
