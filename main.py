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


window.configure(background="black")
frame = Frame(window, bg='black')

background_image = tk.PhotoImage(file="sky.png")
title = Label(window, image=background_image,highlightthickness=0, bd=0)
title.pack()




loadimage = tk.PhotoImage(file="4OKd.gif")
loadimage2 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage3 = tk.PhotoImage(file="4OKd.gif")
loadimage4 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage5 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage6 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage7 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage8 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage9 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")
loadimage10 = tk.PhotoImage(file="imgonline-com-ua-Resize-Nd7vFQJ5pWqd.png")



#window.overrideredirect(True)
#window.geometry("+250+250")
#window.wm_attributes("-topmost", True)
#window.wm_attributes("-disabled", True)
window.wm_attributes("-transparentcolor", "white") # -- фон_белый



sunbtn =Button(window,
                   image=loadimage,
#width=25, размеры планеты
                   command=createearthWindow,bg = "white",
                   borderwidth=0,bd=0)
mercurybtn=Button(window,
                   image=loadimage2,
                   command=createmercuryWindow)

venusbtn=Button(window,
               image=loadimage2,
               highlightthickness=0,
               bd=0,
               command=createsunWindow)


earthbtn=tk.Button(window,
                   image=loadimage2,
#width=25, размеры планеты
                   command=createearthWindow,bg = "white",
                   borderwidth=0,bd=0)


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
