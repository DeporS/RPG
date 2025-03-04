from database import add_item, get_all_items


def menu():
    print("\n----- Menu -----")
    print("1. Add item")
    print("8. See all items")
    print("9. Exit")
    choice = input("Choose one option: ")
    return choice


def get_item_details():
    name = input("Input name: ")
    description = input("Input description: ")
    item_type = input(
        "Type (0 - crafting items, 1 - weapon, ...): ")
    return name, description, int(item_type)


while True:
    choice = menu()

    if choice == '1':
        name, description, item_type = get_item_details()
        add_item(name, description, item_type)
        print("Item added to database succesfully.")

    elif choice == '8':
        items = get_all_items()
        for item in items:
            print(
                f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Type: {item[3]}")
    elif choice == '9':
        print("Exiting.")
        break

    else:
        print("No such option, try again.")
