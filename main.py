#!/usr/bin/env python3



from math import cos, sin, radians

from tkinter import *
import tkinter as tk




def createsunWindow():
    newWindow = Toplevel(window)

    labelExample = Label(newWindow, text="Солнце")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample.pack()
def createmercuryWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="МЕРКУРИЙ\n"
                         "Большая полуось - 0.38709830982а.е, Эксцентриситет - 0.205631752, Наклон к эклиптике - 7.0049863889, Период обращения - 87,968 суток, наклон оси - 0, орбитальная скорость - 47,87км/c\n"
                          "Радиус меркурия составляет 2440км, масса - 3,285е23кг температура поверхности колеблется от -190 до +430.\n"
                          "Атмосфера разреженная, её составляют гелий, натрий, кислород, калий, аргон, водород.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createvenusWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="ВЕНЕРА\n"
                          "Большая полуось - 0.72332981996а.е, Эксцентриситет - 0.006771882, наклон к эклиптике - 3.3946619444, период образщения - 224,695 суток, наклон оси - 177град., орбитальная скорость - 35,02 км/c\n"
                          "Радиус - 6051км, масса - 4,867е24кг, средняя температура поверхности - +461.\n"
                          "Атмосфера - углекислый газ, азот\n")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createearthWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="ЗЕМЛЯ\n"
                          "Большая полуось - 1а.е., Эксцентриситет - 0.016708617, наклон к эклиптике - 0, период обращения - 365.242 суток, наклон оси - 23,45град, орбитальная скорость - 29,79 км/c\n"
                          "Радиус - 6 371км, 5,972е24кг, температура от -89,2 до +56,7\n"
                          "Атмосфера - азот, кислород, углекислый газ, аргон, гелий. \n")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createmarscWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="МАРС\n"
                          "Большая полуось - 1.52367934191а.е., Эксцентриситет - 0.093400620, наклон к эклиптике - 1.8497263889град,  период обращения - 686.9297 суток, наклон оси - 25,19град, орбитальная скорость - 24,13км/c\n"
                          "Радиус - 3 389,5км, масса - 6,39е23кг, температура от -153 до +25\n"
                          "Атмосфера - углекислый газ, кислород, водород.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createjupiterWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="ЮПИТЕР\n"
                          "Большая полуось - 5.20260319132а.е., Эксцентриситет - 0.048494851, наклон к эклиптике - 1.3032697222, период обращения - 4330.595 суток, наклон оси -  3.13град, орбитальная скорость - 13,06 км/c\n"
                          "Радиус - 69 911км, масса - 1,898е27кг, температура от -145 до 24000 (в зависимости от близости к ядру). \n"
                          "Атмосфера - водород, гелий.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createsaturnWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="САТУРН\n"
                          "Большая полуось - 9.55490959574а.е., Эксцентриситет - 0.055508622, наклон к эклиптике - 2.4888780556, период обращения - 10746.94 суток, наклон оси - 25.33град, орбитальная скорость - 9,66км/c\n"
                          "Радиус - 58 232км, масса - 5,683E26кг, температура от -175 до 11700 (в зависимости от близости к ядру). \n"
                          "Атмосфера - водород, гелий, метан, амиак.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createuranusWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="УРАН\n"
                          "Большая полуось - 19.21844606178а.е., Эксцентриситет - 0.046295899,  наклон к эклиптике - 0.77319611град, период обращения - 30588.740354 суток, наклон оси - 97,86град, орбитальная скорость - 6,8км/c\n"
                          "Радиус - 25 362км, масса - 8,681E25 кг, температура от -224 до 4737 (в зависимости от близости к ядру).\n"
                          "Атмосфера - водород, гелий, вода, амиак, метан.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createneptuneWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="НЕПТУН\n"
                          "Большая полуось - 30.11038686942а.е., Эксцентриситет - 0.008988095, наклон к эклиптике - 1.7699522град, период обращения - 59799.900456 суток, наклон оси - 28,31град, орбитальная скорость - 5,44 км/c\n"
                          "Радиус - 24 622 км, масса - 1,024E26 кг, температура от -218 до 7000 (в зависимости от близости к ядру).\n"
                          "Атмосфера - водород, гелий, углеводород, азот, вода, амиак, метан.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createplutoWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="ПЛУТОН\n"
                          "Большая полуось - 39.5181761979 а.е., Эксцентриситет - 0.2459387823, наклон к эклиптике - 17.1225991666град, период обращения - 90738.995 суток, наклон оси - 122.52град, орбитальная скорость - 4,74км/c\n"
                          "Радиус - 1 188,3 км, масса - 1.3 × 10^22кг, температура составляет -229град\n"
                          "Атмосфера - азот, метан, монооксид углерода")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()

