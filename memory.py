import random
import time
import os 

os.system("cls")
print("это игра мемори.тебе нужно открывать по два скрытых элемента списка.если там будут одинаковые слова - они остаются открытыми.цель открыть все слова")

animals = "медведь, лиса, кот, собака, корова, крокодил, заяц, тигр".split(", ")
animals += animals
random.shuffle(animals)
secret_words = ["🧮"]*len(animals)

counter = 0
while secret_words.count("🧮") > 0:
    counter += 1
    print(*secret_words)
    index = int(input('введите индекс карточки: ')) - 1
    secret_words[index] = animals[index]
    print(*secret_words)
    if counter == 2:
        counter = 0
        time.sleep(5)
        if secret_words[index] != secret_words[prev_index]:
            secret_words[index] = "🧮"
            secret_words[prev_index] = "🧮"
    elif counter == 1:
        prev_index = index
    os.system("cls")
print("Браво! Ты прошла игру")