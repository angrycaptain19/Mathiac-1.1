from turtle import *
import time
from GameData.levels.level_1.physics import math_add as m
import os
import random as r

class play(Turtle):
    def __init__(l):
        l.t=Turtle()
        l.t.color('cyan','blue')
        l.t.ht()
        l.t.up()
        l.t2=Turtle()
        l.t2.color('orange')
        l.t2.ht()
        l.t2.up()
    def start(l):
        l.t.setpos(0,95)
        time.sleep(0.25)
        l.t.write("Level 1",align='center',font=("Times",50,'bold italic'))
        time.sleep(0.25)
        l.t.setpos(0,50)
        l.t.color("Blue")
        l.dt=open("GameData\\levels\\level_1\\readme.txt","r")
        l.d=l.dt.read()
        l.t.write(l.d,align='center',font=("Sans serif",25,'bold italic'))
        l.dt.close()
        l.draw_button()
    def draw_button(l):
        l.t.setpos(0,-50)
        l.t.st()
        l.t.shape('square')
        l.t.turtlesize(3,8,12)
        l.t.setpos(0,-55)
        l.t2.setpos(0,-65)
        l.t.color('cyan','blue')
        l.t2.write("Play",align='center',font=("Sans serif",20,'bold italic'))
    def lis_t_en(l):
        l.t.onclick(l.activate)
        l.t2.write("Play",align='center',font=("Sans serif",20,'bold italic'))
    def activate(l,x,y):
        l.t.ht()
        l.t2.clear()
        l.t.clear()
        l.start_lev_1()
    def start_lev_1(l):
        l.score=0
        l.an=0
        l.s=Turtle()
        l.s.ht()
        l.s.up()
        l.s.color('Navy Blue')
        l.s.setpos(400,225)
        for i in range(5):
            l.s.write('{o}/5'.format(o=l.an),align='center',font=("Calibri",40,'bold italic'))
            l.t.setpos(0,0)
            l.a=m.create()
            l.b=m.create()
            l.t.write('{a}+{b}=?'.format(a=l.a,b=l.b),align='center',font=("Sans serif",60,'bold italic'))
            l.c=m.add_auto(l.a,l.b)
            l.d=numinput('Answer:','Enter your answer here:')
            if l.d==l.c:
                l.score+=l.c*2
                l.an+=1
            else:
                l.score+=l.c/2
            l.s.clear()
            l.t.clear()
        if l.an==5:
            bon=[10,50,100,500,1000]
            bon=r.choice(bon)
            l.score+=bon
            l.t.write('Math Crush!'.format(o=l.an),align='center',font=("Times new Roman",40,'bold italic'))
            time.sleep(2)
            l.t.clear()
            l.t.write(':):):)'.format(o=l.an),align='center',font=("Sans serif",40,'bold italic'))
            time.sleep(2)
            l.t.clear()
            l.t.write('Your score is {s}'.format(s=l.score),align='center',font=("Sans serif",40,'bold italic'))
            f=open("./GameData\ending.txt","r")
            ef=f.read()
            print(ef)
            f.close()
        else:
            l.t.color('red')
            l.t.write(':(:(:('.format(o=l.an),align='center',font=("Times new Roman",40,'bold italic'))
            time.sleep(2)
            l.t.clear()
            l.t.write('You did not reach the goal.'.format(o=l.an),align='center',font=("Sans serif",40,'bold italic'))
            time.sleep(2)
            l.t.clear()
            l.t.write('Your score is {s}'.format(s=l.score),align='center',font=("Sans serif",40,'bold italic'))
            
            
