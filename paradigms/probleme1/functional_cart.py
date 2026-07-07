def get_total(product):
    return product["price"] * product["quantity"]

def apply_discount(product, discount):
    product["price"] *= (1 - discount)
    
def add_product(cart, product):
    cart.append(product)
    

def calculate_cart_total(cart):
    total = sum(get_total(product) for product in cart)
    if total > 50000:
        print("Cart value exceeds 50000. Applying a discount of 10%.")
        for product in cart:
            apply_discount(product, 0.1)
        total = sum(get_total(product) for product in cart)
    return total