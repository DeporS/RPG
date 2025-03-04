from database import add_item, get_all_items, give_player_item, get_all_player_items


def menu():
    print("\n----- Menu -----")
    print("1. Add item")
    print("2. Give player item")
    print("3. Print player items")
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


def give_item_details():
    print("Give items to:")
    player_name = input("Player name: ")
    item_name = input("Item name: ")
    quantity = int(input("Quantity: "))
    return player_name, item_name, quantity


while True:
    choice = menu()

    if choice == '1':
        name, description, item_type = get_item_details()
        add_item(name, description, item_type)
        print("Item added to database succesfully.")
    elif choice == '2':
        player_name, item_name, quantity = give_item_details()
        give_player_item(player_name, item_name, quantity)
        print("Item given succesfully!")
    elif choice == '3':
        player_name = input("Players name: ")
        player_items = get_all_player_items(player_name)
        for item, quantity in player_items:
            print(f"{item}: {quantity}")
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
