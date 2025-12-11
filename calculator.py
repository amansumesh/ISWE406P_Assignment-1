#Program 1:

num1 = float(input("Enter first number: "))
op = input("Enter operator (+ or -): ")
num2 = float(input("Enter second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
else:
    print("Invalid operator! Use + or - only.")
    exit()

print("Result:", result)

