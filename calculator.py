# Program 1

num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /, %): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2

elif op == "-":
    result = num1 - num2

elif op == "*":
    result = num1 * num2

elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num1 / num2

elif op == "%":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        exit()
    result = num1 % num2

else:
    print("Invalid operator! Use +, -, *, /, or %.")
    exit()

print("Result:", result)
