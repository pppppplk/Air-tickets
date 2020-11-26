class Aircraft():
    def __init__(prog, spis):
        prog.spis = spis

    def spisok(prog):
        for t in range(len(prog.spis)):
            if 'Самолет' in prog.spis[t]:
                a, b, c, d, e, f, g, h, i, j, k, l, m = prog.spis[t]
                top = Plane(b, c, d, e, f, g, h, i, j, k, l, m)
                top.display_plane_info()
                if spis[0][4] == 'истребитель' or 'штурмовик' or 'бомбардировщик':
                    print('есть возможность поражения цели')
                else:
                    print('нет возможности')
            elif 'Вертолет' in prog.spis[t]:
                a, b, c, d, e, f, g, h, i, j = prog.spis[t]
                top = Helicopter(b, c, d, e, f, g, h, i, j)
                top.display_heli_info()

    def information(prog):
        for t in range(len(prog.spis)):
            if 'Самолет' in prog.spis[t]:
                a, b, c, d, e, f, g, h, i, j, k, l, m = prog.spis[t]
                print("Данные самолета:", b, c, d, e, f, g, h, i, j, k, l, m)
                print("....................................")
            elif 'Вертолет' in prog.spis[t]:
                a, b, c, d, e, f, g, h, i, j = prog.spis[t]
                print("Данные вертолета:", b, c, d, e, f, g, h, i, j)
                print("...................")


class Plane(Aircraft):
    def __init__(prog, name, price, speed, type_plane, type_armament, max_h, flight_alt, fuel_sup, max_fuel_sup,
                 fuel_con, manufacturer, owner):
        prog.name = name
        prog.price = price
        prog.speed = speed
        prog.type_plane = type_plane
        prog.type_armament = type_armament
        prog.max_h = max_h
        prog.flight_alt = flight_alt
        prog.fuel_sup = fuel_sup
        prog.max_fuel_sup = max_fuel_sup
        prog.fuel_con = fuel_con
        prog.manufacturer = manufacturer
        prog.owner = owner

    def display_plane_info(prog):
        time = (prog.fuel_sup * 100 / prog.fuel_con) / prog.speed
        l = prog.fuel_sup * 100 / prog.fuel_con
        print("***** Самолёт *****")
        print("Название:", prog.name, "\nЦена:", prog.price, "млн руб", "\nСкорость:", prog.speed, "км/ч",
              "\nТип самолёта:", prog.type_plane, "\nТип вооружения:", prog.type_armament, "\nМаксимальная высота:",
              prog.max_h, "м", "\nВысота полёта:", prog.flight_alt, "м", "\nЗапас топлива:", prog.fuel_sup, "л",
              "\nМаксимальный запас топлива:", prog.max_fuel_sup, "л", "\nРасход топлива:", prog.fuel_con, "л",
              "\nСтрана производитель:", prog.manufacturer, "\nСтрана потребитель:", prog.owner, "\nВремя полета:",
              time)
        l = prog.fuel_sup * 100 / prog.fuel_con
        n = int(input('Введите расстояние:'))
        if l < n:
            print('полет возможен')
        else:
            print('полет невозможен')


class Helicopter(Aircraft):
    def __init__(prog, name, price, num_cr_mem, num_scr, type_heli, flight_alt, location, manufacturer, owner):
        prog.name = name
        prog.price = price
        prog.num_cr_mem = num_cr_mem
        prog.num_scr = num_scr
        prog.type_heli = type_heli
        prog.flight_alt = flight_alt
        prog.location = location
        prog.manufacturer = manufacturer
        prog.owner = owner

    def display_heli_info(prog):
        print("***** Вертолет *****")
        print("Название:", prog.name, "\nЦена:", prog.price, "млн руб", "\nКол-во членов экипажа:", prog.num_cr_mem,
              "\nКол-во винтов:", prog.num_scr, "\nТип вертолета:", prog.type_heli, "\nВысота полёта:", prog.flight_alt,
              "м", "\nМестонахождение:", prog.location, "\nСтрана производитель:", prog.manufacturer,
              "\nСтрана потребитель:", prog.owner)
        weight = int(input('Введите массу груза:'))
        k = int(input("Введите кол-во полетов:"))
        v = weight / k
        if v == 1:
            spis[1][4] = 'транспортный'
            print("возможно")
        elif v > 1:
            v < k < weight
            print('возможно')
        else:
            print("невозможно")


