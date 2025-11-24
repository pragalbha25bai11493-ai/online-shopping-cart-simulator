from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "replace_with_any_secret_key"  # needed for session storage

# --------- DUMMY PRODUCT DATA ----------
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 55000},
    {"id": 2, "name": "Smartphone", "price": 20000},
    {"id": 3, "name": "Headphones", "price": 1500},
    {"id": 4, "name": "Smartwatch", "price": 4000},
    {"id": 5, "name": "Backpack", "price": 800},
]


def get_cart():
    """Get cart dictionary from session."""
    return session.get("cart", {})


@app.route("/")
def index():
    cart = get_cart()
    total_items = sum(cart.values())
    # show home page with products
    return render_template("index.html",
                           products=PRODUCTS,
                           total_items=total_items)


@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    cart = get_cart()
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    session["cart"] = cart
    return redirect(url_for("index"))


@app.route("/cart")
def view_cart():
    cart = get_cart()
    items = []
    total_price = 0

    for p in PRODUCTS:
        pid = str(p["id"])
        qty = cart.get(pid, 0)
        if qty > 0:
            line_total = qty * p["price"]
            total_price += line_total
            items.append({
                "name": p["name"],
                "price": p["price"],
                "qty": qty,
                "line_total": line_total
            })

    return render_template("cart.html",
                           items=items,
                           total_price=total_price)


@app.route("/clear")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)