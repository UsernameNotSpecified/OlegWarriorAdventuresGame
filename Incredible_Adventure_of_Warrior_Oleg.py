from tkinter import *
from tkinter import messagebox
from time import *
from random import *

adventure_window = Tk()
adventure_window.title('Невероятное приключение воина по имени Олег')
adventure_window.geometry("840x940+500+20")
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

health_points = 10
damage = 1
coins = 0

canvas_room.create_image(420, 420, image = picture_lawn)
canvas_room.create_image(420, 420, image = picture_trader)
canvas_room.create_image(420, 420, image = picture_pointer)
canvas_room.create_image(420, 420, image = picture_warrior)
canvas_text.create_text(420, 50, text = 'Твое здоровье: {0}          Твой урон: {1}          Кол-во монет: {2}'.format(health_points, damage, coins))

def trading(event):
        trading_window = Toplevel(adventure_window)
        trading_window.title('tr')
        # Прописать окно торговли


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

def meet_monster():
    meet = randint(1, 500)
    if meet == 1:
        monster_window = Toplevel(adventure_window)
        monster_window.geometry("400x200+500+20")
        monster_window.resizable(False, False)
        cfnvas_battle = Canvas(monster_window, width=400, height=200, bg='orange')
        cfnvas_battle.pack()
        cfnvas_battle.create_image(10, 49, image=picture_room3)
        cfnvas_battle.create_image(10,  49, anchor = NW, image=picture_warrior)
    # else:
    #     variable -= 1

def leave_room(event):
    room_geniration()


def open_chest_window(event):
    chest_window = Toplevel(adventure_window)
    chest_window.title('ch')
    # Прописать окно сундука


def room_geniration():
    room = randint(1, 3)
    variable = 1000
    def move(event):
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
        canvas_room.tag_bind(3, '<Button-1>', leave_room)
        canvas_room.tag_bind(2, '<Button-1>', open_chest_window)
    if room == 3:
        canvas_room.itemconfigure(1, image = picture_room3)
        canvas_room.itemconfigure(2, image = picture_chest)
        canvas_room.itemconfigure(4, image = picture_warrior)
        canvas_room.coords(2, 660, 180)
        canvas_room.coords(3, 420, 780)
        canvas_room.coords(4, 60, 180)
        canvas_room.tag_bind(3, '<Button-1>', leave_room)
        canvas_room.tag_bind(2, '<Button-1>', open_chest_window)


room_geniration()
adventure_window.mainloop()