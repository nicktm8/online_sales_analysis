import product as pr
import product_manager as pm

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

