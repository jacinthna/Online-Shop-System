product_list = {}

def add_product(product_list, product_name, product_quantity):
    if product_name in product_list:
        product_list[product_name] += product_quantity
    else:
        product_list[product_name] = product_quantity

def show_product(product_list):
    for key in product_list.keys():
        print(key + " : " + str (product_list[key]))

add_product(product_list, "Cookie", 82)
add_product(product_list, "Cupcake", 65)
add_product(product_list, "Croissant ", 28) 
add_product(product_list, "Muffin", 77) 
add_product(product_list, "Mille feuille", 50) 
add_product(product_list, "Apple pie", 42) 

show_product(product_list)