from turtle import *
import time
from GameData.levels.level_1 import lev_1

class pl(Turtle):
    def __init__(se):
        se.p1=Turtle()
        se.p1.penup()
        se.p1.color("blue")
        se.p1.ht()
    def load(se):
        time.sleep(0.25)
        se.p1.write("Loading...",move=False,align='center',font=("PT root UI",25,'bold italic'))
        time.sleep(3)
        se.p1.clear()
    def open_lev_1(se):
        l1=lev_1.play()
        l1.start()
        l1.lis_t_en()
