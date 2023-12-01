from tkinter import *
from tkinter import messagebox
from time import *
from random import *
from PIL import Image, ImageTk

adventure_window = Tk()
adventure_window.title('Невероятное приключение воина по имени Олег')
adventure_window.geometry("840x940+500+20")
adventure_window.attributes('-toolwindow', True)
adventure_window.resizable(False, False)

canvas_room = Canvas(adventure_window, width=840, height=840, bg='black')
canvas_room.pack()
canvas_text = Canvas(adventure_window, width=840, height=100, bg='orange')
canvas_text.pack()

picture_lawn = PhotoImage(file='pic/picture_lawn.png')
picture_room2 = PhotoImage(file='pic/picture_room2.png')
picture_room3 = PhotoImage(file='pic/picture_room3.png')
picture_trader = PhotoImage(file='pic/picture_trader.png')
picture_chest = PhotoImage(file='pic/picture_chest.png')
picture_warrior = PhotoImage(file='pic/picture_warrior.png')
picture_warrior_up = PhotoImage(file='pic/picture_warrior_up.png')
picture_warrior_left = PhotoImage(file='pic/picture_warrior_left.png')
picture_warrior_fall = PhotoImage(file='pic/picture_warrior_fall.png')
picture_pointer = PhotoImage(file='pic/picture_pointer.png')
picture_warrior_attack = PhotoImage(file='pic/picture_warrior_attack.png')
picture_warrior_protection = PhotoImage(file='pic/picture_warrior_protection.png')
picture_enemy1 = PhotoImage(file='pic/picture_enemy1.png')
picture_enemy2 = PhotoImage(file='pic/picture_enemy2.png')

health_points = 10
damage = 1
coins = 0

canvas_room.create_image(420, 420, image = picture_lawn)
canvas_room.create_image(420, 420, image = picture_trader)
canvas_room.create_image(420, 420, image = picture_pointer)
canvas_room.create_image(420, 420, image = picture_warrior)
canvas_text.create_text(210, 50, text = 'Твое здоровье: {0}'.format(health_points), font=("Comic Sans MS", 15))
canvas_text.create_text(420, 50, text = 'Твой урон: {0}'.format(damage), font=("Comic Sans MS", 15))
canvas_text.create_text(630, 50, text = 'Твои монеты: {0}'.format(coins), font=("Comic Sans MS", 15))

variable = None
unique_window = None
room = None
room_number = None
pos = canvas_room.coords(4)

def trading(event):
    global unique_window
    def buy_damage(event):
        global damage
        global coins
        if coins >= cost:
            coins -= cost
            damage += increase
            canvas_text.itemconfigure(2, text='Твой урон: {0}'.format(damage), font=("Comic Sans MS", 15))
            canvas_text.itemconfigure(3, text='Твои монеты: {0}'.format(coins), font=("Comic Sans MS", 15))
            unique_window.destroy()
    def buy_health_points(event):
        global health_points
        global coins
        if coins >= cost:
            coins -= cost
            health_points += increase
            canvas_text.itemconfigure(1, text='Твое здоровье: {0}'.format(health_points), font=("Comic Sans MS", 15))
            canvas_text.itemconfigure(3, text='Твои монеты: {0}'.format(coins), font=("Comic Sans MS", 15))
            unique_window.destroy()
    if unique_window is None:
        cost = randint(3, 7)
        increase = randint(1, 3)
        unique_window = Toplevel(adventure_window)
        unique_window.title('Покупка параметров')
        unique_window.geometry("1150x70+340+160")
        unique_window.attributes('-toolwindow', True)
        unique_window.resizable(False, False)
        unique_window.grab_set()
        canvas_trading = Canvas(unique_window, width=1150, height=70, bg='orange')
        canvas_trading.pack()
        canvas_trading.create_text(575, 20, text = 'Здравствуй, путник. Я вижу твое копье изношено. Не хочешь ли сменить свое оружие? (+{0} урона за {1} монет)'.format(increase, cost), font=("Comic Sans MS", 15))
        canvas_trading.create_text(575, 50, text = 'Должно быть, ты ослаб от получееых травм. Я могу их вылечить. Не бесплатно, конечно. (+{0} здоровья за {1} монет)'.format(increase, cost), font = ("Comic Sans MS", 15))
        canvas_trading.tag_bind(1, '<Button-1>', buy_damage)
        canvas_trading.tag_bind(2, '<Button-1>', buy_health_points)

