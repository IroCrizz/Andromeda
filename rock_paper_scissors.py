import random

print("Это игра Камень-ножницы-бумага. Попробуй победи компьютер!")
variants = ["камень", "ножницы", "бумага"]
tries = 3
my_points = 0
comp_points = 0
while tries > 0:
    print(f"Осталось попыток: {tries}")
    tries -= 1

    comp = random.choice(variants)
    player = input("Введи, что будешь ставить (камень, ножницы или бумага):")
    print(f"Компьютер выбрал {comp}")

    player_win = False
    comp_win = False

    if player == "камень" and comp == "бумага":
        comp_win = True
    elif player == "камень" and comp == "ножницы":
        player_win = True
    elif player == "камень" and comp == "камень":
        pass

    elif player == "ножницы" and comp == "бумага":
        player_win = True
    elif player == "ножницы" and comp == "ножницы":
        pass
    elif player == "ножницы" and comp == "камень":
        comp_win = True
        
    elif player == "бумага" and comp == "бумага":
        pass
    elif player == "бумага" and comp == "ножницы":
        comp_win = True
    elif player == "бумага" and comp == "камень":
        player_win = True

    if player_win:
        print("Ты победил!")
        my_points +=1
    elif comp_win:
        print("Компьютер победил!")
        comp_points +=1
    else:
        print("Ничья!")
# происходит после цикла       
print(f"Итоги: твоих побед - {my_points}, компьютера - {comp_points}")