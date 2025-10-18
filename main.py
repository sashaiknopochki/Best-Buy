from products import Product
from store import Store


# Setup initial stock of inventory
mac = Product(name="MacBook Air M2", price=1450, quantity=100)
bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product(name="Google Pixel 7", price=500, quantity=250)
product_list = [mac, bose, pixel]
best_buy = Store(product_list)


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
        print(store.get_all_products())
        start(store)
    elif choice == "2":
        print(f"Total of {store.get_total_quantity()} items in store.")
    elif choice == "3":
        shopping_list = []
        pass
    elif choice == "4":
        exit()
    else:
        print("Please choose a valid number.")



def main():
    start(best_buy)



if __name__ == "__main__":
    main()







"""
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product("Google Pixel 7", price=500, quantity=250)


# Temp tests


product_list = [mac, bose, pixel]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))

print(mac.get_quantity())

mac.set_quantity(0)
print(mac.get_quantity())

print(mac.is_active())

mac.activate()
print(mac.is_active())

mac.deactivate()
print(mac.is_active())

print(bose.show())

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()"""