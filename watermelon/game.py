from tkinter import *
from random import *
from tkinter import messagebox

t_a = 'y'
while t_a == 'y' :
    quit = 0
    game_type = 0

    def Quit() :
        global quit
        quit = 1
        win_gamemode.destroy()

    def gamemode(game) :
        global game_type
        game_type = game
        win_gamemode.destroy()

    win_gamemode = Tk()
    win_gamemode.title('game settings')
    win_gamemode.geometry("750x500")

    img = PhotoImage(file = '수박씨 빼기 게임 이미지.png')
    img1 = PhotoImage(file = '+timer.png')
    img2 = PhotoImage(file = 'dangerous.png')

    lbr = Label(win_gamemode, text = "select you gamemode!", font = 50)

    lmg = Label(win_gamemode, image = img)
    lmg1 = Label(win_gamemode, image = img1)
    lmg2 = Label(win_gamemode, image = img2)

    lbl_clas = Label(win_gamemode, text = 'classic')
    lbl_time = Label(win_gamemode, text = 'timer/speedrun')
    lbl_dang = Label(win_gamemode, text = 'dangerous')

    btn_clas = Button(win_gamemode, text = 'classic', command = lambda : gamemode("classic"))
    btn_time = Button(win_gamemode, text = 'timer/speedrun', command = lambda : gamemode("timer"))
    btn_dang = Button(win_gamemode, text = 'dangerous', command = lambda : gamemode("dangerous"))

    btn_quit = Button(win_gamemode, text = 'quit', command = Quit)

    lbr.grid(row = 0, column = 1)

    lmg.grid(row = 1, column = 0)
    lmg1.grid(row = 1, column = 1)
    lmg2.grid(row = 1, column = 2)

    lbl_clas.grid(row = 2, column = 0)
    lbl_time.grid(row = 2, column = 1)
    lbl_dang.grid(row = 2, column = 2)

    btn_clas.grid(row = 3, column = 0)
    btn_time.grid(row = 3, column = 1)
    btn_dang.grid(row = 3, column = 2)

    btn_quit.grid(row = 3, column = 3)

    win_gamemode.mainloop()


    if game_type == 'dangerous' :
        messagebox.showinfo("ok", 'Working on dangerous mode')
        quit = 1


    seed_num = 0

    def ready() :
        global seed_num
        seed_num = int(entry.get())
        win_mainual.destroy()

    win_mainual = Tk()

    if quit == 1 :
        win_mainual.destroy()

    win_mainual.title("settings")
    win_mainual.geometry("300x70")

    lbl_ask = Label(win_mainual, text = 'how many seeds?(your answer > 0)')
    lbl_dec = Label(win_mainual, text = 'answer : ')
    entry = Entry(win_mainual)

    btn_answered = Button(win_mainual, text = 'Ok!', command = ready)

    lbl_ask.grid(row = 0, column = 1)
    lbl_dec.grid(row = 1, column = 0)
    entry.grid(row = 1, column = 1)
    btn_answered.grid(row = 1, column = 2)
    win_mainual.mainloop()



    speed = 10

    def move(event) :
        global px, py
        if event.keysym == 'Up' :
            canvas.delete("all")
            py -= speed
            canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill = "cyan")
        elif event.keysym == 'Down' :
            canvas.delete("all")
            py += speed
            canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill = "cyan")
        elif event.keysym == 'Right' :
            canvas.delete("all")
            px += speed
            canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill = "cyan")
        elif event.keysym == 'Left' :
            canvas.delete("all")
            px -= speed
            canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill = "cyan")
        g = seed_num - seed
        for i in range(g) :
            canvas.create_rectangle(cpux[i], cpuy[i], cpux[i] + 5, cpuy[i] + 5, fill = "#423934")
        playerx.clear()
        playery.clear()
        for i in range(10) :
            posnum = i - 6
            playerx.append(px + posnum)
            playery.append(py + posnum)

    def pick_up_seed(event) :
        global seed
        g = seed_num - seed
        for i in range(g) :
            if cpux[i] in playerx and cpuy[i] in playery :
                print('%s, %s' % (cpux[i], cpuy[i]))
                del cpux[i]
                del cpuy[i]
                seed += 1
                canvas.delete("all")
                break
    

        g = seed_num - seed   
        for i in range(g) :
            canvas.create_rectangle(cpux[i], cpuy[i], cpux[i] + 5, cpuy[i] + 5, fill = "#423934")
        canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill = "cyan")
        seed_left(seed)

    def change_speed(fastness) :
        global speed
        if fastness == 'up' :
            speed += 1
        else :
            speed -= 1
        speed_label(speed)

    def seed_left(seeds) :
        lbl_seed['text'] = "%s seed left" % (seed_num - seeds)
        if seed_num - seeds == 0 :
            if game_type == "timer" :
                win_timer.destroy()
            messagebox.showinfo("ok", "you have succed!")
            win.destroy()

    def speed_label(UD) :
        lbl_speed['text'] = '%s' % UD

    px, py = 255, 235
    w, h = 13, 2
    seed = 0
    cpux = []
    cpuy = []
    playerx = []
    playery = []
    for i in range(seed_num) :
        rx, ry = randint(0, 500), randint(0, 460)
        cpux.append(rx)
        cpuy.append(ry)

    win = Tk()

    if quit == 1 :
        win.destroy()

    if game_type == "timer" :
        timer = seed_num * 10
        win_timer = Tk()
        win_timer.title("timer")
        win_timer.geometry("300x300+800+400")

        def timers() :
            global timer
            timer -= 1
            lbl_time['text'] = timer
            if timer > 0 :
                win.after(1000, timers)
            else :
                messagebox.showwarning("ok", "you have failed!")
                win_timer.destroy()
                win.destroy()

        lbl_time = Label(win_timer, font = 30)
        lbl_time.pack()
        win_timer.after(0, timers)

    win.title("watermelon seeds")
    win.geometry("510x650")
    win.configure(bg='light green')


    canvas = Canvas(win, bg = "#eb4263", width = 510, height = 475)
    canvas.grid(row = 0, column = 0, columnspan = 6)
    canvas.bind_all("<KeyPress-Up>", move)
    canvas.bind_all("<KeyPress-Down>", move)
    canvas.bind_all("<KeyPress-Right>", move)
    canvas.bind_all("<KeyPress-Left>", move)
    canvas.bind_all("<Return>", pick_up_seed)

    for i in range(seed_num) :
        canvas.create_rectangle(cpux[i], cpuy[i], cpux[i] + 5, cpuy[i] + 5, fill = "#423934")
    canvas.create_oval(px - 5, py - 5, px + 5, py + 5, fill = "cyan")

    lbl_seed = Label(win, text = "%s seed left" % seed_num, font = ("Elephant" ,20), fg = 'black', bg = 'light green')

    btn_faster = Button(win, text = '△', bg = 'light green', fg = 'black', command = lambda : change_speed('up'))
    btn_slower = Button(win, text = '▽', bg = 'light green', fg = 'black', command = lambda : change_speed('down'))
    lbl_speed = Label(win, text = '%s' % speed, bg = 'light green', fg = 'black')

    btn_faster.grid(row = 1, column = 4)
    lbl_speed.grid(row = 2, column = 4)
    btn_slower.grid(row = 3, column = 4)

    lbl_seed.grid(row = 4, column = 2)

    win.mainloop()

    def set_retry(YN) :
        global t_a
        if YN == 'no' :
            t_a = 'n'
        win_retry.destroy()

    win_retry = Tk()

    win_retry.title("play again?")

    lbl_retry = Label(win_retry, text = 'Try again?', font = 20)
    btn_yes = Button(win_retry, text = 'yes', command = lambda : set_retry('yes'))
    btn_no = Button(win_retry, text = 'no', command = lambda : set_retry('no'))

    lbl_retry.grid(row = 0, column = 1)
    btn_yes.grid(row = 1, column = 0)
    btn_no.grid(row = 1, column = 2)

    win_retry.mainloop()
