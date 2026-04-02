memory = 0
history = []
last_result = None

while True:
    op = input("\nEnter operator (+, -, *, /, %, M+, M-, MR, MC, history, exit): ").strip()

    # Exit
    if op == "exit":
        print("\nFinal History:")
        for item in history:
            print(item)
        break

    # Show history
    if op == "history":
        if len(history) == 0:
            print("No history yet")
        else:
            print("\nHistory:")
            for item in history:
                print(item)
        continue

    # Memory Read
    if op == "MR":
        print("Memory:", memory)
        continue

    # Memory Clear
    if op == "MC":
        memory = 0
        print("Memory cleared")
        continue

    # Memory Add
    if op == "M+":
        if last_result is not None:
            memory += last_result
            print("Memory:", memory)
        else:
            print("No result yet ❌")
        continue

    # Memory Subtract
    if op == "M-":
        if last_result is not None:
            memory -= last_result
            print("Memory:", memory)
        else:
            print("No result yet ❌")
        continue

    # Invalid operator check
    if op not in ["+", "-", "*", "/", "%"]:
        print("Invalid operator ❌")
        continue

    # Input numbers safely
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except:
        print("Invalid number ❌")
        continue

    # Calculation
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero ❌")
            continue
    elif op == "%":
        result = num1 % num2

    # Store last result
    last_result = result

    # Print result
    print("Result:", result)

    # Save history
    history.append(f"{num1} {op} {num2} = {result}")