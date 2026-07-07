class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity=quantity
        
    def get_total(self):
        return self.price * self.quantity
        
    
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total(self):
        return sum(product.get_total() for product in self.products)

    def apply_discount(self, discount):
        for product in self.products:
            product.apply_discount(discount)