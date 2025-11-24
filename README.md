# Online Shopping Cart Simulator

This project is a simple **online shopping cart simulator** built using **Python (Flask)**.  
It is made as a 1st year mini project to understand how an online shopping system works.

## 📌 Project Overview

The project simulates a basic online shopping flow:

1. User can see a list of products with name and price.
2. User can add products to a shopping cart.
3. User can open the cart page and see:
   - Product name
   - Quantity
   - Price
   - Line total (price × quantity)
   - Grand total amount
4. User can **checkout / clear** the cart.

Everything runs on the **browser**, but the logic is written in **Python**.

## 🧠 Concepts Used (Python Basics)

- **List** – to store the list of products.
- **Dictionary** – to store cart items (product id → quantity).
- **Functions** – for different actions (home page, add to cart, view cart, clear cart).
- **Loops and conditions** – to calculate quantities and totals.

Flask is used only to display the output in the browser instead of the terminal.

## 🛠️ Technologies / Tools

- Python 3
- Flask (lightweight web framework)
- HTML + CSS (for the web pages)
- VS Code (code editor)
- Git & GitHub (version control and hosting)

## 📂 Project Structure

```text
online-shopping-cart/
├── app.py               # Main Flask application
├── shopping_cart.py     # (Optional) Console-based version of the cart
├── templates/
│   ├── index.html       # Home page (product listing)
│   └── cart.html        # Cart page (items + total)
├── .gitignore           # To ignore virtual environment and cache files
└── README.md            # Project documentation (this file)