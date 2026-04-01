# History Store """"

history = []

while True :
    op = input("Enter Operator(+,/,-,*,%) or 'exit':")
    
    if op == "exit":
        print("History:", history)
        break
    
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter Second number:"))
    

    if op == "+":
        result = num1+num2
    
    elif op == "-":
     result = num1-num2
    
    elif op == "*":
     result = num1*num2
    
    elif op == "/":
     if num2 !=0:
        result = num1/num2
     else:
         print("Cannot divide by zero X")
         continue
    
    elif op == "%":
        result = num1%num2
    else:
         print("Invaild Operator X")
         continue
    print("Result:", result)
    history.append(result)    
    
    

        
    