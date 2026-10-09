#Задание 1 — лёгкое
person = {"name":"Вадим",
          "age":18,
          "city":"Cheboksary"}
for item in person.values():
    print(item)

#Задание 2 — изменениperson = {
person = {
    "name": "Alex",
    "age": 20,
    "city": "Amsterdam"
}
person["age"] = 21
person["job"] = "Developer"
for new in person.items():
    print(new)

#Задание 3 — .get()
user = {
    "name": "Alex",
    "age": 20
}
for i in user.keys():
    print(i)
print(user.get("email"))
print(user.get("phone"))

#Задание 4 — перебор
user = {
    "name": "Alex",
    "age": 20,
    "city": "Amsterdam",
    "job": "Developer"
}
for items in user.items():
    print(*items)

#Задание 5 — подсчёт
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {
    "apple" : words.count("apple"),
    "banana" : words.count("banana"),
    "orange" : words.count("orange")
}
for key, value in counts.items():
    print(key, value)

#Задание 6 — пользователи
users = {
    "alex": {
        "age": 20,
        "city": "Amsterdam"
    },
    "max": {
        "age": 25,
        "city": "Berlin"
    },
    "john": {
        "age": 30,
        "city": "London"
    }
}
print(users["alex"])

#Задание 7 — посложнее
product = {
    "name": "Laptop",
    "price": 1200,
    "quantity": 3
}
product["total"] = product["price"] * product["quantity"]

for key, value in product.items():
    print(key, value)

#Задание 8 — уже ближе к реальному программированию
users = [
    {"name": "Alex", "age": 20},
    {"name": "Max", "age": 17},
    {"name": "John", "age": 25},
    {"name": "Sam", "age": 16}
]
for user in users:
    if user["age"] >= 18:
        print(user["name"],user["age"])

#Задание 9 — поиск пользователя
users = [
    {"name": "Alex", "age": 20},
    {"name": "Max", "age": 17},
    {"name": "John", "age": 25},
    {"name": "Sam", "age": 16}
]
for user in users:
    if user["age"] >= 18:
        print(user["name"])

#Задание 10 — поиск по городу
users = [
    {"name": "Alex", "age": 20, "city": "Amsterdam"},
    {"name": "Max", "age": 17, "city": "Berlin"},
    {"name": "John", "age": 25, "city": "Amsterdam"},
    {"name": "Sam", "age": 16, "city": "London"}
]
for user in users:
    if user["city"] == "Amsterdam":
        print(user["name"])

#Задание 11 — немного сложнее
users = [
    {"name": "Alex", "age": 20, "city": "Amsterdam"},
    {"name": "Max", "age": 17, "city": "Berlin"},
    {"name": "John", "age": 25, "city": "Amsterdam"},
    {"name": "Sam", "age": 16, "city": "London"}
]
for user in users:
    if user["city"] == "Amsterdam" and user["age"] >= 18:
        print(user["name"],user["age"])

#Задание 12 — уже ближе к реальной задаче
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300}
]
for thing in products:
    if thing["price"] >= 100:
        print(thing["name"],thing["price"])

#Задание 13 — подсчёт
users = [
    {"name": "Alex", "age": 20},
    {"name": "Max", "age": 17},
    {"name": "John", "age": 25},
    {"name": "Sam", "age": 16}
]
count = 0
for user in users:
    if user["age"] >= 18:
        count +=1
print(count)

#Задание 14 — сумма
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300}
]
total = 0
for user in products:
    total += user["price"]
print(total)

#Задание 15 — сумма только подходящих
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300}
]
total =0
for user in products:
    if user["price"] >= 100:
        total +=user["price"]
print(total)

#Задание 16 — доделать самостоятельно
users = [
    {"name": "Alex", "age": 20, "city": "Amsterdam"},
    {"name": "Max", "age": 17, "city": "Berlin"},
    {"name": "John", "age": 25, "city": "Amsterdam"},
    {"name": "Sam", "age": 16, "city": "London"},
    {"name": "Mike", "age": 30, "city": "Berlin"}
]
citis = {}

for user in users:
    citis[user["city"]] = 0
for user in users:
    city = user["city"]
    if user["age"] >= 18:
        if city in citis:
            citis[city] += 1
        else:
            citis[city] = 1
for city in citis:
    print(city, citis[city])

#Задание 17 — найти самого взрослого
users = [
    {"name": "Alex", "age": 20},
    {"name": "Max", "age": 17},
    {"name": "John", "age": 25},
    {"name": "Sam", "age": 16},
    {"name": "Mike", "age": 30}
]
ages = {}

for user in users:
    ages[user["age"]] = 0
for user in users:
    oldest = user["age"]
    if user["age"] < oldest:
        oldest = user
print(user["name"],oldest)

#Задание 18 — найти товар
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300}
]
names = input("Введите товар: ")

for user in products:
    choice = user["name"]
    if choice == names:
        print(choice,user["price"])
else:                         
    print("Товар не найден")
#Задание 19 — изменение данных
user = {
    "name": "Alex",
    "age": 20,
    "city": "Amsterdam"
}
new_city = input("Введите новый город: ")

user["city"] = new_city
print(user)  

#🔥Задание 20 — финальное
users = [
    {"name": "Alex", "age": 20, "city": "Amsterdam"},
    {"name": "Max", "age": 17, "city": "Berlin"},
    {"name": "John", "age": 25, "city": "Amsterdam"},
    {"name": "Sam", "age": 16, "city": "London"},
    {"name": "Mike", "age": 30, "city": "Berlin"}
]
citys = {

}
for city in users:
    citys[city["city"]] = 0

for user in users:
    city = user["city"]
    if user["age"] >= 18:
        city = user["city"]
        if city in citys:
            citys[city] += 1
        else:
            citys[city] = 1
for city in citys:
    print(city, citys[city])

#№21 — самый взрослый
users = [
    {"name": "Alex", "age": 20},
    {"name": "Max", "age": 17},
    {"name": "John", "age": 25},
    {"name": "Sam", "age": 16},
    {"name": "Mike", "age": 30}
] 

first_user = users[0]  
max_value = first_user["age"]
max_user = first_user

for user in users:
    if user["age"] > max_value:
            max_value = user["age"]
            max_user = user
for key, value in max_user.items():
    print(value, end=" ")
print() 
#№22 — самый дешёвый товар
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 80},
    {"name": "Monitor", "price": 300}
]

first_products = products[0]  
min_value = first_products["price"]
min_user = first_products

for user in products:
    if user["price"] < min_value:
        min_value = user["price"]
        min_user = user

for key, value in min_user.items():
    print(value, end=" ")
print()   

#№23 — контрольная
products = [
    {"name": "Laptop", "price": 1200, "quantity": 2},
    {"name": "Mouse", "price": 25, "quantity": 10},
    {"name": "Keyboard", "price": 80, "quantity": 5},
    {"name": "Monitor", "price": 300, "quantity": 3}
]
first_products = products[0] 
max_value = first_products["price"] * first_products["quantity"]
max_name = first_products["name"]

for user in products:
    if user["price"]* user["quantity"]  >  max_value:
        max_value = user["price"] * user["quantity"]
        max_name  = user["name"]
print(max_name, max_value)