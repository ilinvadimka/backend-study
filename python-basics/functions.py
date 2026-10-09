#№1 — простая функция
def hello():
    print("Hello, World!")
hello()
hello()

#№2 — функция с параметром
def greet(name):
    print(f"Привет, {name}!")
greet("Alex")
greet("John")

#№3 — сложение
def add(a,b):
    return a+b
result = add(5, 3)
print(result)
#№4 — квадрат числа
def square(number):
    return number**2
print(square(5))
print(square(10))
#№5 — проверка возраста
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
print(is_adult(20))
print(is_adult(15))

#🔥 №6 — максимум из двух чисел
def max_number(a, b):
    if a > b:
        return(a)
    else:
        return(b)  
print(max_number(10, 5))
print(max_number(3, 8))

#🔥 №7 — количество элементов
def count_users(users):
    count =0
    for _ in users:
        count+=1
    return(count)
users = ["Alex", "John", "Mike", "Sam"]
print(count_users(users))

#🔥 №8 — взрослые пользователи
users = [
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 17},
    {"name": "Mike", "age": 30},
    {"name": "Sam", "age": 16},
]
def get_adults(users):
    my_list = []
    for user in users:
        if user["age"] >= 18:
            my_list.append(user["name"])
    return my_list
print(get_adults(users)) 

#🔥 №9 — поиск пользователя
users = [
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 17},
    {"name": "Mike", "age": 30},
    {"name": "Sam", "age": 16},
]
def find_user(users, name):
    for user in users:
        if name == user["name"]:
            return user
    else:
        return None
user = find_user(users, "Mike")
print(user)

#🧠 №10 — контрольная
products = [
    {"name": "iPhone", "price": 1000},
    {"name": "Samsung", "price": 800},
    {"name": "Xiaomi", "price": 500},
    {"name": "MacBook", "price": 1500},
]

def find_expensive_products(products, price):
    my_list = []
    for user in products:
        if user["price"] >= price:
            my_list.append(user["name"])
    return my_list
print(result) 

#🔹 №11 — функция с двумя параметрами
def multiply(a, b):
    return a * b
multiply(5, 4)
multiply(7, 3)

#🔹 №12 — положительное число
number = int(input("Введите число: "))
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
is_positive(number)  

#🔹 №13 — сумма списка
def calculate_sum(numbers):
    result = 0
    for dig in numbers:
        result += dig
    return result
calculate_sum([1, 2, 3, 4, 5])

#🔥 №14 — среднее значение
def average(numbers):
    result = 0
    count = 0
    for dig in numbers:
        result += dig
        count +=1
    return result/count
average([10, 20, 30])

#🔥 №15 — найти минимальное число
def find_min(numbers):
    min_dig = numbers[0]
    for digit in numbers:
        if digit < min_dig:
            min_dig = digit
    return min_dig
find_min([5, 2, 8, 1, 9])

#🔥 №16 — фильтр чисел
def get_even_numbers(numbers):
    my_list = []
    for num in numbers:
        if num % 2 == 0:
            my_list.append(num)
    return my_list
get_even_numbers([1, 2, 3, 4, 5, 6])

#🔥 №17 — функция поиска пользователя
users = [
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 17},
    {"name": "Mike", "age": 30},
    {"name": "Sam", "age": 16},
]
def get_user_age(users, name):
    for user in users:
        if name == user["name"]:
            return user["age"]
    else:
        return None
get_user_age(users, "Mike")

#🔥 №18 — количество совершеннолетних
users = [
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 17},
    {"name": "Mike", "age": 30},
    {"name": "Sam", "age": 16},
]
def count_adults(users):
    count = 0
    for user in users:
        if user["age"] >= 18:
            count+=1
    return count
count_adults(users)

#🧠 №19 — функция внутри функции
users = [
    {"name": "Alex", "age": 25},
    {"name": "John", "age": 17},
    {"name": "Mike", "age": 30},
    {"name": "Sam", "age": 16},
]
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
    
def get_adults(users):
    my_list = []
    for user in users:
        if is_adult(user["age"]):
            my_list.append(user["name"])
    return my_list
print(get_adults(users)) 

#🧠 №20 — общая стоимость товаров
products = [
    {"name": "iPhone", "price": 1000, "quantity": 3},
    {"name": "Samsung", "price": 800, "quantity": 5},
    {"name": "Xiaomi", "price": 500, "quantity": 10},
    {"name": "MacBook", "price": 1500, "quantity": 2},
]

def get_total_value(products):
    total = 0
    for user in products:
        first_products = user["price"]*user['quantity']
        total+=first_products
    return total#я в задание вникнул и решил за 5 минут
print(get_total_value(products))

#№21 — return vs print
def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"
print(get_full_name("Vadim","Ilin"))

#№22 — значение по умолчанию
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"
print(greet("Alex"))

#№23 — None
products = [
    {"name": "iPhone", "price": 1000},
    {"name": "Samsung", "price": 800},
    {"name": "Xiaomi", "price": 500}
]
def find_product(products, name):
    for user in products:
        if name == user["name"]:
            return user
    else:
        return None
print(find_product(products,"iPhone"))

#№24 — функция вызывает функцию
users = [
    {"name": "Alex", "age": 25},
    {"name": "Mike", "age": 30}
]
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
def get_adult_users(users):
    my_list = []
    for user in users:
        if is_adult(user["age"]):
            my_list.append(user)
    return my_list
print(get_adult_users(users))

#№25 — несколько значений через return
def get_min_max(numbers):
    max_val = numbers[0]
    min_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return min_val, max_val
result = get_min_max([5, 2, 8, 1, 9])
print(result)

#№26 — небольшая практическая задача
users = [
    {"name": "Alex", "age": 25, "city": "Berlin"},
    {"name": "John", "age": 17, "city": "Berlin"},
    {"name": "Mike", "age": 30, "city": "Munich"},
    {"name": "Sam", "age": 16, "city": "Berlin"},
]

def get_users_by_city(users, city):
    citys = []
    for user in users:
        if user["city"] == city:
            citys.append(user)
    return citys
print(get_users_by_city(users, "Berlin"))