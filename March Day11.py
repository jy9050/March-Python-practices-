num1 = int(input("Enter first number:    "))
num2 = int(input("Enter second number:    "))
op = input("Enter operator:  ").strip()

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero X")
        
        
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid Operator")        