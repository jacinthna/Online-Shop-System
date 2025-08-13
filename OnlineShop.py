import uuid
from Procedural import product_list

class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.products = []  

    def import_from_store(self, store, price_map, desc_map):
        for p in store.get_products():
            price = price_map.get(p.name, 0)
            desc = desc_map.get(p.name, "")
            self.products.append(ProductDetail(p.name, desc, price, p.quantity))

    def addingItemsToCart(self, customer, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if quantity > product.stock:
                    print(f"Not enough stock for {product_name}")
                    return
                customer.cart.append({"product": product, "quantity": quantity})
                product.stock -= quantity
                print(f"Added {quantity} of {product_name} to {customer.name}'s cart.")
                return
        print(f"Product '{product_name}' not found.")

    def checkOut(self, customer):
        if not customer.cart:
            print("Cart is empty!")
            return
        total_price = sum(item["product"].price * item["quantity"] for item in customer.cart)
        order_id = str(uuid.uuid4())[:8]
        order_record = {
            "order_id": order_id,
            "items": customer.cart.copy(),
            "total": total_price
        }
        customer.past_orders.append(order_record)
        customer.cart.clear()
        print(f"Order {order_id} placed successfully! Total: {total_price} THB")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                print(f"\nOrder ID: {order_id}")
                for item in order["items"]:
                    p = item["product"]
                    print(f"- {p.name} x {item['quantity']} (฿{p.price})")
                print(f"Total: {order['total']} THB")
                return
        print("Order not found.")


class Product:
    def __init__(self, name, description, price, stock):
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock 

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = []
        self.past_orders = []

if __name__ == "__main__":

    shop = OnlineShop("La Baie Myrtille", "www.labaiemrtille.com")
    price_map = {
        "Cookie": 25,
        "Cupcake": 40,
        "Croissant": 60,
        "Muffin": 45,
        "Mille feuille": 55,
        "Apple pie": 65
    }
    desc_map = {
        "Cookie": "Sweet cookie",
        "Cupcake": "Delicious cupcake",
        "Croissant": "Buttery croissant",
        "Muffin": "Blueberry muffin",
        "Mille feuille": "French dessert",
        "Apple pie": "Classic apple pie"
    }

