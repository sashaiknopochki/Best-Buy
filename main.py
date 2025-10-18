from products import Product
from store import Store


# Setup initial stock of inventory
mac = Product(name="MacBook Air M2", price=1450, quantity=100)
bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product(name="Google Pixel 7", price=500, quantity=250)
product_list = [mac, bose, pixel]
best_buy = Store(product_list)


# Features

# 1. List all products in store

def list_products(store):
    """Returns all products in the store that are active."""
    products = store.get_all_products()
    for i, product in enumerate(products, 1):
        print(f"{i}. {product[0]}, Price: ${product[1]}, Quantity: {product[2]}")
    print("----------")
    start(store)

# Test:
# list_products(best_buy)


# 2. Show total amount in store

def show_total_amount(store):
    total_amount = store.get_total_quantity()
    print(f"Total of {total_amount} items in store.")
    start(store)

# Test:
# show_total_amount(best_buy)


# 3. Make an order

def make_order(store):
    """
    Allows a user to build a shopping list until they enter an empty product choice.
    The order is placed only after the list is finalized.
    """
    shopping_list = []
    products = store.get_all_products()
    for i, product in enumerate(products, 1):
        print(f"{i}. {product[0]}, Price: ${product[1]}, Quantity: {product[2]}")
    print("----------")
    while True:
        print("When you want to finish order, enter empty text.")
        product_choice = input("Which product number would you like to order? ")
        if product_choice == "":
            break
        if not product_choice.isdigit():
            print("Error: Please enter a valid number!")
            continue
        if int(product_choice) > len(store.product_list):
            print("Error: Product number is out of range!")
            continue
        product_amount = input("What amount do you want? ")
        if not product_amount.isdigit():
            print("Error: Please enter a valid number!")
            continue
        if int(product_amount) > store.product_list[int(product_choice) - 1].get_quantity():
            print("Error: Product quantity is out of range!")
            continue
        shopping_list.append((store.product_list[int(product_choice) - 1], int(product_amount)))
        print(f"Product added to list!")

    if shopping_list:
        store.order(shopping_list)
        start(store)



# Test:
#make_order(best_buy)
#list_products(best_buy)



# Interface

def start(store):
    print("""
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
    choice = input("Please choose a number: ")
    print()
    if choice == "1":
        list_products(store)
    elif choice == "2":
        show_total_amount(store)
    elif choice == "3":
        make_order(store)
    elif choice == "4":
        exit()
    else:
        print("Please choose a valid number.")


def main():
    start(best_buy)


if __name__ == "__main__":
    main()