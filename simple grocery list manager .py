grocery = []  # Empty list

while True:
    print("\n1. Add item")
    print("2. Show list")
    print("3. Exit")

    choice = input("Enter 1 or 2 or 3: ")

    if choice == '1':
        item = input("Enter item: ")
        grocery.append(item)
        print(f"{item} added ✅")

    elif choice == '2':
        print("Your grocery list:")
        for i in grocery:
            print("- " + i)

    elif choice == '3':
        print("Bye 👋 Exit pannudhu")
        break

    else:
        print("❌ Invalid choice! Enter 1 / 2 / 3")
