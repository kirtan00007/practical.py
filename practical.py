inventory = []

def add_item():
    item_name = input("\nEnter item name: ")
    category = input("Enter category: ").lower()
    quantity = int(input("Enter quantity: "))

    inventory.append({
        "name": item_name,
        "category": category,
        "quantity": quantity
    })

def show_summary():
    print("\n=========== INVENTORY REPORT ===========\n")

    if not inventory:
        print("No items in inventory!")
        return


    print(f"Total Different Items: {len(inventory)}")

    total_quantity = sum(item['quantity'] for item in inventory)
    print(f"Total Quantity in Stock: {total_quantity}")

    category_count = {}
    for item in inventory:
        category_count[item['category']] = category_count.get(item['category'], 0) + item['quantity']

    print("\nCategory-wise Stock:")
    for cat, qty in category_count.items():
        print(f" - {cat.capitalize()}: {qty}")

    most = max(inventory, key=lambda x: x['quantity'])
    least = min(inventory, key=lambda x: x['quantity'])
    print(f"\nMost Stocked Item: {most['name']} ({most['quantity']} units)")
    print(f"Least Stocked Item: {least['name']} ({least['quantity']} units)")

    print("\n========================================\n")

while True:
    print("\n1. Add Item")
    print("2. Show Inventory Summary")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        show_summary()
    elif choice == '3':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")