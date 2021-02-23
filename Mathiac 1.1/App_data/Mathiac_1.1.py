from turtle import *
from GameData.play import *
import time

#Setting up Screen

win=Screen()
win.title('Mathiac 1.1')
win.setup(1050,575)
win.colormode(255)
bgcol=(255,200,150)
win.bgcolor(bgcol)

class i(Turtle):
    def __init__(se):
        se.t=Turtle()
        se.t2=Turtle()
        se.t.penup()
        se.t.color("red")
        se.t.setpos(0,100)
        se.t.hideturtle()
        se.t2.penup()
        se.t2.color("red")
        se.t2.setpos(0,-65)
        se.t2.hideturtle()
    def draw(se):
        time.sleep(0.25)
        se.t.write("Mathiac",align='center',font=("Times new Roman",75,'bold italic'))
        time.sleep(0.25)
        se.t.setpos(0,50)
        se.t.color("Blue")
        se.t.write("Mathiac 1.1",align='center',font=("Sans serif",20,'bold italic'))
        se.draw_button()
    def draw_button(se):
        se.t.setpos(0,-50)
        se.t.st()
        se.t.shape('square')
        se.t.color('pink','orange')
        se.t.turtlesize(3,8,12)
        se.t.setpos(0,-55)
        se.t2.write("Play",align='center',font=("Sans serif",20,'bold italic'))
    def lis_t_en(se):
        se.t.onclick(i_n.activate)
        se.t2.write("Play",align='center',font=("Sans serif",20,'bold italic'))
    def activate(se,x,y):
        se.t.ht()
        se.t2.clear()
        se.t.clear()
        se.p=pl()
        se.p.load()
        se.start_1()
    def start_1(se):
        se.p.open_lev_1()
        

i_n=i()
i_n.draw()
i_n.lis_t_en()
done()
