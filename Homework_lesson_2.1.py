user_input = int(input("Введіть 4-значне число: "))

digit1 = user_input // 1000
digit2 = (user_input % 1000) // 100
digit3 = (user_input % 100) // 10
digit4 = user_input % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)
pass
