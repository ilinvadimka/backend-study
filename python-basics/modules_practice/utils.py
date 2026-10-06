#Задача 7 — финальная 🧠
def find_max(numbers):
    max_num= numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_min(numbers):
    min_num= numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def calculate_average(numbers):
    summ = 0
    count = 0
    for user in numbers:
        summ += user
        count += 1
    return summ/count
