# 🛒 Python OOP – Online Sales Analysis

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-Object%20Oriented-green)]()
[![Status](https://img.shields.io/badge/Project-Portfolio%20Ready-brightgreen)]()

A modular Python project for managing product inventory and a shopping cart, built using Object-Oriented Programming and version-controlled with Git and GitHub.

---

## 🚀 Key Features

- Product creation with name, price, and quantity
- Product inventory management (add, remove, display)
- Total inventory value calculation
- Shopping cart with dynamic item and quantity management
- Total cart price calculation
- Clean separation of concerns across multiple modules

---

## 🧠 OOP Concepts Demonstrated

### ✅ Classes & Objects

- `Product` — represents a single product with attributes and methods
- `ProductManager` — manages a collection of `Product` objects
- `Cart` — handles cart items and calculates totals
- Each class is instantiated and used in `main.py`

### ✅ Git & GitHub Workflow

- Project developed using Git for version control
- Commits tracked across the full development lifecycle
- Repository hosted and managed on GitHub

---

## 📂 Project Structure

```
online_sales_analysis/
├── product.py
├── product_manager.py
├── cart.py
├── main.py
├── config.json
└── .gitignore
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

...
--------------------
Total inventory value: 63,530.00 EUR

----------Cart----------

Product Name: Macbook Pro M3
Price: 1,550.00 EUR
Quantity: 1

...
Total Cart price is: 4,400.00 EUR
```

---

## 🎯 Project Purpose

This project was developed to strengthen understanding of:

- Designing and working with Python classes and objects
- Building multi-file, modular Python projects
- Managing code with Git and GitHub
- Applying OOP principles to a real-world-style use case

---

## 🔮 Possible Future Improvements

- CLI interactive menu
- Data persistence (JSON or SQLite)
- Unit testing (pytest)
- Search and filter products by name or price
- Flask or FastAPI REST API version

---

## 👨‍💻 Author

**Nick Tem**  
Aspiring Python Developer

GitHub: https://github.com/nicktm8