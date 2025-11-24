# -----------------------------------------
# Online Shopping Cart Simulation in Python
# -----------------------------------------

from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    price: float
    stock: int

class ShoppingCart:
    def __init__(self):
        # key = product_id, value = quantity
        self.items = {}

    def add_item(self, product: Product, quantity: int):
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity > product.stock:
            print(f"Sorry, only {product.stock} item(s) available in stock.")
            return

        # Add to cart
        if product.id in self.items:
            self.items[product.id] += quantity
        else:
            self.items[product.id] = quantity

        # Reduce stock from store
        product.stock -= quantity
        print(f"✅ Added {quantity} x {product.name} to cart.")

    def remove_item(self, product: Product, quantity: int):
        if product.id not in self.items:
            print("This item is not in your cart.")
            return

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if quantity >= self.items[product.id]:
            # Remove completely
            removed_qty = self.items.pop(product.id)
        else:
            self.items[product.id] -= quantity
            removed_qty = quantity

        # Return stock to store
        product.stock += removed_qty
        print(f"✅ Removed {removed_qty} x {product.name} from cart.")

    def is_empty(self):
        return len(self.items) == 0

    def view_cart(self, products: dict):
        if self.is_empty():
            print("\n🛒 Your cart is empty.\n")
            return

        print("\n🛒 Your Cart:")
        print("-" * 40)
        total = 0.0
        for product_id, qty in self.items.items():
            product = products[product_id]
            line_total = product.price * qty
            total += line_total
            print(f"{product.name} (x{qty}) - ₹{product.price:.2f} each | Line total: ₹{line_total:.2f}")
        print("-" * 40)
        print(f"Total Amount: ₹{total:.2f}\n")

    def checkout(self, products: dict):
        if self.is_empty():
            print("Your cart is empty. Nothing to checkout.")
            return

        print("\n====== CHECKOUT BILL ======")
        self.view_cart(products)
        print("Thank you for shopping with us! 🎉")
        # Clear the cart
        self.items.clear()

def show_products(products: dict):
    print("\n📦 Available Products:")
    print("-" * 60)
    print(f"{'ID':<5}{'Name':<20}{'Price (₹)':<15}{'Stock':<10}")
    print("-" * 60)
    for p in products.values():
        print(f"{p.id:<5}{p.name:<20}₹{p.price:<14.2f}{p.stock:<10}")
    print("-" * 60)

def get_product_by_id(products: dict, product_id: int):
    return products.get(product_id)

def main():
    # Sample product catalog
    products = {
        1: Product(1, "Laptop", 55000.0, 5),
        2: Product(2, "Smartphone", 20000.0, 10),
        3: Product(3, "Headphones", 1500.0, 20),
        4: Product(4, "Smartwatch", 4000.0, 8),
        5: Product(5, "Backpack", 800.0, 15)
    }

    cart = ShoppingCart()

    while True:
        print("\n===== ONLINE SHOPPING CART MENU =====")
        print("1. View Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout and Exit")
        print("6. Exit without Checkout")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            show_products(products)

        elif choice == "2":
            show_products(products)
            try:
                pid = int(input("Enter Product ID to add: "))
                product = get_product_by_id(products, pid)
                if product is None:
                    print("Invalid Product ID.")
                    continue
                qty = int(input("Enter quantity: "))
                cart.add_item(product, qty)
            except ValueError:
                print("Please enter a valid number for ID and quantity.")

        elif choice == "3":
            cart.view_cart(products)
            try:
                pid = int(input("Enter Product ID to remove: "))
                product = get_product_by_id(products, pid)
                if product is None:
                    print("Invalid Product ID.")
                    continue
                qty = int(input("Enter quantity to remove: "))
                cart.remove_item(product, qty)
            except ValueError:
                print("Please enter a valid number for ID and quantity.")

        elif choice == "4":
            cart.view_cart(products)

        elif choice == "5":
            cart.checkout(products)
            print("Exiting program...")
            break

        elif choice == "6":
            print("Exiting without checkout. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()