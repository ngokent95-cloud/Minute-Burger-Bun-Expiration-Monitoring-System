from datetime import datetime

print("===================================")
print("    BUN INVENTORY MANAGEMENT")
print("===================================")

# LOGIN ACCOUNTS
users = {
    "staff@gmail.com": {
        "password": "staff123",
        "role": "Staff"
    },
    "manager@gmail.com": {
        "password": "manager123",
        "role": "Manager"
    }
}

# BUN TYPES
bun_types = [
    "Soft Burger Bun",
    "Brioche Bun",
    "Oatmeal-Sprinkled Brioche Bun",
    "Brioche Hotdog Bun",
    "Signature Hotdog Bun",
    "New Bun"
]

# INVENTORY STORAGE
products = []


# CHOICE INPUT WITH BACK OPTION
def get_choice(prompt, valid_choices):
    while True:
        answer = input(prompt).strip()

        if answer.upper() == "BACK":
            return "BACK"

        if answer in valid_choices:
            return answer

        print("Invalid choice. Please try again or type BACK.")


# QUANTITY INPUT
def get_quantity(prompt, allow_zero=False):
    while True:
        answer = input(prompt).strip()

        if answer.upper() == "BACK":
            return None

        try:
            quantity = int(answer)

            if quantity < 0:
                print("Quantity cannot be negative.")
            elif quantity == 0 and not allow_zero:
                print("Quantity must be greater than zero.")
            else:
                return quantity

        except ValueError:
            print("Invalid quantity. Enter a whole number only.")
            print("Example: 10")


# EXPIRATION DATE INPUT
def get_expiration_date():
    while True:
        answer = input(
            "Enter expiration date (MM/DD/YYYY) or BACK: "
        ).strip()

        if answer.upper() == "BACK":
            return None

        try:
            expiration = datetime.strptime(
                answer, "%m/%d/%Y"
            ).date()

            today = datetime.today().date()

            if expiration < today:
                print("This bun is already expired.")
                print("Please enter a future expiration date.")
            else:
                return expiration

        except ValueError:
            print("Invalid date. Please use MM/DD/YYYY.")
            print("Example: 12/31/2026")


# CHECK EXPIRATION STATUS
def get_status(expiration):
    today = datetime.today().date()
    days_remaining = (expiration - today).days

    if days_remaining < 0:
        status = "Expired"
    elif days_remaining <= 7:
        status = "Expiring Soon"
    else:
        status = "Safe"

    return days_remaining, status


# UPDATE INVENTORY STATUSES
def update_inventory_dates():
    for product in products:
        days, status = get_status(product["expiration"])
        product["days_remaining"] = days
        product["status"] = status


# PRINT INVENTORY TABLE
def print_table(items):
    if not items:
        print("\nNo products found.")
        return

    update_inventory_dates()

    print("-" * 105)
    print(
        f"{'No.':<5}"
        f"{'Bun Type':<35}"
        f"{'Quantity':<12}"
        f"{'Expiration':<16}"
        f"{'Days Left':<12}"
        f"{'Status':<18}"
    )
    print("-" * 105)

    for number, product in enumerate(items, start=1):
        expiration = product["expiration"].strftime("%m/%d/%Y")

        print(
            f"{number:<5}"
            f"{product['name']:<35}"
            f"{product['quantity']:<12}"
            f"{expiration:<16}"
            f"{product['days_remaining']:<12}"
            f"{product['status']:<18}"
        )

    print("-" * 105)


# FIND A PRODUCT
def find_product():
    if not products:
        print("\nInventory is empty.")
        return None

    print("\n========== SELECT A BUN ==========")

    for number, product in enumerate(products, start=1):
        print(
            f"{number}. {product['name']} "
            f"(Quantity: {product['quantity']})"
        )

    print("Type BACK to return.")

    while True:
        answer = input("Enter product number: ").strip()

        if answer.upper() == "BACK":
            return None

        try:
            number = int(answer)

            if 1 <= number <= len(products):
                return products[number - 1]

            print("Invalid product number.")

        except ValueError:
            print("Please enter a whole number.")


# ADD BUN
def add_bun():
    print("\n========== ADD BUN ==========")

    for number, bun in enumerate(bun_types, start=1):
        print(f"{number}. {bun}")

    print("Type BACK to return.")

    choice = get_choice(
        "Choose bun type: ",
        [str(i) for i in range(1, len(bun_types) + 1)]
    )

    if choice == "BACK":
        return

    bun_name = bun_types[int(choice) - 1]

    # CREATE A CUSTOM BUN NAME
    if choice == "6":
        while True:
            custom_name = input(
                "Enter new bun name or BACK: "
            ).strip()

            if custom_name.upper() == "BACK":
                return

            if not custom_name:
                print("Bun name cannot be empty.")
                continue

            # Prevent duplicate bun type names
            if any(
                name.lower() == custom_name.lower()
                for name in bun_types
                if name != "New Bun"
            ):
                print("This bun name already exists.")
                continue

            bun_name = custom_name

            # Add the custom name for future use
            bun_types.append(custom_name)
            break

    quantity = get_quantity("Enter quantity: ")

    if quantity is None:
        return

    expiration = get_expiration_date()

    if expiration is None:
        return

    # Combine matching bun types with the same expiration date
    existing_product = None

    for product in products:
        if (
            product["name"] == bun_name
            and product["expiration"] == expiration
        ):
            existing_product = product
            break

    if existing_product:
        existing_product["quantity"] += quantity
    else:
        products.append({
            "name": bun_name,
            "quantity": quantity,
            "expiration": expiration,
            "days_remaining": 0,
            "status": ""
        })

    update_inventory_dates()

    print("\nBun added successfully!")
    print("Bun Type:", bun_name)
    print("Quantity:", quantity)
    print("Expiration:", expiration.strftime("%m/%d/%Y"))


