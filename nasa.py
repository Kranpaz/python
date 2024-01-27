import json
list1 = []

with open('nasa.json') as nasa:                     # открываем json как nasa
    data = json.load(nasa)                          # записываем в data содержимое nasa
    for item in data:                               # берем каждую строку в data
        name = item['name']                         # в переменную name записываем строки из data
        if 'mass' in item:                          # проверка на пустые mass в строках
            for mass in item['mass']:
                mass = float(item['mass'])
        else: mass = 0                              # если пустые пишем в переменную 0

        str = name, mass                            # формируем строку списка
        list1.append(list(str))                     # добавляем строку в список

list1 = list(filter(lambda x: x[1] !=0, list1))     # убираем строки с нулевыми массами

list1.sort(key=lambda x: x[1])                      # сортируем новый список

list_min = list1[0], list1[1], list1[2]             # составляем список минимумов масс

print('\nТри самых лёгких метеорита:')
for x in list_min:
    print(x[0], x[1])

list_max = list1[-1], list1[-2], list1[-3]          # составляем список максимумов масс

print('\nТри самых тяжёлых метеорита:')
for x in list_max:
    print(x[0], x[1])