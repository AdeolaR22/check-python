
def calculator(num1, num2):

    operator = input("Enter an operator (+, -, *, /): ")

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2

    else:
        return "Invalid operator!"


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))


result = calculator(first_number, second_number)


print("The result is:", result)
