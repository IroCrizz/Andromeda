import random

print(f"Компьютер кидает кубик, твоя задача - угадать, сколько на нем выпадет точек")

points = 10


while points > 0:
    print(f'у вас {points} очков')
    secret_number = random.randint(1, 6)
    my_number = input("Введите ваше число от 1 до 6: ")# -> строка
    my_number = int(my_number) # ->  число
    bet = int(input('ваша ставка: '))
    if bet > points:
        print('так  нельзя, у вас столько нет')
        continue
    if my_number == secret_number:
        print(f"Ты угадала!")
        points += bet
        print(f"Ставка выиграна")
    else:
        points -= bet
        print(f"На кубике выпало: {secret_number}")
        print(f"Ставка проиграна")
    answer = input("хотите продолжить игру?? ")
    if answer == "нет":
        break
print(f"Ваш результат: {points} очков")