def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter action (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    output = "Error: division by zero!"
                    print(output)
                    continue
                result = num1 / num2
            else:
                output = "Unknown operation!"
                print(output)
                continue

            output = f"Result: {result}"

        except ValueError:
            output = "Please enter numbers only."

        print(output)

        again = input("Would you like to continue? (y/yes to continue): ").lower()
        if again not in ["y", "yes"]:
            break


calculator()
