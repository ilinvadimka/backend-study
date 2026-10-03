#🟢 №1 — создать и записать
file = open('hello.txt','w')
file.write("Hello, Python!\n" 
"I am learning files.",)
file.close()
#🟢 №2 — прочитать файл
file = open('hello.txt','r')
print(file.read())
file.close()
#🟢 №3 — добавить информацию
file = open("hello.txt","a")
file.write("\nI want to become a backend developer.")
file.close()#на этом задании много гуглил
file = open("hello.txt","r")
print(file.read())
file.close()
#🟡 №4 — with open
with open("hello.txt","r") as file:#не понял почуму не работало загуглил понял что при with open нужен в конце as file:
    print(file.read())
#🟡 №5 — строки из файла
users = open('users.txt','w')
users.write("""Alex
John
Mike
Sam""")
with open('users.txt','r') as users:
    for user in users:
        print(user.strip())# на этом заднии много гуглил и спрашивал
#🟡 №6 — посчитать пользователей
with open("users.txt","r") as users:
    count = 0
    for user in users:
        count +=1
    print(count) #написал сам
#🟡 №7 — найти пользователя
def find_user(filename, name):
    with open('users.txt','r') as users:
        for user in users:
            if name == user.strip(): #написал сам но тольео из за .strip() не было правильно
                return True
        else:
            return False
print(find_user("users.txt", "Mike"))
print(find_user("users.txt", "David"))
#🔴 №8 — файл + список + функция
def get_adults(filename):
    with open('users.txt','w') as users:
        users.write("""Alex,25
John,17
Mike,30
Sam,16""")
    with open('users.txt','r') as users:
        adults = []
        for user in users:
            parts = user.split(",")
            age = int(parts[1]) #скажу честно ,тут мне помог ии а имнно age = int(parts[1])
            if age >= 18:
                adults.append(parts[0].strip()) # и тут тоже момог parts[0]с этим и даже не знаю вроде основу я сам написал но если бы не ии то она бы вообще не работало бы
        return (adults)
print(get_adults("users.txt"))
#🔥 №9 — запись результатов
def save_adults(input_file, output_file):
    with open('users.txt','w') as users:
        users.write("""Alex,25
John,17
Mike,30
Sam,16""")
    with open("users.txt",'r') as users:
        adults = []
        for user in users:
            parts = user.split(",")
            age = int(parts[1])
            if age >= 18:
                adults.append(user)

    with open('adults.txt','w') as out:
        for user in adults:
            out.write(user) #написал сам но ии cкfзал мне что я     return adults не туда вставил и что код может сломатся и я сам исправил это и замтил что нужно еще         for user in adults:
    return adults
print(*save_adults("users.txt",'adults.txt'))
#🧠 №10 — контрольная
def get_expensive_products(filename, min_price):
    with open("products.txt","w") as products:
        products.write("""iPhone,1000
Samsung,800
Xiaomi,500
MacBook,1500""")
    with open ("products.txt","r") as commodity:
        list_products = []
        for goods in commodity:
            parts = goods.split(",")
            price = int(parts[1])
            if price >= min_price:
                list_products.append(parts[0].strip())
        return list_products #это задание написал сам полностью
print(get_expensive_products("products.txt", 900))     

#Задание 1. Записать в файл
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет, файл!")
#Задание 2. Прочитать из файла
with open("hello.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
#Задание 3. Несколько строк
with open('list.txt','w',encoding="utf-8") as f:
    f.write("Первая строка\n")
    f.write("Вторая строка\n")
    f.write("Третья строка\n")
#Задание 4. Прочитать построчно
with open("list.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
#Задание 5. Дописать в конец
with open('list.txt','a',encoding="utf-8") as f:
    f.write('Четвертая строка\n')
#Задание 6. Цикл и файл
with open("numbers.txt", "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f'{str(i)}\n')
#Задание 7. Ввод от пользователя
name = input("Ваше имя: ")
with open("name.txt", "w", encoding="utf-8") as f:
    f.write(f"Меня зовут {name}")
with open("name.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(text)
#Задание 8. Сумма чисел из файла
total = 0
with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        total += int(line)
print(total)
#Задание 9. Мини-заметки
text = input("Ваш текст: ")
with open('notes.txt','a',encoding="utf-8") as f:
    f.write(f"{text}\n")
#Задание 10. Посчитать заметки
count = 0
with open('notes.txt','r',encoding="utf-8") as f:
    for line in f:
        count += 1
print(count)
#Задание 11. Когда файла нет
try:
    with open("nothing.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден")