# 🛒 Python OOP Product Inventory & Cart System

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-Object%20Oriented-green)](https://github.com/nicktm8/online_sales_analysis)
[![Git](https://img.shields.io/badge/Version%20Control-Git%20%26%20GitHub-orange)](https://github.com/nicktm8/online_sales_analysis/commits/main)
[![Status](https://img.shields.io/badge/Project-Portfolio%20Ready-brightgreen)](https://github.com/nicktm8/online_sales_analysis)

A modular Python project for managing product inventory and a shopping cart using Object-Oriented Programming principles and Git & GitHub for version control.

---

## 🚀 Key Features

- Product creation with name, price, and quantity
- Product inventory management (add, remove, display)
- Total inventory value calculation
- Shopping cart with dynamic item addition
- Total cart price calculation
- Clean, readable console output with EUR formatting

---

## 🗃️ Sample Products

| Product | Price (EUR) | Quantity |
|---|---|---|
| Macbook Pro M3 | 1,550.00 | 15 |
| Samsung Galaxy S25 Ultra | 1,100.00 | 10 |
| Samsung Galaxy Tab S11 | 899.00 | 20 |
| Dell Gaming Monitor (27 inch) | 250.00 | 30 |

---

## 🧠 OOP Concepts Demonstrated

### ✅ Classes & Objects

- `Product` — represents a single product with name, price, and quantity
- `ProductManager` — manages a collection of `Product` objects (add, remove, display, calculate inventory value)
- `Cart` — handles shopping cart logic, including adding items and computing total price

### ✅ Git & GitHub Workflow

- Project developed using Git for version control
- Organized commits tracking incremental development
- Hosted publicly on GitHub as a portfolio project

---

## 📂 Project Structure

```
online_sales_analysis/
├── .gitignore
├── cart.py
├── config.json
├── main.py
├── product.py
└── product_manager.py
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/nicktm8/online_sales_analysis.git
```

2. Navigate to the project directory:

```
cd online_sales_analysis
```

3. Run the program:

```
python main.py
```

---

## 📊 Example Output

```
------------List of Products--------------

Product Name: Macbook Pro M3
Price: 1,550.00 EUR
Quantity: 15

Product Name: Samsung Galaxy S25 Ultra
Price: 1,100.00 EUR
Quantity: 10

Product Name: Samsung Galaxy Tab S11
Price: 899.00 EUR
Quantity: 20

Product Name: Dell Gaming Monitor (27 inch)
Price: 250.00 EUR
Quantity: 30

--------------------
Total inventory value: 72,780.00 EUR

----------Cart----------

Product Name: Macbook Pro M3
Price: 1,550.00 EUR
Quantity: 1

Product Name: Samsung Galaxy S25 Ultra
Price: 1,100.00 EUR
Quantity: 2

Product Name: Dell Gaming Monitor (27 inch)
Price: 250.00 EUR
Quantity: 3

Total Cart price is: 4,500.00 EUR
```

---

## 🎯 Project Purpose

This project was developed to strengthen understanding of:

- Designing and using Python classes and objects
- Building modular, multi-file Python projects
- Managing code with Git and GitHub
- Applying OOP concepts in a practical, real-world scenario

It serves as a clean backend-style foundation suitable for further expansion.

---

## 🔮 Possible Future Improvements

- CLI interactive menu for managing products and cart
- Data persistence (JSON or SQLite)
- Unit testing (pytest)
- Discount and coupon system
- Flask or FastAPI REST API version

---

## 👨‍💻 Author

**Nick Tem**  
Aspiring Python Developer

GitHub: https://github.com/nicktm8