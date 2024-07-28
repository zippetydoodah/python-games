
class Shop:
    def __init__(self,location,name):
        self.location = location
        self.name = name
        self.products = []
    def addproduct(self,product):
        self.products.append(product)

    def __str__(self):
        return '%s: %s has %d products' % (self.location, self.name, len(self.products))

class Product:
    def __init__(self):
        self.price = None
        self.colour = None
        self.material = None

    def gettinginput(self):
        self.price = input("What is the price?")
        self.colour = input("what is the colour?")
        self.material = input("what is the material?")

shop = Shop("oxford","zachs store")

for i in range(4):
    product = Product()
    product.gettinginput()
    shop.addproduct(product)

print(shop)



        