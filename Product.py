class product:
    inventory = []
    product_counter = 0

    def __init__ (self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def addProduct(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        newProduct = product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(newProduct)
        return "Product added successfully"
    
    @classmethod
    def updateProduct(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found."

    @classmethod
    def deleteProduct(cls, product_id):
            for product in cls.inventory:
                if product.product_id == product_id:
                    cls.inventory.remove(product)
                return "Product deleted successfully"
            return "Product Not Found"

class order:
    def __init__ (self, order_id, product_id, quantity, customer_info = None):
            self.order_id = order_id
            self.product_id = product_id
            self.quantity = quantity
            self.customer_info = customer_info
     
    def place_order(self):
        for product in product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    return f"Order placed successfully. Order ID:", {self.order_id}
                else:
                    return "Insufficient stock to place order"
     
p1 = product.addProduct("Laptop", "Electronics", 50, 1000, "Supplier A")
product.addProduct("T-Shirt", "Clothing", 100, 25, "Supplier B")
p2 = product.updateProduct(1, quantity=45, price=950)
p3 = product.deleteProduct(2)
p4 = order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")

print(p1)
print(p2)
print(p3)
print(p4)
