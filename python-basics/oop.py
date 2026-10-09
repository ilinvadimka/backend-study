#№1 — первый класс
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
         
user1 = User("Vadim",18)
user2 = User("Alex",25)

print(user1.name,user1.age)
print(user2.name,user2.age)
#№2 — метод
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

user1 = User("Vadim",18)
user2 = User("Alex",25)

user1.introduce()
user2.introduce()
#№3 — изменение атрибута
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User("Vadim",18)
user.age = 19
print(user.name,user.age)

#№4 — метод с логикой
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
        
user1 = User("Vadim",18)
user2 = User("Roma",16)

print(user1.is_adult())
print(user2.is_adult())

#№5 — метод, изменяющий объект 🔥
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

user = BankAccount("Vadim",1000)
print(user.deposit(500)) 
#№6 — логика внутри класса 🔥
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            pass
        else:
            self.balance -= amount
        return self.balance
    def get_balance(self):
        return self.balance

user = BankAccount("Vadim",500)
print(user.deposit(100))
print(user.withdraw(700))
#№7 — финальная на сегодня 🧠
class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

product1 = Product('MacBook', 1500, 2)
product2 = Product('iPad',1000,4)
product3 = Product('iPhone',500,12)

print(product1.get_total()+product2.get_total()+product3.get_total())