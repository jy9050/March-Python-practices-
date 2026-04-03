balance = 1000
history = []

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. History")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance += amount
        history.append(f"Deposited {amount}")

    elif choice == "3":
        amount = int(input("Enter amount: "))
        if amount > balance:
            print("Insufficient balance ❌")
        else:
            balance -= amount
            history.append(f"Withdraw {amount}")

    elif choice == "4":
        for item in history:
            print(item)

    elif choice == "5":
        print("Thank you 💙")
        break

    else:
        print("Invalid choice ❌")