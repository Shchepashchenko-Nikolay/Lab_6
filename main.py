#!/usr/bin/python
# -*- coding: utf-8 -*-
""" подключение библиотек """
from math import cos, sin, radians
from tkinter import *
import tkinter as tk

"""def create%planet name%window: при вызове функции создается новое окно с информацией о планете"""


def createsunwindow():
    newwindow = Toplevel(window)
    labelexample = Label(newwindow, text="Солнце \n"
                                         "Масса 1,0014 M \n"
                                         "Период обращения	225—250 млн лет\n"
                                         "Орбитальная скорость	220—240 км/с \n"
                                         "Возраст		4,5682±0,0006 млрд лет \n"
                                         "Температура поверхности 5 778 К \n"
                                         "В отличие от Земли, у Солнца нет твердой поверхности. Но у него есть"
                                         " перегретая атмосфера, состоящая из солнечного материала,"
                                         "связанного со звездой гравитацией и магнитными силами")
    labelexample.pack()


def createmercurywindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="МЕРКУРИЙ\n"
                                          "Большая полуось - 0.38709830982а.е, Эксцентриситет - 0.205631752, Наклон"
                                          " к эклиптике - 7.0049863889,"
                                          " Период обращения - 87,968 суток, наклон оси - 0, орбитальная скорость "
                                          "- 47,87км/c\n"
                                          "Радиус меркурия составляет 2440км, масса - 3,285е23кг температура"
                                          " поверхности колеблется от -190 до +430.\n"
                                          "Атмосфера разреженная, её составляют гелий, натрий, кислород, калий,"
                                          "аргон, водород.")

    labelexample2.pack()


def createvenuswindow():
    newqindow = Toplevel(window)
    labelexample2 = Label(newqindow, text="ВЕНЕРА\n"
                                          "Большая полуось - 0.72332981996а.е, Эксцентриситет - 0.006771882, наклон"
                                          " к эклиптике - 3.3946619444, период образщения - 224,695 суток, наклон оси "
                                          "- 177град., орбитальная скорость - 35,02 км/c\n"
                                          "Радиус - 6051км, масса - 4,867е24кг, средняя температура поверхности -"
                                          " +461.\n"
                                          "Атмосфера - углекислый газ, азот\n")

    labelexample2.pack()


def createearthwindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="ЗЕМЛЯ\n"
                                          "Большая полуось - 1а.е., Эксцентриситет - 0.016708617, наклон к эклиптике -"
                                          " 0, период обращения - 365.242 суток, наклон оси - 23,45град, орбитальная"
                                          " скорость - 29,79 км/c\n"
                                          "Радиус - 6 371км, 5,972е24кг, температура от -89,2 до +56,7\n"
                                          "Атмосфера - азот, кислород, углекислый газ, аргон, гелий. \n")

    labelexample2.pack()


def createmarscwindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="МАРС\n"
                                          "Большая полуось - 1.52367934191а.е., Эксцентриситет - 0.093400620, наклон к "
                                          "эклиптике - 1.8497263889град,  период обращения - 686.9297 суток, наклон оси"
                                          " - 25,19град, орбитальная скорость - 24,13км/c\n"
                                          "Радиус - 3 389,5км, масса - 6,39е23кг, температура от -153 до +25\n"
                                          "Атмосфера - углекислый газ, кислород, водород.")

    labelexample2.pack()


def createjupiterwindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="ЮПИТЕР\n"
                                          "Большая полуось - 5.20260319132а.е., Эксцентриситет - 0.048494851, наклон"
                                          " к эклиптике - 1.3032697222, период обращения - 4330.595 суток, наклон оси"
                                          " -  3.13град, орбитальная скорость - 13,06 км/c\n"
                                          "Радиус - 69 911км, масса - 1,898е27кг, температура от -145 до 24000 "
                                          "(в зависимости от близости к ядру). \n"
                                          "Атмосфера - водород, гелий.")

    labelexample2.pack()


def createsaturnwindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="САТУРН\n"
                                          "Большая полуось - 9.55490959574а.е., Эксцентриситет - 0.055508622, наклон к"
                                          " эклиптике - 2.4888780556, период обращения - 10746.94 суток, наклон оси "
                                          "- 25.33град, орбитальная скорость - 9,66км/c\n"
                                          "Радиус - 58 232км, масса - 5,683E26кг, температура от -175 до 11700 "
                                          "(в зависимости от близости к ядру). \n"
                                          "Атмосфера - водород, гелий, метан, амиак.")

    labelexample2.pack()


def createuranuswindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="УРАН\n"
                                          "Большая полуось - 19.21844606178а.е., Эксцентриситет - 0.046295899,  "
                                          "наклон к эклиптике - 0.77319611град, период обращения - 30588.740354 "
                                          "суток, наклон оси - 97,86град, орбитальная скорость - 6,8км/c\n"
                                          "Радиус - 25 362км, масса - 8,681E25 кг, температура от -224 до 4737"
                                          " (в зависимости от близости к ядру).\n"
                                          "Атмосфера - водород, гелий, вода, амиак, метан.")

    labelexample2.pack()


def createneptunewindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="НЕПТУН\n"
                                          "Большая полуось - 30.11038686942а.е., Эксцентриситет - 0.008988095,"
                                          " наклон к эклиптике - 1.7699522град, период обращения - 59799.900456 "
                                          "суток, наклон оси - 28,31град, орбитальная скорость - 5,44 км/c\n"
                                          "Радиус - 24 622 км, масса - 1,024E26 кг, температура от -218 до 7000 "
                                          "(в зависимости от близости к ядру).\n"
                                          "Атмосфера - водород, гелий, углеводород, азот, вода, амиак, метан.")

    labelexample2.pack()


def createplutowindow():
    newwindow = Toplevel(window)
    labelexample2 = Label(newwindow, text="ПЛУТОН\n"
                                          "Большая полуось - 39.5181761979 а.е., Эксцентриситет - 0.2459387823, наклон "
                                          "к эклиптике - 17.1225991666град, период обращения - 90738.995 суток, наклон "
                                          "оси - 122.52град, орбитальная скорость - 4,74км/c\n"
                                          "Радиус - 1 188,3 км, масса - 1.3 × 10^22кг, температура составляет "
                                          "-229град\n"
                                          "Атмосфера - азот, метан, монооксид углерода")

    labelexample2.pack()


def planetspeed(x):
    """x- переменная содержащая 1 из 2 значении,если условия up/down, то скорость планет speedplanet
    повышается/понижается на 0.25. функция вызывается нажатим кнопок speedplanet/speeddown"""
    global speedplanet
    if x == 'up':
        speedplanet += 0.25
    elif x == 'down':
        speedplanet -= 0.25


def speed():
    """angle(0-8)  - переменная отвечающая за скорость движения по окружности, является градусом синуса и косинуса
     i(0-8),ii(0-8)-переменнные координаты отвечающие за нахождение планеты на холсте от скорости angel
           и формулы окружности.
    %button%.place(x,y) -задает координаты кнопки  на холсте
    скорость планет зависит от самой быстрой-Меркурия
    """
    angle = 0
    angle1 = 0
    angle2 = 0
    angle3 = 0
    angle4 = 0
    angle5 = 0
    angle6 = 0
    angle7 = 0
    angle8 = 0

    while True:
        if angle >= 360:
            angle = 0
        elif angle1 >= 360:
            angle1 = 0
        elif angle2 >= 360:
            angle2 = 0
        elif angle3 >= 360:
            angle3 = 0
        elif angle4 >= 360:
            angle4 = 0
        elif angle5 >= 360:
            angle5 = 0
        elif angle6 >= 360:
            angle6 = 0
        elif angle7 >= 360:
            angle7 = 0
        elif angle8 >= 360:
            angle8 = 0

        global speedplanet
        i = 200 * cos(radians(angle))
        ii = 200 * sin(radians(angle))
        angle += 1 * speedplanet

        i1 = 200 * cos(radians(angle1))
        ii1 = 200 * sin(radians(angle1))
        angle1 += 0.7 * speedplanet

        i2 = 200 * cos(radians(angle2))
        ii2 = 200 * sin(radians(angle2))
        angle2 += 0.62 * speedplanet

        i3 = 200 * cos(radians(angle3))
        ii3 = 200 * sin(radians(angle3))
        angle3 += 0.5 * speedplanet

        i4 = 200 * cos(radians(angle4))
        ii4 = 200 * sin(radians(angle4))
        angle4 += 0.27 * speedplanet

        i5 = 200 * cos(radians(angle5))
        ii5 = 200 * sin(radians(angle5))
        angle5 += 0.2 * speedplanet

        i6 = 200 * cos(radians(angle6))
        ii6 = 200 * sin(radians(angle6))
        angle6 += 0.14 * speedplanet

        i7 = 200 * cos(radians(angle7))
        ii7 = 200 * sin(radians(angle7))
        angle7 += 0.11 * speedplanet

        i8 = 200 * cos(radians(angle8))
        ii8 = 200 * sin(radians(angle8))
        angle8 += 0.09 * speedplanet

        informationaboutspeed.place(x=1400, y=900)
        speedup.place(x=1400, y=800)
        speeddown.place(x=1400, y=850)
        sunbtn.place(x=840, y=525)
        mercurybtn.place(x=0.3 * i + 840, y=0.3 * ii + 525)
        venusbtn.place(x=0.55 * i1 + 840, y=0.55 * ii1 + 525)
        earthbtn.place(x=i2*0.9 + 840, y=ii2*0.9 + 525)
        marsbtn.place(x=1.2 * i3 + 840, y=1.2 * ii3 + 525)
        jupiterbtn.place(x=1.5 * i4 + 840, y=1.5 * ii4 + 525)
        saturnbtn.place(x=1.9 * i5 + 840, y=1.9 * ii5 + 525)
        uranusbtn.place(x=2.3 * i6 + 840, y=2.3 * ii6 + 525)
        neptunebtn.place(x=2.6 * i7 + 840, y=2.6 * ii7 + 525)
        plutobtn.place(x=2.9 * i8 + 840, y=2.9 * ii8 + 525)

        window.update()