def click(event):
    global pos
    pos = canvas_room.coords(4)
    if (room == 2 and pos[0] >= 240 and pos[0] <= 480 and pos[1] >= 360 and pos [1] <= 480 or
            room == 3 and pos[0] >= 600 and pos[0] <= 720 and pos[1] >= 120 and pos [1] <= 360):
        global unique_window
        if unique_window is None:
            global coins
            received_coins = randint(1, 5)
            unique_window = messagebox.showinfo('Открытие сундука', 'Вы получили {0} монет'.format(received_coins))
            coins += received_coins
            canvas_text.itemconfigure(3, text = 'Твои монеты: {0}'. format(coins), font=("Comic Sans MS", 15))
    elif (room == 2 and pos[0] >= 600 and pos[0] <= 840 and pos[1] >= 360 and pos [1] <= 480 or
          room == 3 and pos[0] >= 360 and pos[0] <= 480 and pos[1] >= 600 and pos [1] <= 840):
        room_geniration()


def meet_monster():
    global health_points
    global damage
    global coins
    global variable
    global room_number
    power = randint(-2, 2)
    power = (power * room_number / 2)
    monster_health = power + randint(-3, 3)
    def protection(event):
        canvas_battle.move(100, 0)
        canvas_battle.itemconfigure(3, image=picture_warrior_protection)
        power /= 2
        health_points -= power

    meet = randint(1, variable)
    if meet == 1:
        monster_window = Toplevel(adventure_window)
        monster_window.title('Монстр!!!')
        monster_window.geometry("400x200+720+440")
        monster_window.attributes('-toolwindow', True)
        monster_window.resizable(False, False)
        monster_window.grab_set()
        canvas_battle = Canvas(monster_window, width=400, height=200, bg='black')
        canvas_battle.pack()
        canvas_battle.create_image(400, 400, image=picture_room3)
        canvas_battle.create_image(10,  49, anchor = NW, image=picture_warrior)
        canvas_battle.create_image(300,  49, anchor = NW, image=picture_enemy1)
        canvas_battle.bind_all('<KeyPress-0>', protection)
        canvas_battle.bind_all('<KeyPress-1>', attack)

    else:
        if variable > 300:
            variable -= 1


def leave(event):
    canvas_room.itemconfigure(4, image = picture_warrior)
    for warrior_leave in range(1, 60):
        canvas_room.move(4, 0, 5)
        adventure_window.update()
        sleep(00.01)
    for warrior_leave in range(1, 10):
        canvas_room.move(4, 5, 5)
        adventure_window.update()
        sleep(00.01)
    for warrior_leave in range(1, 70):
        canvas_room.move(4, 5, 0)
        adventure_window.update()
        sleep(00.01)
    room_geniration()