def cat():
    i = 0 #именно она движет
    ii =0
    x=0
    angle = 0

    while True:
        if angle >= 360:
            angle = 0
        i = 200 * cos(radians(angle))
        ii = 200 * sin(radians(angle))
        angle += 1

        sunbtn.place(x=840, y=525)
        mercurybtn.place(x=0.5*i+840, y=0.5*ii+525)

        venusbtn.place(x=0.75*i+840, y=0.75*ii+525)
        earthbtn.place(x=i+840, y=ii+525)


        marsbtn.place(x=1.25*i+840, y=1.25*ii+525)
        jupiterbtn.place(x=1.5*i+840, y=1.5*ii+525)

        saturnbtn.place(x=1.75*i+840, y=1.75*ii+525)
        uranusbtn.place(x=2*i+840, y=2*ii+525)

        neptunebtn.place(x=2.25*i+840, y=2.25*ii+525)
        plutobtn.place(x=2.5*i+840, y=2.5*ii+525)
        window.update()


     #   i = math.cosh(x)
     #   ii =math.sinh(x)



def die(): #она обновляет кооординаты , это mainloop()/ ее замена
    while True:
        cat()
        #catpl()
        window.update()




window = Tk()  # создание окна

#window['bg'] = 'black'  # типо фон черный

window.title('lab6')  # name of programm
# Указываем размеры окна
window.geometry('1680x1050')
# Делаем невозможным менять размеры окна
window.resizable(width=False, height=False)

# canvas = Canvas(window, height=1280, width=720)
# canvas.pack()

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
#frame = Frame(window, bg='black')
#frame.place(relx=0.1, rely=0.21, relwidth=0.2, relheight=0.1)




background_image = tk.PhotoImage(file="sky.png")

window.configure(background="white")


frame = Label(window, bg='white')
title = Label(window, image=background_image,highlightthickness=0, bd=0)


title.pack()




loadimage = PhotoImage(file="sun.png")
loadimage2 = tk.PhotoImage(file="mercury.png").subsample(1,1)#ТИПО РАЗМЕР КАРТИНКИ
loadimage3 = tk.PhotoImage(file="venera.png")
loadimage4 = tk.PhotoImage(file="earth.png")
loadimage5 = tk.PhotoImage(file="mars.png")
loadimage6 = tk.PhotoImage(file="jupiter.png")
loadimage7 = tk.PhotoImage(file="saturn.png")
loadimage8 = tk.PhotoImage(file="uran.png")
loadimage9 = tk.PhotoImage(file="neptun.png")
loadimage10 = tk.PhotoImage(file="pluto.png")


#window.overrideredirect(True)
#window.geometry("+250+250")
#window.wm_attributes("-topmost", True)
#window.wm_attributes("-disabled", True)
#window.wm_attributes("-transparentcolor", "white") # -- фон_белый


#plane = canvas.create_image(450,250,image=loadimage2)

sunbtn =Button(window,
                   image=loadimage,
#width=25, #размеры планеты
                   command=createearthWindow,
                   borderwidth=1000,bd=0)
mercurybtn=Button(window,
                   image=loadimage2,
                   command=createmercuryWindow)

venusbtn=Button(window,
               image=loadimage3,
               highlightthickness=0,
               bd=0,
               command=createvenusWindow)


earthbtn=tk.Button(window,
                   image=loadimage4,
#width=25, размеры планеты
                   command=createearthWindow,bg = "white",
                   borderwidth=0,bd=0)


marsbtn=Button(window,
                   image=loadimage5,
                   command=createmarscWindow)
jupiterbtn=Button(window,
                   image=loadimage6,
                   command=createjupiterWindow)
saturnbtn=Button(window,
                   image=loadimage7,
                   command=createsaturnWindow)
uranusbtn=Button(window,
                   image=loadimage8,
                   command=createuranusWindow)
neptunebtn=Button(window,
                   image=loadimage9,
                   command=createneptuneWindow)
plutobtn=Button(window,
                   image=loadimage10,
                   command=createplutoWindow)







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


'''
sunbtn.place(x=750, y=350)
mercurybtn.place(x=500, y=350)

venusbtn.place(x=450, y=350)
earthbtn.place(x=400, y=350)

marsbtn.place(x=350, y=350)
jupiterbtn.place(x=300, y=350)

saturnbtn.place(x=250, y=350)
uranusbtn.place(x=200, y=350)

neptunebtn.place(x=150, y=350)
plutobtn.place(x=100, y=350)
'''

die()
#while True:
  #  i += 0.1
  #  mercurybtn.place(x=i, y=350)

#mercurybtn.place(x=i, y=350)
# sunbtn = Button(frame, bg='yellow')
# sunbtn.pack()

#window.mainloop()