window = Tk()  # создание окна
window.title('lab6')  # name of programm

# Указываем размеры окна
window.geometry('1610x1050')
# Делаем невозможным менять размеры окна
window.resizable(width=False, height=False)

background_image = tk.PhotoImage(file='sky.png')

window.configure(background='white')
frame = Label(window, bg='white')
title = Label(window, image=background_image, highlightthickness=0,
              bd=0)
title.pack()

loadimage = PhotoImage(file='sun.png').subsample(2, 2)
loadimage2 = tk.PhotoImage(file='mercury.png').subsample(2, 2)
loadimage3 = tk.PhotoImage(file='venera.png').subsample(2, 2)
loadimage4 = tk.PhotoImage(file='earth.png').subsample(2, 2)
loadimage5 = tk.PhotoImage(file='mars.png').subsample(2, 2)
loadimage6 = tk.PhotoImage(file='jupiter.png').subsample(2, 2)
loadimage7 = tk.PhotoImage(file='saturn.png').subsample(2, 2)
loadimage8 = tk.PhotoImage(file='uran.png').subsample(2, 2)
loadimage9 = tk.PhotoImage(file='neptun.png').subsample(2, 2)
loadimage10 = tk.PhotoImage(file='pluto.png').subsample(2, 2)

speedplanet = 1

sunbtn = Button(window, image=loadimage, command=createsunwindow,
                borderwidth=0, bg="black")
mercurybtn = Button(window, image=loadimage2, width=25,
                    command=createmercurywindow, bg="black")

venusbtn = Button(
    window,
    image=loadimage3,
    highlightthickness=0,
    command=createvenuswindow, bg="black"
)

earthbtn = tk.Button(
    window,
    image=loadimage4,
    command=createearthwindow, bg="black"
)

marsbtn = Button(window, image=loadimage5, command=createmarscwindow, bg="black")
jupiterbtn = Button(window, image=loadimage6,
                    command=createjupiterwindow, bg="black")
saturnbtn = Button(window, image=loadimage7, command=createsaturnwindow, bg="black")
uranusbtn = Button(window, image=loadimage8, command=createuranuswindow, bg="black")
neptunebtn = Button(window, image=loadimage9,
                    command=createneptunewindow, bg="black")
plutobtn = Button(window, image=loadimage10, command=createplutowindow, bg="black")

speedup = Button(window, text="Увеличить скорость",
                 command=lambda x='up': planetspeed(x), fg="#eee", bg="#333")

speeddown = Button(window, text="Уменьшить скорость",
                   command=lambda x='down': planetspeed(x), fg="#eee", bg="#333")

informationaboutspeed = Label(window, text="Базовая скорость планет 47.87 км/сек\n кнопки скорости +-0.25%",
                              fg="#eee", bg="#333")

informationaboutspeed.pack()
speedup.pack()
speeddown.pack()
sunbtn.pack()
mercurybtn.pack()
venusbtn.pack()
earthbtn.pack()
marsbtn.pack()
jupiterbtn.pack()
saturnbtn.pack()
uranusbtn.pack()
neptunebtn.pack()
plutobtn.pack()
speed()
