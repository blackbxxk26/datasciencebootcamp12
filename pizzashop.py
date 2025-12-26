def display_menu(menu):
    """Display menu with pricing"""
    print("\n" + "=" * 60)
    print("SSR PIZZA SHOP - MENU")
    print("=" * 60)
    for i, item in enumerate(menu, start=1):
        if isinstance(item["price"], dict):
            price_str = f"M: {item['price']['M']}฿ | L: {item['price']['L']}฿"
        else:
            price_str = f"{item['price']}฿"
        print(f"{i:2d}. {item['food']:<25} {price_str:>20}")
    print("=" * 60)


def parse_menu_selection(input_str, menu_size):
    """Parse comma-separated menu numbers"""
    try:
        selections = []
        parts = input_str.replace(" ", "").split(",")
        for part in parts:
            num = int(part)
            if 1 <= num <= menu_size:
                selections.append(num - 1)
            else:
                return None, f"Invalid menu number: {num}"
        return selections, None
    except ValueError:
        return None, "Please enter valid numbers separated by commas"


def take_order(menu):
    """Process customer order"""
    bill = []

    name = input("\nCustomer name: ").strip()
    if not name:
        name = "Guest"

    print(f"\nWelcome to SSR Pizza Shop, {name}!")
    print("You can order multiple items at once (e.g., 1,3,6)")

    while True:
        display_menu(menu)

        choice_input = input("\nSelect menu (comma-separated) or 'done' to checkout: ").strip().lower()

        if choice_input in ("done", "checkout", "finish", "x"):
            break

        # Parse selections
        selections, error = parse_menu_selection(choice_input, len(menu))
        if error:
            print(f"Error: {error}")
            continue

        # Process each selection
        for idx in selections:
            item = menu[idx]
            food_name = item["food"]

            # Handle size selection for pizza
            if isinstance(item["price"], dict):
                size = input(f"  Size for {food_name} (M/L): ").upper().strip()
                if size not in item["price"]:
                    print(f"  Error: Invalid size for {food_name}. Skipped.")
                    continue
                price = item["price"][size]
            else:
                size = "-"
                price = item["price"]

            # Get quantity
            units_input = input(f"  Quantity for {food_name}: ").strip()
            if not units_input.isdigit() or int(units_input) <= 0:
                print(f"  Error: Invalid quantity for {food_name}. Skipped.")
                continue

            units = int(units_input)
            total = price * units

            # Add to bill
            bill.append({
                "food": food_name,
                "size": size,
                "units": units,
                "price": price,
                "total": total
            })

            print(f"  Added: {food_name} ({size}) x{units} = {total}฿")

    return bill, name


def print_bill(bill, name):
    """Display receipt"""
    if not bill:
        print("\nNo items ordered.")
        return

    print("\n" + "=" * 70)
    print(f"{'RECEIPT - SSR PIZZA SHOP':^70}")
    print(f"{'Customer: ' + name:^70}")
    print("=" * 70)
    print(f"{'Item':<30} {'Size':<8} {'Qty':<6} {'Price':>10} {'Total':>10}")
    print("-" * 70)

    grand_total = 0
    for item in bill:
        size_display = item['size'] if item['size'] != '-' else 'N/A'
        print(f"{item['food']:<30} {size_display:<8} x{item['units']:<5} "
              f"{item['price']:>9}฿ {item['total']:>9}฿")
        grand_total += item["total"]

    print("=" * 70)
    print(f"{'TOTAL':>60} {grand_total:>9}฿")
    print("=" * 70)
    print("\nThank you for your order!")


# Menu data
menu = [
    {"food": "Hawaiian Pizza", "category": "Pizza", "price": {"M": 299, "L": 350}},
    {"food": "Pepperoni Pizza", "category": "Pizza", "price": {"M": 299, "L": 350}},
    {"food": "Seafood Pizza", "category": "Pizza", "price": {"M": 350, "L": 400}},
    {"food": "4 Cheese Pizza", "category": "Pizza", "price": {"M": 250, "L": 300}},
    {"food": "BBQ Chicken Pizza", "category": "Pizza", "price": {"M": 100, "L": 180}},
    {"food": "Coke", "category": "Drink", "price": 30},
    {"food": "Sprite", "category": "Drink", "price": 30},
    {"food": "Orange Juice", "category": "Drink", "price": 35},
]

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SSR PIZZA SHOP - ORDER SYSTEM v2.0")
    print("=" * 60)

    bill, customer_name = take_order(menu)
    print_bill(bill, customer_name)
