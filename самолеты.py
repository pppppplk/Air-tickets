
"""
Created on Thu Nov 28 12:11:08 2019

@author: liza
"""
import os
import random

print("Авиарейсы на декабрь 2019 года\n")

file = open('zadacha3.txt', mode='r')
for i in file:
    print(i)
file.close()

d = {}


def func3():
    file = open('5z.txt', mode='r')
    for line in file:
        key, *value = line.split()
        d[key] = value
    file.close()
    print(d)


func3()

t = {}


def func5():
    file = open('mest.txt', mode='r')
    for line in file:
        key, *value = line.split()
        t[key] = value
    file.close()
    print(t)


func5()

marshruti = []


def func1():
    global chosen_fl
    A = input("Введите точку отправления: ").title()
    B = input('Введите точку прибытия: ').title()
    chosen_fl = []
    for flight1, city1 in d.items():
        if len(chosen_fl) == 0:
            if city1[0] == A:
                if city1[1] != B:
                    for flight2, city2 in d.items():
                        if city2[0] == city1[1] and city2[1] == B:
                            marshruti.append([city1[0] + city1[1] + city2[0] + city2[1], f' {flight1} -> {flight2} '])
                            for fl in d:
                                if d[fl][0] == A and d[fl][1] == city1[1]:
                                    chosen_fl.append(fl)
                                if d[fl][0] == city2[0] and d[fl][1] == B:
                                    chosen_fl.append(fl)
                else:
                    marshruti.append([city1[0] + city1[1], f'{flight1}'])
                    for fl in d:
                        if d[fl][0] == A and d[fl][1] == B:
                            chosen_fl.append(fl)


func1()

s = {}


def create():
    s[0] = ['Данные о рейсе']
    s[1] = ['ФИО пассажира ']
    s[2] = ['Место']
    s[3] = ['Дата отправления']
    s[4] = ['Серия и номер паспорта']


create()


def func2():
    file = input("Сохранить билет, как: ")
    my_file = open(file + '.txt', mode='w')
    for r in s.items():
        if s[0]:
            dan = input("\n" + "Введите данные о рейсе: " + '\n')
            my_file.write('........................' + '\n' + 'Номер билета: ' + random.choice(
                'abcdefghijklmnopqrstuvwxyz') + str(random.randrange(1, 1000)) + '\n' + 'Данные о рейсе: ' + dan + '\n')
        if s[1]:
            fio = input("Введите ФИО:")
            my_file.write('ФИО: ' + fio + '\n')

        if s[2]:
            for i in range(len(chosen_fl)):
                while True:
                    mes = str(input("Ваше место на рейсе " + chosen_fl[i] + ":"))
                    c = 0
                    for h in range(len(t[chosen_fl[i]])):
                        if mes == t[chosen_fl[i]][h]:
                            print('Данное место занято')
                            c += 1
                    if c == 0:
                        print('место свободно и было забронировано для вас!')
                        my_file.write('Место: ' + mes + '\n')
                        break
        if s[3]:
            date = input("Введите дату отправления:")
            my_file.write('Дата отправления: ' + date + '\n')

        if s[4]:
            s_n = input("Введите серию и номер паспорта:")
            my_file.write('Серия и номер паспорта: ' + s_n + '\n')
            print("...................................")

            return (dan, fio, mes, date, s_n)
    my_file.close()


func2()

print("Стоимость билета 20.000 рублей\n")


def choise():
    t = None
    print('\n"1", Читать  информацию о билете')
    print('\n"2", Возврат билета')
    t = int(input('Введите номер команды, которую хотите выполнить:'))
    return t


number = choise()
if number == 1:
    filename = input('Название файла, который хотите прочитать:')
    my_file = open(filename, mode='r')
    print(my_file.read())
    my_file.close()
elif number == 2:
    filename = input('Название файла, который хотите удалить:')
    try:
        os.remove(filename)
        print('Файл удалён!')
    except (OSError, NameError):
        print("\n Файл не существует")

total = marshruti[0]
for k in marshruti:
    if k[0] < total[0]:
        total = k

if total[0] == 0:
    print('Нет маршрута')
else:
    print(f'Маршрут с 1 пересадкой: {total[1]}')
