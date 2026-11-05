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

products = [
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

#Задача №2 — атрибуты экземпляра и класса
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.company = "TechCorp"

employees = [
    Employee('Vadim',103900),
    Employee('Roma',112654), 
    Employee('Dima',151000),
]

for employee in employees:
    company = "NewTech"
    employee.company = company
    print(employee.name,employee.salary,employee.company)
#Задача №3 — метод __str__
class Book:
    def __init__ (self,title,author,pages):
        self.title = title
        self.author = author
        self.pages =pages
    def __str__ (self):
        return(f"Книга: {self.title}, автор: {self.author}, страниц: {self.pages}")

book1 = Book('Python для начинающих','Иван',350)
book2 = Book('Python для продвинутых','Ваня',420)
book3 = Book('С++ для новичков','Алексей',380)

print(book1)
print(book2)
print(book3)
#Задача №4 — инкапсуляция
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        return self.__balance
    def get_balance(self):
        return self.__balance 

user = BankAccount('Vadim',1000)

print(user.deposit(200))
print(user.withdraw(500))

#Задача №5 — наследование
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):
    def speak(self):
        return "Гав"
class Cat(Animal):
    def speak(self):
        return "Мяу"

my_dog = Dog("Шарик")
my_cat = Cat("Мурка")
print(f"{my_dog.name} говорит: {my_dog.speak()}")
print(f"{my_cat.name} говорит: {my_cat.speak()}")

#Задача №6 — super() и полиморфизм
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "Животное издает звук"

class Dog(Animal):
    def speak(self):
        return "Гав"
class Cat(Animal):
    def speak(self):
        return "Мяу"

my_cat = Cat("Мурка")
print(f"{my_dog.name} говорит: {my_dog.speak()}")
print(f"{my_cat.name} говорит: {my_cat.speak()}")