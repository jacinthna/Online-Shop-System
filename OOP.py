class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Store:
    def __init__(self):
        self.__products = []

    def add_product(self, name, quantity):
        for product in self.__products:
            if product.name == name:
                product.quantity += quantity
                return
        self.__products.append(Product(name, quantity))

    def show_products(self):
        print("\nStore Product List:")
        if not self.__products:
            print("No products available.")
        else:
            for idx, product in enumerate(self.__products, start=1):
                print(f"{idx}. {product.name} - {product.quantity} units")

my_store = Store()                
my_store.add_product("Cookie", 82)
my_store.add_product("Cupcake", 65)
my_store.add_product("Croissant", 28) 
my_store.add_product("Muffin", 77) 
my_store.add_product("Mille feuille", 50) 
my_store.add_product("Apple pie", 42) 

my_store.show_products()