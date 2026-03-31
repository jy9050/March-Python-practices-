while True:
    op = input("Enter Operator(+,-,*,/,%)or'exit':").strip()
    if op == "exit":
        print("Calculator band ho gya")
        break
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "*":
        print(num1*num2)
    elif op == "/":
        if num2 !=0:
            print(num1/num2)
        else:
            print("Cannot divide by zero X")
    elif op == "%":
        print(num1%num2) 
    else:
        print("Invalid Operator")