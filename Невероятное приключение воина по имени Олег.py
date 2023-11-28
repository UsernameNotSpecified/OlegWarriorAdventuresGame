from tkinter import *
from time import *
from random import *

adventure_window = Tk()
adventure_window.title('Невероятное приключение воина по имени Олег')
adventure_window.maxsize(840, 940)
adventure_window.minsize(840, 940)
adventure_window.geometry("+500+20")

canvas_room = Canvas(adventure_window, width = 840, height = 840)
canvas_room.pack()
canvas_text = Canvas(adventure_window, width = 840, height = 100, bg = 'orange')
canvas_text.pack()

picture_lawn = PhotoImage(file ='pic/picture_lawn.png')
picture_castle = PhotoImage(file ='pic/замок.png')
picture_trader = PhotoImage(file ='pic/picture_trader.png')
picture_chest = PhotoImage(file ='pic/picture_chest.png')
picture_warrior = PhotoImage(file ='pic/picture_warrior.png')
picture_warrior_up = PhotoImage(file ='pic/picture_warrior_up.png')
picture_warrior_left = PhotoImage(file ='pic/picture_warrior_left.png')
picture_warrior_attack = PhotoImage(file ='pic/picture_warrior_attack.png')
picture_pointer = PhotoImage(file ='pic/picture_pointer.png')

canvas_room.create_image(420, 420, image = picture_lawn)
canvas_room.create_image(420, 420, image = picture_trader)
canvas_room.create_image(420, 420, image = picture_pointer)
canvas_room.create_image(420, 420, image = picture_warrior)

def trading(event):
    trading_window =  Toplevel(adventure_window)
    trading_window.title('tr')
    #Прописать окно торговли
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

def leave_room(event):
    room_geniration()
def open_chest_window(event):
    chest_window = Toplevel(adventure_window)
    chest_window.title('ch')
    #Прописать окно сундука
def room_geniration():
    room = randint(1, 3)
    def move(event):
        pos = canvas_room.coords(4)
        if (room == 2 and (pos[0] >= 168 and pos[0] <= 192 and pos[1] >= 50 and pos[1] <= 670 or
                          pos[0] >= 288 and pos[0] <= 672 and pos[1] >= 650 and pos[1] <= 670 or
                          pos[0] >= 288 and pos[0] <= 432 and pos[1] >= 410 and pos[1] <= 430 or
                          pos[0] >= 288 and pos[0] <= 552 and pos[1] >= 170 and pos[1] <= 190 or
                          pos[0] >= 648 and pos[0] <= 672 and pos[1] >= 170 and pos[1] <= 310 or
                          pos[0] >= 648 and pos[0] <= 792 and pos[1] >= 410 and pos[1] <= 430) or
        room == 3 and (pos[0] >= 48 and pos[0] <= 312 and pos[1] >= 170 and pos[1] <= 190 or
                          pos[0] >= 408 and pos[0] <= 432 and pos[1] >= 170 and pos[1] <= 310 or
                          pos[0] >= 168 and pos[0] <= 552 and pos[1] >= 410 and pos[1] <= 430 or
                          pos[0] >= 168 and pos[0] <= 192 and pos[1] >= 530 and pos[1] <= 670 or
                          pos[0] >= 648 and pos[0] <= 672 and pos[1] >= 170 and pos[1] <= 550 or
                          pos[0] >= 408 and pos[0] <= 432 and pos[1] >= 650 and pos[1] <= 790 or
                          pos[0] >= 528 and pos[0] <= 672 and pos[1] >= 650 and pos[1] <= 670)):
            y1 = -5
            y2 = 5
            x1 = -5
            x2 = 5
        else:
            y1 = 5
            y2 = -5
            x1 = 5
            x2 = -5
        if event.keysym == 'Up':
            canvas_room.itemconfigure(4, image = picture_warrior_up)
            canvas_room.move(4, 0, y1)
            y1 = -5
            y2 = 5
            x1 = -5
            x2 = 5
        elif event.keysym == 'Down':
            canvas_room.itemconfigure(4, image = picture_warrior)
            canvas_room.move(4, 0, y2)
            y1 = -5
            y2 = 5
            x1 = -5
            x2 = 5
        elif event.keysym == 'Left':
            canvas_room.itemconfigure(4, image = picture_warrior_left)
            canvas_room.move(4, x1, 0)
            y1 = -5
            y2 = 5
            x1 = -5
            x2 = 5
        elif event.keysym == 'Right':
            canvas_room.itemconfigure(4, image = picture_warrior)
            canvas_room.move(4, x2, 0)
            y1 = -5
            y2 = 5
            x1 = -5
            x2 = 5
        
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
        canvas_room.itemconfigure(1, image = picture_castle)
        canvas_room.itemconfigure(2, image = picture_chest)
        canvas_room.itemconfigure(4, image = picture_warrior)
        canvas_room.coords(2, 420, 420)
        canvas_room.coords(3, 780, 420)
        canvas_room.coords(4, 180, 60)
        canvas_room.tag_bind(3, '<Button-1>', leave_room)
        canvas_room.tag_bind(2, '<Button-1>', open_chest_window)
    if room == 3:
        canvas_room.itemconfigure(1, image = picture_castle)
        canvas_room.itemconfigure(2, image = picture_chest)
        canvas_room.itemconfigure(4, image = picture_warrior)
        canvas_room.coords(2, 660, 180)
        canvas_room.coords(3, 420, 780)
        canvas_room.coords(4, 60, 180)
        canvas_room.tag_bind(3, '<Button-1>', leave_room)
        canvas_room.tag_bind(2, '<Button-1>', open_chest_window)

room_geniration()

adventure_window.mainloop()
