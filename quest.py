def act1():
    print("Ты лежишь на диване. Вдруг слышишь странный звук на кухне")
    answer = input("Что делать? 1 - пойти посмотреть, 2 - спрятаться, 3 - ничего не делать: ")
    if answer == "1":
        print("На кухне летает ворона. Как она сюда попала? ")
        return "1"
    elif answer == "2":
        print("Вы спрятались под кровать. Тут чьи-то ноги подобрались к кровати... ")
        return "2"
    elif answer == "3":
        print("Вы закрыли глаза, наслаждаясь музыкой в наушниках. Больше вы их не открывали. Конец ")
        exit()
    else:
        print("Так нельзя. Вы умерли")
        exit()

def act2(action):
    if action == "1":
        print("Ворона уронила люстру. ")
        answer = input("Шугнуть ворону? (да/нет): ")
    elif action == "2":
        print("Вы затаили дыхание. Это явно был кто-то незнакомый")
        answer = input("Позвонить по телефону?(да/нет) ")
    else:
        print("Такого варианта нет. Ты умер")
        exit()
    return answer

def act3(action, yes_or_no):
    if action == "1":
        if yes_or_no == "да":
            print("Вы накинулись с криком на ворону и буквально вытолкали ее в окно.")
            print("Что за наглые животные? С этими мыслями вы вернулись в кровать и сладко уснули")
        else:
            print("Ворона на ваших глазах выросла до размеров человека и превратилось в нечто страшное и бесформенное")
            print('Это существо потянулось к вам... И вы умерли.')
    elif action == "2":
        if yes_or_no == "да":
            print("Вы решили позвонить. Набрав номер мамы, вы поставили громкость на минимум, но незнакомец не издавал никаких звуков")
            print("Звонок был сброшен, а буквально через мгновение вы увидели, что вам перезванивают")
            print("Вибрация выдала вас! Черное бесформенное существо оказалось на уровне ваших глаз")
            print("Это было последнее, что вы увидели")
        else:
            print("Вы играли в Роблокс под кроватью до прихода родителей")

action = act1()
yes_or_no = act2(action)
end = act3(action, yes_or_no)

        

    
    
    