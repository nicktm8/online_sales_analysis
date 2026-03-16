import product as pr
import product_manager as pm
import cart

# Instance Product manager

manager = pm.ProductManager()

# List of products

products = [
        pr.Product("Macbook Pro M3", 1550, 15),
        pr.Product("Samsung Galaxy S25 Ultra", 1100, 10),
        pr.Product("Samsung Galaxy Tab S11", 899, 20),
        pr.Product("Dell Gaming Monitor (27 inch)", 250, 30)
]

# Adding products to product manager

manager.add_product(products[0])
manager.add_product(products[1])
manager.add_product(products[2])
manager.add_product(products[3])

# Display of products

print("\n------------List of Products--------------\n")
manager.display_products()

# Calculating total inventory value
print("-"*20)
total = manager.total_inventory_value()
print(f"Total inventory value: {total:,.2f} EUR")

shoping_cart = cart.Cart()
print("\n----------Cart----------\n")
shoping_cart.add_to_cart(manager.products[0], 1)
shoping_cart.add_to_cart(manager.products[1], 2)
shoping_cart.add_to_cart(manager.products[3], 3)

shoping_cart.display_cart()
