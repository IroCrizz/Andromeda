print('''приложения ТОП-FILMS!
меню команд:
1  - вывод списка топ-фильмов на экран
2 - добавить новый фильм в список
3 - удалить просмотренный фильм
4 - выйти из приложения''')

top_films = []

while True:
    command = input('выберите команду из меню >>> ')
    if command == '1':
        if len(top_films) == 0:
            print('список пока пуст!!')
        else:
            print('список фильмов:')
            for i, k in enumerate(top_films):
                print(f'{i+1}.{k}')
    elif command == '2':
        new_film = input('введи новый фильм >>> ')
        if new_film.lower() in top_films:
            print('такой фильм уже есть в списке!!')
            continue
        else:
            top_films.append(new_film.lower())
            print('фильм добавлен в список!!')
    elif command == '3':
        print('список фильмов:')
        for i, k in enumerate(top_films):
            print(f'{i+1}.{k}')
        number = int(input('выберите номер фильма, который посмотрели >>> '))
        top_films.pop(number-1)
        print('фильм удален из списка!!')
    elif command == '4':
        print('до новых встреч!!')
        break
    else:
        print('такой команды нет!!')