class Product:
    def __init__(self, name, price, quantity):
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except Exception as e:
            print(e)


    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (int)."""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity. If the quantity reaches 0, deactivates the product."""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False
        return self.quantity


    def is_active(self) -> bool:
        """Getter function for active. Returns True if the product is active, otherwise False."""
        return self.active


    def activate(self):
        """Activates the product."""
        self.active = True
        return self.active


    def deactivate(self):
        """Deactivates the product."""
        self.active = False
        return self.active


    def show(self):
        """Prints a string that represents the product, for example: 'MacBook Air M2, Price: 1450, Quantity: 100'"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity) -> float:
        """
        - Buys a given quantity of the product.
        - Returns the total price (float) of the purchase.
        - Updates the quantity of the product.
        - In case of a problem (when? think about it), raises an Exception.
        """
        try:
            self.quantity -= quantity
        except Exception as e:
            print(e)
        return float(self.price * quantity)