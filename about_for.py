# from turtle import *
# 
# for i in range(20):
#     for c in('red', 'yellow', 'blue', 'green'):
#         color(c)
#         forward(100)
#         left(60)
#     right(80)


film = ['такси1', 'такси2', 'интерстеллар', 'на гребне волны']
film[1] = 'такси3'
film.append('такси4')
film.pop(2)
for i, k in enumerate(film):
    print(f'{i+1}.{k}')
