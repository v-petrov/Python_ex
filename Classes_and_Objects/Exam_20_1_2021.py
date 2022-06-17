class Products:
    def __init__(self, product, code, price, quantity):
        self.product = product
        self.code = code
        self.price = price
        self.quantity = quantity
    
class Cart:
    def __init__(self):
        self.cart = list()
    
    def add_product(self, product, code, price, quantity):
        new_product = Products(product = product, code = code, price = price, quantity = quantity)
        self.cart.append(new_product)
    
    def price(self, price_for_delivery):
        for pr in self.cart:
            total_price  = pr.price*pr.quantity
            tax_price = total_price +  total_price * 0.2
            final_price = tax_price + price_for_delivery
            with open('price_file1.txt', 'a') as file:
                file.write(f'Final price of the {pr.product}: {round(final_price, 2)}\n')

p1 = Cart()
p1.add_product('A', 1234, 20.00, 5)
p1.add_product('B', 4321, 25.00, 6)
p1.add_product('C', 4532, 16.99, 2)
p1.add_product('D', 7593, 77.99, 6)
p1.add_product('E', 9362, 12.50, 7)
p1.add_product('F', 1267, 35.99, 12)
p1.price(2.00)