p = Plane('СУ-30', 1.5, 2120, 'истребитель', 'воздух-земля', 500, 300, 100, 50, 10, 'Россия', 'Китай')
spis = [['Самолет', 'СУ-30', 1.5, 2120, 'истребитель', 'воздух-земля', 500, 300, 100, 50, 10, 'Россия', 'Китай'],
        ['Вертолет', 'МИ-28', 100, 3, 5, 'транспортный', 300, 'Китай', 'Россия', 'Китай']]
sp = Aircraft(spis)
sp.information()
sp.spisok()


class PVO():
    def __init__(pvo, s):
        pvo.s = s

    def pv_spisok(pvo):
        for t in range(len(pvo.s)):
            if 'Ракетные' in pvo.s[t]:
                a, b, c, d, e, f, g, h, i = pvo.s[t]
                top_ = Rocket(b, c, d, e, f, g, h, i)
                top_.display_rock_info()
            elif 'Зенитные' in pvo.s[t]:
                a, b, c, d, e, f, g = pvo.s[t]
                top_ = Anti_aircraft(b, c, d, e, f, g)
                top_.display_anti_info()
            elif 'Объекты поражения' in pvo.s[t]:
                a, b, c = pvo.s[t]
                top_ = Objects_defeat(b, c)
                top_.display_obj_info()

    def inform(pvo):
        for t in range(len(pvo.s)):
            if 'Ракетные' in pvo.s[t]:
                a, b, c, d, e, f, g, h, i = pvo.s[t]
                print("Ракетные:", b, c, d, e, f, g, h, i)
                print("....................................")
            elif 'Зенитные' in pvo.s[t]:
                a, b, c, d, e, f, g = pvo.s[t]
                print("Зенитные:", b, c, d, e, f, g)
                print("...................")
            elif 'Объекты поражения' in pvo.s[t]:
                a, b, c = pvo.s[t]
                print("Объекты поражения:", b, c)
                print("...................")


class Rocket(PVO):
    def __init__(pvo, name, range_, h_defeat, speed, num_miss, stat_mov, tr_speed, num_people):
        pvo.name = name
        pvo.range_ = range_
        pvo.h_defeat = h_defeat
        pvo.speed = speed
        pvo.num_miss = num_miss
        pvo.stat_mov = stat_mov
        pvo.tr_speed = tr_speed
        pvo.num_people = num_people

    def display_rock_info(pvo):
        print('///// Ракетные /////')
        print("Название:", pvo.name, "\nДальность:", pvo.range_, "\nВысота поражения:", pvo.h_defeat, "\nСкорость:",
              pvo.speed, "\nКол-во ракет:", pvo.num_miss, "\nСтационарное или перемещаемое:", pvo.stat_mov,
              "\nСкорость перемещения:", pvo.tr_speed, "\nКол-во людей:", pvo.num_people)

    def ddd(pvo, prog):
        if int(pvo.speed) > int(prog.speed):
            print('можно сбить ракетными')
        else:
            print('нельзя сбить ракетными')


r = Rocket('Звезда', 100, 230, 300, 4, 'стационарное', 300, 2)
r.ddd(p)


class Anti_aircraft(PVO):
    def __init__(pvo, name, height, num_shells, caliber, number_trunks, number_people):
        pvo.name = name
        pvo.height = height
        pvo.num_shells = num_shells
        pvo.caliber = caliber
        pvo.number_trunks = number_trunks
        pvo.number_people = number_people

    def display_anti_info(pvo):
        print("///// Зенитные /////")
        print("Название:", pvo.name, "\nВысота поражения:", pvo.height, "\nКол-во снарядов:", pvo.num_shells,
              "\nКалибр:", pvo.caliber, "\nКол-во стволов:", pvo.number_trunks, "\nКол-во людей:", pvo.number_people)

    def ddd_2(pvo, prog):
        if int(pvo.height) > int(prog.flight_alt):
            print('можно сбить зенитными')
        else:
            print('нельзя сбить зенитными')


an = Anti_aircraft('Победа', 100, 3, 60, 3, 4)
an.ddd_2(p)


class Objects_defeat(PVO):
    def __init__(pvo, name, types):
        pvo.name = name
        pvo.types = types

    def display_obj_info(pvo):
        print("///// Объекты поражения /////")
        print("Название:", pvo.name, "\nТип:", pvo.types)
        print(".............................")


s = [['Ракетные', 'Звезда', 100, 230, 300, 4, 'стационарное', 300, 2], ['Зенитные', 'Победа', 100, 3, 60, 3, 4],
     ['Объекты поражения', 'Луч', 'ядерный']]
sp_s = PVO(s)
sp_s.inform()
sp_s.pv_spisok()


