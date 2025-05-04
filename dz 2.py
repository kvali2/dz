def numbers():
    numbers = list(range(1, 20))
    return [x ** 2 for x in numbers]
list = numbers()
print("Квадрат чисел від 1 до 20")
print(list)