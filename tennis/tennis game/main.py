from tkinter import *
from court import *
from ball import *

win = Tk()

width, height = 745, 374

court = Court(win, width, height, 'court.png')

x1, y1 = 745/2 - 15, 374/2 - 15
x2, y2 = 745/2 + 15, 374/2 + 15

ball = Ball(court, x1, y1, x2, y2)

def play_game() :
    #ball(move_ball)
    ball.move_ball()

    win.after(50, play_game)

play_game()

win.mainloop()
