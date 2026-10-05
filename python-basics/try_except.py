#🟢 №1 — неправильный ввод
try:
    number = int(input("Введите число: "))
    print(number)
except:
    print('Ошибка: нужно ввести число')
#🟢 №2 — деление
def divide(a, b):
    try:
        result = a / b
        return result
    except:
        return "На ноль делить нельзя!"
print(divide(10, 2))
print(divide(10, 0))
#🟢 №3 — конкретный тип ошибки
try:
    number = int(input("Введите число: "))
    print(number)
except ValueError:
    print("Пиши число")
#🟡 №4 — несколько ошибок
try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    print(a / b)
except ValueError:
    print('Пиши число!')
except ZeroDivisionError:
    print('Зачем тебе ноль!')
#🟡 №5 — функция + try / except
def get_number():
    try:
        number = int(input("Введите число: "))
        return number
    except ValueError:
        print("Ошибка")
        return None
get_number()
#🟡 №6 — файл + ошибка
def read_file(filename):
    try:
        with open(filename,'r',encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден")
#🟡 №7 — файл + return
def read_file(filename):
    try:
        with open(filename,'r',encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None
content = read_file("hello.txt")
print(content)
#🔴 №8 — практическая задача
def get_user_age(filename, name):
    try:
        with open(filename,'r',encoding='utf-8') as users:
            for user in users:
                parts = user.split(",")
                age = int(parts[1])
                names = parts[0] # parts[0] только это подскозал ии и все 
                if name == names:
                    return age
            else:
                return None
    except FileNotFoundError:
        return None
#🔥 №9 — контрольная
def safe_divide():
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        return number_1 / number_2
    except ValueError:
        return("Вводите число!")
    except ZeroDivisionError:
        return("На ноль делить нельзя!")