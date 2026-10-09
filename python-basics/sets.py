#№1 — создать множество
numbers = {1, 2, 3, 4, 5}
print(type(numbers))
#№2 — повторения
numbers = {1, 2, 3, 2, 4, 1, 5, 3}
print(numbers)
#№3 — список → множество
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
numbers = set(numbers)
print(numbers)
#№4 — уникальные имена
names = ["Alex", "John", "Alex", "Mike", "John", "Sam"]
names = set(names)
for name in names:
    print(name)
#№5 — добавить элемент
names = {"Alex", "John", "Mike"}
names.add("Sam")
print(names)
#№6 — удалить элемент
names = {"Alex", "John", "Mike", "Sam"}
names.remove("Mike")
names.discard("Mike")
print(names)
#№7 — проверка наличия
users = {"Alex", "John", "Mike", "Sam"}
name = input("Введите имя: ")

if name in users:
    print("Пользователь найден")
else:
    print("Пользователь не найден")

#🔥 №8 — количество уникальных пользователей
users = [
    "Alex",
    "John",
    "Alex",
    "Mike",
    "John",
    "Sam",
    "Mike",
    "Alex"
]
count = 0
users=set(users)
for name in users:
    count+=1
print(count)

#🔥 №9 — два множества
python_students = {"Alex", "John", "Mike", "Sam"}
java_students = {"John", "Mike", "Bob", "Tom"}
print(*python_students & java_students,sep= "\n")

#🔥 №10 — контрольная
shop1 = {"Apple", "Samsung", "Xiaomi", "Google"}
shop2 = {"Apple", "Xiaomi", "Huawei", "Google"}
shop1.update(shop2)
print(*shop1,sep="\n")