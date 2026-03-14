class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_info(self):
        return (
            f"Product Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Quantity: {self.quantity}\n"
        )
