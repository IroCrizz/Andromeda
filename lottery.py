import random


secret_number = random.randint(1, 10)
my_number = input("Введите ваше число от 1 до 10: ")# -> строка
my_number = int(my_number) # ->  число
if my_number == secret_number:
    print(f"Ты угадал!")
else:
    print(f"Победитель лотереи: {secret_number}")
    print(f"Ваше число: {my_number}")