#Задача 5 — свой модуль 🔥
import helpers
helpers.add
helpers.multiply

print(helpers.add(10, 5))
print(helpers.multiply(10, 5))

#Задача 6 — свой модуль + логика 🔥🔥
users =[
    {"name":"Vadim","age":18},
    {"name":"Denis","age":19},
    {"name":"Maxim","age":19},
    {"name":"Roma","age":16},
    {"name":"Danil","age":17}
    ]
adults = []
for user in users:
    if helpers.is_adult(user["age"]):
        adults.append(user['name'])
print(adults) #я короче когда решал у меня выходила не правильно и я думал дело в функции или не правильно что делаю в цикле с файлом ведь это новая тема а оказалось что дела в списке я просто сделал [{и тут все имена и возраст}]а не для каждого, а коазалось что я полностью правильно написал а только дело в списке

#Задача 7 — финальная 🧠
import utils
numbers = [10, 4, 25, 7, 18]
print(utils.find_max(numbers))
print(utils.find_min(numbers))
print(utils.calculate_average(numbers))
