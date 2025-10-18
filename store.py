class Store:
    def __init__(self, product_list: list) -> None:
        self.product_list = product_list

    def add_product(self, product: object) -> list:
        """Adds a product to a store."""
        self.product_list.append(product)
        return self.product_list

    def remove_product(self, product: object) -> list:
        """Removes a product from a store."""
        self.product_list.remove(product)
        return self.product_list

    def get_total_quantity(self) -> int:
        """Returns the total quantity of products in the store."""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Returns all products in the store that are active."""
        active_products = []
        for i, product in enumerate(self.product_list, 1):
            if product.is_active():
                product_details = f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}"
                active_products.append(product_details + "\n")
        active_products.append("----------")
        result = "".join(active_products)
        return result

    def order(self, shopping_list: list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        - Product (Product class) and quantity (int).
        - Buys the products and returns the total price of the order."""
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