def room_geniration():
    global unique_window
    global variable
    global room_number
    global room
    variable = 500
    unique_window = None
    room = randint(1, 3)
    def move(event):
        global health_points
        global damage
        global coins
        global pos
        pos = canvas_room.coords(4)
        if (room == 2 and (pos[0] >= 140 and pos[0] <= 220 and pos[1] >= 40 and pos[1] <= 680 or
                            pos[0] >= 140 and pos[0] <= 700 and pos[1] >= 640 and pos[1] <= 680 or
                            pos[0] >= 140 and pos[0] <= 460 and pos[1] >= 400 and pos[1] <= 440 or
                            pos[0] >= 140 and pos[0] <= 700 and pos[1] >= 160 and pos[1] <= 200 or
                            pos[0] >= 620 and pos[0] <= 700 and pos[1] >= 160 and pos[1] <= 440 or
                            pos[0] >= 620 and pos[0] <= 820 and pos[1] >= 400 and pos[1] <= 440) or
                room == 3 and (pos[0] >= 20 and pos[0] <= 460 and pos[1] >= 160 and pos[1] <= 200 or
                            pos[0] >= 380 and pos[0] <= 460 and pos[1] >= 160 and pos[1] <= 440 or
                            pos[0] >= 140 and pos[0] <= 700 and pos[1] >= 400 and pos[1] <= 440 or
                            pos[0] >= 140 and pos[0] <= 220 and pos[1] >= 400 and pos[1] <= 680 or
                            pos[0] >= 620 and pos[0] <= 700 and pos[1] >= 160 and pos[1] <= 680 or
                            pos[0] >= 380 and pos[0] <= 460 and pos[1] >= 640 and pos[1] <= 800 or
                            pos[0] >= 380 and pos[0] <= 700 and pos[1] >= 640 and pos[1] <= 680)):
            if event.keysym == 'Up':
                canvas_room.itemconfigure(4, image = picture_warrior_up)
                canvas_room.move(4, 0, -5)
            elif event.keysym == 'Down':
                canvas_room.itemconfigure(4, image = picture_warrior)
                canvas_room.move(4, 0, 5)
            elif event.keysym == 'Left':
                canvas_room.itemconfigure(4, image = picture_warrior_left)
                canvas_room.move(4, -5, 0)
            elif event.keysym == 'Right':
                canvas_room.itemconfigure(4, image = picture_warrior)
                canvas_room.move(4, 5, 0)
            meet_monster()
        elif room == 1:
            pass
        else:
            canvas_room.itemconfigure(4, image=picture_warrior_fall)
            if messagebox.askyesno('ВЫ УРОНИЛИ ОЛЕГА!!!', 'Хотите ли вы выйти из приложения?'):
                adventure_window.destroy()
            else:
                health_points = 10
                damage = 1
                coins = 0
                canvas_text.itemconfigure(1, text='Твое здоровье: {0}'.format(health_points), font=("Comic Sans MS", 15))
                canvas_text.itemconfigure(2, text='Твой урон: {0}'.format(damage), font=("Comic Sans MS", 15))
                canvas_text.itemconfigure(3, text='Твои монеты: {0}'.format(coins), font=("Comic Sans MS", 15))
                room_geniration()
    canvas_room.bind_all('<KeyPress-Up>', move)
    canvas_room.bind_all('<KeyPress-Down>', move)
    canvas_room.bind_all('<KeyPress-Left>', move)
    canvas_room.bind_all('<KeyPress-Right>', move)
    if room == 1:
        canvas_room.itemconfigure(1, image = picture_lawn)
        canvas_room.itemconfigure(2, image = picture_trader)
        canvas_room.itemconfigure(4, image = picture_warrior)
        canvas_room.coords(2, 420, 280)
        canvas_room.coords(3, 740, 640)
        canvas_room.coords(4, 0, 420)
        for warrior_moove in range(1, 84):
            canvas_room.move(4, 5, 0)
            adventure_window.update()
            sleep(0.01)
        canvas_room.itemconfigure(4, image = picture_warrior_up)
        canvas_room.tag_bind(2, '<Button-1>', trading)
        canvas_room.tag_bind(3, '<Button-1>', leave)
    if room == 2:
        canvas_room.itemconfigure(1, image = picture_room2)
        canvas_room.itemconfigure(2, image = picture_chest)
        canvas_room.itemconfigure(4, image = picture_warrior)
        canvas_room.coords(2, 420, 420)
        canvas_room.coords(3, 780, 420)
        canvas_room.coords(4, 180, 60)
        canvas_room.tag_bind(3, '<Button-1>', click)
        canvas_room.tag_bind(2, '<Button-1>', click)
    if room == 3:
        canvas_room.itemconfigure(1, image = picture_room3)
        canvas_room.itemconfigure(2, image = picture_chest)
        canvas_room.itemconfigure(4, image = picture_warrior)
        canvas_room.coords(2, 660, 180)
        canvas_room.coords(3, 420, 780)
        canvas_room.coords(4, 60, 180)
        canvas_room.tag_bind(3, '<Button-1>', click)
        canvas_room.tag_bind(2, '<Button-1>', click)


room_geniration()
adventure_window.mainloop()