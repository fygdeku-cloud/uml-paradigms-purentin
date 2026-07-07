cart=[
    {"name": "Apple", "price": 350, "quantity": 5},
    {"name": "Banana", "price": 175, "quantity": 10},
    {"name": "Orange", "price": 125, "quantity": 8},
    {"name": "Grapes", "price": 200, "quantity": 3},
    {"name": "Mango", "price": 175, "quantity": 6}
]
for item in cart:
    total_price = item["price"] * item["quantity"]
    print(item['name'],": ", total_price)

cart_total = sum(item["price"] * item["quantity"] for item in cart)

if cart_total > 50000:
    print("Cart value exceeds 50000. Applying a discount of 10%.")
    cart_total *= 0.9
    print("Total cart value:", cart_total)
else:
    print("Total cart value:", cart_total)