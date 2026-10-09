#Следующая задача — несколько объектов одного класса
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity
    def increase_quantity(self,amount):
        self.quantity += amount
        return self.quantity 

products = [#тут я спросил у ии как такие списки делать и как работают, но не брал готовое в тольео смотрел по похожуму который он показал 
    Product('iPhone', 799, 24),
    Product('MacBook', 1299, 6),
    Product('iPad', 449, 12),
    Product('AirPods', 249, 36)
]
#1
print(products[0].name,products[0].get_total())
print(products[1].name,products[1].get_total())
print(products[2].name,products[2].get_total())
print(products[3].name,products[3].get_total())
#2
products[0].increase_quantity(10) 
#3
print(products[0].name,products[0].get_total()) 
#4
total = 0
for all in products:
    total += all.get_total()
print(total)