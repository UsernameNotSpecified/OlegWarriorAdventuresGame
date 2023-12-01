from random import *

health = 10
chance_not_to_meet_monster = 951  # Если уменьшать значение, шансы встретить монстра увеличатся
mouse_clicks_max = 1000  # Временный ограничитель
alive = True


def monster_fight():
    global health
    # TODO: Тут дописать алгоритм боя с монстром
    health -= 1
    print(count, "Не повезло! Бой с монстром ¯\_(ツ)_/¯ Здоровье уменьшилось:", health)


def meet_monster():
    global chance_not_to_meet_monster

    _random = randint(1, chance_not_to_meet_monster)

    if _random != 1:
        # Постепенно увеличиваем вероятность встречи с монстром
        if chance_not_to_meet_monster > 10:
            chance_not_to_meet_monster -= 1
        return False
    else:
        monster_fight()
        return True


count = 0
# while mouse_clicks_max > 0:
#     mouse_clicks_max -= 1
#     count += 1
#     if meet_monster():
#         if health <= 0:
#             alive = False
#             break
#     else:
#         print(count, "Монстра нет. Здоровье:", health)
#
# if alive:
#     print("\n🙌 Ты счастливчик, остался жив. (/・・)ノ Здоровье:", health)
# else:
#     print("\n☠⚰ Плохие новости, ТЫ УМЕР!!! Здоровье:", health)

def count_formula(x, y):
    n = x + y^2
    return n


z = count_formula(3, 2)
print(z)