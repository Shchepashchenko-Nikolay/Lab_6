from tkinter import *
import tkinter as tk




def createsunWindow():
    newWindow = Toplevel(window)

    labelExample = Label(newWindow, text="Со́лнце (астр. ☉) — одна из звёзд нашей Галактики (Млечный Путь) "
                                         "и единственная звезда Солнечной системы. Вокруг Солнца обращаются другие объекты этой системы: планеты и их спутники, карликовые планеты и их спутники, астероиды, метеороиды, кометы и космическая пыль.")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample.pack()
def createmercuryWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createvenusWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createearthWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createmarscWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createjupiterWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createsaturnWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createuranusWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createneptuneWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()
def createplutoWindow():
    newWindow = Toplevel(window)

    labelExample2 = Label(newWindow, text="merc very big")
   # buttonExample = Button(newWindow, text="New Window button")

    labelExample2.pack()





window = Tk()  # создание окна
photo = tk.PhotoImage(file="zvezdnoe_nebo_noch_temnyj_152039_3840x2160.png")
 #photo = tk.PhotoImage(file = "zvezdnoe_nebo_noch_temnyj_152039_3840x2160.jpg")

window['bg'] = 'black'  # типо фон черный

window.title('lab6')  # name of programm
# Указываем размеры окна
window.geometry('1680x1050')
# Делаем невозможным менять размеры окна
window.resizable(width=False, height=False)

# canvas = Canvas(window, height=1280, width=720)
# canvas.pack()

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame = Frame(window, bg='black')
#frame.place(relx=0.1, rely=0.21, relwidth=0.2, relheight=0.1)

title = Label(frame)
title.pack()




loadimage = tk.PhotoImage(file="89146_sun_icon.png")
loadimage2 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage3 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage4 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage5 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage6 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage7 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage8 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage9 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage10 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")




sunbtn =Button(window,
               image=loadimage,
               command=createsunWindow)
mercurybtn=Button(window,
                   image=loadimage2,
                   command=createmercuryWindow)

venusbtn=Button(window,
                   image=loadimage2,
                   command=createvenusWindow)
earthbtn=Button(window,
                   image=loadimage2,
                   command=createearthWindow)
marsbtn=Button(window,
                   image=loadimage2,
                   command=createmarscWindow)
jupiterbtn=Button(window,
                   image=loadimage2,
                   command=createjupiterWindow)
saturnbtn=Button(window,
                   image=loadimage2,
                   command=createsaturnWindow)
uranusbtn=Button(window,
                   image=loadimage2,
                   command=createuranusWindow)
neptunebtn=Button(window,
                   image=loadimage2,
                   command=createneptuneWindow)
plutobtn=Button(window,
                   image=loadimage2,
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


#while True:
  #  i += 0.1
  #  mercurybtn.place(x=i, y=350)

#mercurybtn.place(x=i, y=350)
# sunbtn = Button(frame, bg='yellow')
# sunbtn.pack()

window.mainloop()
