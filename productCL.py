class _Food:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"[Food] <{self.name:10}: {self.price:7.2f}>"
class _Drink:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"[Drink] <{self.name:10}: {self.price:7.2f}>"
    
def createProduct(type, name ,price):
    if type == 'food':
        return _Food(name, price)
    elif type == 'drink':
        return _Drink(name , price )
    else: 
        raise TypeError("Only 'food' or 'drink' product can be fabricated ")
