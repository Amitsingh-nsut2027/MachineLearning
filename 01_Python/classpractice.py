class product:
    count = 0

    def __init__(self , name, price):
        self.name = name
        self.price= price
        product.count +=1

    def get_info(self):
        print(f"the product is {self.name} is price of {self.price} Rs")

        
    @classmethod
    def get_count(cls):
        print(f"thr total no of objects is = {cls.count}")




p1 = product("car", 32)
p2 = product("bike", 10)
p3 = product("shampoo", 34)

p1.get_info()    
product.get_count()    
