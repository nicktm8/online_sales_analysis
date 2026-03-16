from product import Product

class Cart:
    
    def __init__(self):
        self.cart_items = []
    
    def add_to_cart(self, product, quantity):
        product.update_quantity(quantity)
        self.cart_items.append(product)

    def total_cart_price(self):
        return sum(product.price * product.quantity for product in self.cart_items) 
    
    def display_cart(self):
        for product in self.cart_items:
            print(product.display_info())
                 