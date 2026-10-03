#🔥 №1 — уникальные города
users = [
    {"name": "Alex", "city": "Berlin"},
    {"name": "John", "city": "Amsterdam"},
    {"name": "Mike", "city": "Berlin"},
    {"name": "Sam", "city": "London"},
    {"name": "Bob", "city": "Amsterdam"},
]
cityse = set(user["city"] for user in users) #вот cityse мне помог ии , но я дого сидел и писал cityse = set(users["city"] сам но все равно выдавало ошибки ,но оказывается там вообще через цикл надо я бы до этого бы не додумался как это бы сдеалть
for items in cityse:
    print(items)

#🔥 №2 — количество уникальных городов
users = [
    {"name": "Alex", "city": "Berlin"},
    {"name": "John", "city": "Amsterdam"},
    {"name": "Mike", "city": "Berlin"},
    {"name": "Sam", "city": "London"},
    {"name": "Bob", "city": "Amsterdam"},
]
count = 0
cityse = set(user["city"] for user in users)
for items in cityse:
    count+=1
print(count)

#🔥 №3 — пользователи из города
users = [
    {"name": "Alex", "city": "Berlin"},
    {"name": "John", "city": "Amsterdam"},
    {"name": "Mike", "city": "Berlin"},
    {"name": "Sam", "city": "London"},
    {"name": "Bob", "city": "Amsterdam"},
]
town = input("Введите город: ")
cityse = set(user["city"] for user in users)

if town not in cityse:
    print("Пользователи не найдены")
#в целом я сам написал этот код, но каждый раз с правильным ответом, выходил Пользователи не найдены , я над этим заданием долго сидел по разному пробовал но у меня не выходило и я спросилл у ии и он помог мне, сказав сделать нооборот ,то есть сперва работать с если Эпользователя не найдно", а потом искать челов
else:
    for user in users:
        if town == user["city"]:
            print(user["name"])

#🔥 №4 — уникальные товары
products = [
    {"name": "iPhone", "price": 1000},
    {"name": "Samsung", "price": 800},
    {"name": "iPhone", "price": 1000},
    {"name": "Xiaomi", "price": 500},
    {"name": "Samsung", "price": 800},
]
name_products = set(goods["name"] for goods in products)
print(*name_products,sep = "\n")

#🔥 №5 — кто покупал товар
orders = [
    {"user": "Alex", "product": "iPhone"},
    {"user": "John", "product": "Samsung"},
    {"user": "Mike", "product": "iPhone"},
    {"user": "Sam", "product": "Xiaomi"},
    {"user": "Bob", "product": "iPhone"},
]
products = input("Введите товар: ")
for user in orders:
    if products == user["product"]:
        print(user["user"])

#🔥 №6 — какие товары покупал пользователь
orders = [
    {"user": "Alex", "product": "iPhone"},
    {"user": "John", "product": "Samsung"},
    {"user": "Mike", "product": "iPhone"},
    {"user": "Sam", "product": "Xiaomi"},
    {"user": "Bob", "product": "iPhone"},
]
name = input("Введите имя: ")
for user in orders:
    if name == user["user"]:
        print(user["product"])

#🔥 №7 — уникальные покупатели 🔥
orders = [
    {"user": "Alex", "product": "iPhone"},
    {"user": "John", "product": "Samsung"},
    {"user": "Alex", "product": "MacBook"},
    {"user": "Mike", "product": "iPhone"},
    {"user": "John", "product": "iPhone"},
    {"user": "Alex", "product": "AirPods"},
]
count = 0
cityse = set(user["user"] for user in orders)
for items in cityse:
    count+=1

for items in cityse:
    print(items)
print()
print("Количество: ",count)

#🔥 №8 — общие покупатели
shop1 = {"Alex", "John", "Mike", "Sam"}
shop2 = {"John", "Mike", "Bob", "Tom"}
shop1 = shop1 & shop2

for items in shop1:
    print(items)

#🔥 №9 — контрольная 🧠
users = [
    {"name": "Alex", "age": 25, "city": "Berlin"},
    {"name": "John", "age": 17, "city": "Berlin"},
    {"name": "Mike", "age": 30, "city": "London"},
    {"name": "Sam", "age": 16, "city": "London"},
    {"name": "Bob", "age": 22, "city": "Berlin"},
    {"name": "Tom", "age": 19, "city": "Paris"},
]
citys = set()
for user in users:
    if user["age"] >= 18:
        citys.add(user["city"])
for i in citys:    # долго сидел но сам без ии , много думал сидел менял структур и гуглин но все таки смог решить и понял
    print(i)

#🔥 №10 — большая контрольная
users = [
    {"name": "Alex", "city": "Berlin", "skills": ["Python", "SQL"]},
    {"name": "John", "city": "London", "skills": ["Java", "SQL"]},
    {"name": "Mike", "city": "Berlin", "skills": ["Python", "Docker"]},
    {"name": "Sam", "city": "Paris", "skills": ["Python", "SQL"]},
]
for user in users:
    if "Python" in user["skills"]:
        print(user["name"]) # это задание заняло у меня меньше 5 минут очень легкое