# VIEW INVENTORY
def view_inventory():
    while True:
        print("\n========== VIEW INVENTORY ==========")
        print("1. View All Inventory")
        print("2. View Expired Buns")
        print("3. View Expiring Soon")
        print("4. View Safe Buns")
        print("5. Back to Main Menu")
        print("====================================")

        choice = get_choice(
            "Enter your choice: ",
            ["1", "2", "3", "4", "5"]
        )

        if choice == "BACK" or choice == "5":
            return

        update_inventory_dates()

        if choice == "1":
            print("\nALL INVENTORY")
            print_table(products)

        elif choice == "2":
            print("\nEXPIRED BUNS")
            items = [
                product for product in products
                if product["status"] == "Expired"
            ]
            print_table(items)

        elif choice == "3":
            print("\nEXPIRING SOON")
            items = [
                product for product in products
                if product["status"] == "Expiring Soon"
            ]
            print_table(items)

        elif choice == "4":
            print("\nSAFE BUNS")
            items = [
                product for product in products
                if product["status"] == "Safe"
            ]
            print_table(items)


# MANAGER: EDIT INVENTORY
def manager_edit_inventory():
    print("\n========== EDIT INVENTORY ==========")

    product = find_product()

    if product is None:
        return

    print("\n1. Change Quantity")
    print("2. Change Expiration Date")
    print("3. Back")

    choice = get_choice(
        "Enter your choice: ",
        ["1", "2", "3"]
    )

    if choice == "BACK" or choice == "3":
        return

    if choice == "1":
        quantity = get_quantity(
            "Enter new quantity: ",
            allow_zero=True
        )

        if quantity is None:
            return

        product["quantity"] = quantity
        print("Quantity updated successfully!")

    elif choice == "2":
        expiration = get_expiration_date()

        if expiration is None:
            return

        product["expiration"] = expiration
        print("Expiration date updated successfully!")

    update_inventory_dates()


# MANAGER: TAKE BUNS OUT
def manager_take_buns():
    print("\n========== TAKE BUNS OUT ==========")

    product = find_product()

    if product is None:
        return

    if product["quantity"] == 0:
        print("There is no stock available.")
        return

    quantity = get_quantity("How many buns will be taken out? ")

    if quantity is None:
        return

    if quantity > product["quantity"]:
        print("Not enough stock available.")
        print("Current quantity:", product["quantity"])
        return

    product["quantity"] -= quantity

    print("\nStock updated successfully!")
    print("Remaining quantity:", product["quantity"])


# MANAGER: REMOVE BUN
def manager_remove_bun():
    print("\n========== REMOVE BUN ==========")

    product = find_product()

    if product is None:
        return

    print("\nSelected bun:", product["name"])
    print("1. Confirm removal")
    print("2. Cancel")

    choice = get_choice(
        "Enter your choice: ",
        ["1", "2"]
    )

    if choice == "BACK" or choice == "2":
        print("Removal cancelled.")
        return

    products.remove(product)
    print("Product removed successfully!")


# MANAGE INVENTORY SUBMENU
def manage_inventory():
    while True:
        print("\n========== MANAGE INVENTORY ==========")
        print("1. Edit Inventory")
        print("2. Take Buns Out")
        print("3. Remove Bun")
        print("4. Back to Manager Menu")
        print("======================================")

        choice = get_choice(
            "Enter your choice: ",
            ["1", "2", "3", "4"]
        )

        if choice == "BACK" or choice == "4":
            return

        elif choice == "1":
            manager_edit_inventory()

        elif choice == "2":
            manager_take_buns()

        elif choice == "3":
            manager_remove_bun()


# LOGIN
def login():
    while True:
        print("\n========== LOGIN ==========")
        print("1. Staff")
        print("2. Manager")
        print("3. Exit")

        role_choice = get_choice(
            "Choose your role: ",
            ["1", "2", "3"]
        )

        if role_choice == "3":
            return None

        if role_choice == "1":
            selected_role = "Staff"
        else:
            selected_role = "Manager"

        email = input("Enter your Gmail or BACK: ").strip()

        if email.upper() == "BACK":
            continue

        password = input("Enter your password or BACK: ").strip()

        if password.upper() == "BACK":
            continue

        if email in users:
            if (
                users[email]["password"] == password
                and users[email]["role"] == selected_role
            ):
                print("\nLogin successful!")
                print("Welcome,", selected_role)
                return selected_role

        print("Invalid Gmail, password, or role.")
        print("Please try again.")


# MAIN PROGRAM
def main():
    while True:
        role = login()

        if role is None:
            print("\nThank you for using the system!")
            break

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. Add Bun")
            print("2. View Bun Inventory")

            if role == "Manager":
                print("3. Manage Inventory")
                print("4. Log Out")
            else:
                print("3. Log Out")

            print("===============================")

            if role == "Manager":
                choice = get_choice(
                    "Enter your choice: ",
                    ["1", "2", "3", "4"]
                )
            else:
                choice = get_choice(
                    "Enter your choice: ",
                    ["1", "2", "3"]
                )

            if choice == "BACK":
                continue

            elif choice == "1":
                add_bun()

            elif choice == "2":
                view_inventory()

            elif role == "Manager" and choice == "3":
                manage_inventory()

            elif (
                (role == "Staff" and choice == "3")
                or (role == "Manager" and choice == "4")
            ):
                print("\nLogging out...")
                break


# RUN PROGRAM
if _name_ == "_main_":
    main()
