MENU = {
    1: {"name": "Chicken Adobo with Rice", "price": 85.00},
    2: {"name": "Beef Tapa with Rice", "price": 95.00},
    3: {"name": "Pork Sisig", "price": 120.00},
    4: {"name": "Pancit Canton", "price": 70.00},
    5: {"name": "Burger Steak with Rice", "price": 80.00},
    6: {"name": "Fried Chicken (2pcs) + Rice", "price": 90.00},
    7: {"name": "Milo With Rice", "price": 60.00},
    8: {"name": "Turon With Rice (2pcs)", "price": 30.00},
    9: {"name": "Soft Drink With Rice (Coke/Sprite)", "price": 25.00},
    10: {"name": "Bottled Water With Rice", "price": 15.00},
}


def clear_screen():
    print("\n" * 2)


def show_menu():
    print("=" * 50)
    print("          CANTEEN MENU (₱)")
    print("=" * 50)
    for num, item in MENU.items():
        print(f"  {num:2}. {item['name']:<30} ₱{item['price']:.2f}")
    print("=" * 50)


def show_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return 0.0

    print("\n" + "-" * 50)
    print("YOUR ORDER:")
    print("-" * 50)
    total = 0.0
    for i, item in enumerate(cart, 1):
        subtotal = item["price"] * item["qty"]
        total += subtotal
        print(f"  {i}. {item['name']} x{item['qty']}  =  ₱{subtotal:.2f}")
    print("-" * 50)
    print(f"  TOTAL: ₱{total:.2f}")
    print("-" * 50)
    return total


def main():
    cart = []

    while True:
        clear_screen()
        show_menu()
        print("\nOptions:")
        print("  [A] Add item to order")
        print("  [V] View cart")
        print("  [C] Checkout")
        print("  [X] Exit")

        choice = input("\nEnter choice: ").strip().upper()

        if choice == "A":
            while True:
                item_input = input("Enter item number (or type [B] to go back): ").strip().upper()
                if item_input == "B":
                    break

                try:
                    item_num = int(item_input)
                    if item_num not in MENU:
                        print("Invalid item number! Please choose from the menu.")
                        input("Press Enter to try again...")
                        continue

                    while True:
                        try:
                            qty = int(input("Enter quantity: "))
                            if qty <= 0:
                                print("Quantity must be at least 1.")
                                continue
                            break
                        except ValueError:
                            print("Please enter a valid number for quantity.")

                    selected = MENU[item_num]
                    cart.append({
                        "name": selected["name"],
                        "price": selected["price"],
                        "qty": qty
                    })
                    print(f"\nAdded {qty}x {selected['name']} to cart.")
                    input("Press Enter to continue...")
                    break

                except ValueError:
                    print("Please enter a valid number for the item.")
                    input("Press Enter to try again...")

        elif choice == "V":
            show_cart(cart)
            input("\nPress Enter to continue...")

        elif choice == "C":
            total = show_cart(cart)
            if total == 0:
                input("\nPress Enter to continue...")
                continue

            print("\nProceed to payment?")
            confirm = input("Type YES to confirm order, or Type NO to go Back: ").strip().upper()

            if confirm == "YES":
                print("\n" + "=" * 50)
                print("          ORDER CONFIRMED!")
                print(f"          Please pay ₱{total:.2f}")
                print("          Thank you! Enjoy your meal!")
                print("=" * 50)
                cart.clear()
                break

            elif confirm == "NO":
                print("\nReturning to menu...")
                input("Press Enter to continue...")

            else:
                print("Invalid choice. Returning to menu...")
                input("Press Enter to continue...")

        elif choice == "X":
            print("\nThank you! Goodbye!")
            break

        else:
            print("Invalid choice! Please choose A, V, C, or X.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()