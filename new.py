print(93)
print(94 + 6 - 3 * 9)
print("мне без разницы")
print("не знаю" + " я")
name = input("Введи имя: ").capitalize()
surname = input("Введи фамилию: ").capitalize()
print("Вы ввели " + name + " " +surname )

import math


start = 1
end = 1000
tries = math.log2(end - start)
tries = math.ceil(tries)
print(f"Загадай число от {start} до {end}. Я отгадаю меньше, чем  за {tries} попыток")
while tries > 0:
    tries -= 1
    print(f"Осталось попыток: {tries}")
    comp_number = (start+end)//2
    answer = input(f"{name} {surname}, {comp_number} - это ваше число?(больше, меньше, да) ")
    if answer == "да":
        print(f"Вы угадали! {name} - молодец!")
        break 
    elif answer == "больше":
        start = comp_number + 1
        print(f"Понял, буду искать от {start} до {end}")
    elif answer == "меньше":
        end = comp_number - 1
        print(f"Понял, буду искать от {start} до {end}")

