from tkinter import *


def createNewWindow():
    newWindow = Toplevel(window)
    labelExample = Label(newWindow, text="солнце это солнце,солнце это она она планета")
    #buttonExample = Button(newWindow, text="New Window button")

    labelExample.pack()
    buttonExample.pack()


window = Tk()  # создание окна

# photo = PhotoImage(file = "zvezdnoe_nebo_noch_temnyj_152039_3840x2160.jpg")

window['bg'] = 'black'  # типо фон черный

window.title('sun_sys')  # name of programm
# Указываем размеры окна
window.geometry('1280x720')
# Делаем невозможным менять размеры окна
window.resizable(width=False, height=False)

# canvas = Canvas(window, height=1280, width=720)
# canvas.pack()

# Создаем фрейм (область для размещения других объектов)
# Указываем к какому окну он принадлежит, какой у него фон и какая обводка
frame = Frame(window, bg='black')
frame.place(relx=0.61, rely=0.21, relwidth=0.2, relheight=0.1)

title = Label(frame)
title.pack()

sunbtn =Button(window,
                   text="кнопочка (нажать) она должна быть круглой (иконкой) и кружиться по кругу(планетаже)",
                   command=createNewWindow)
sunbtn.pack()

# sunbtn = Button(frame, bg='yellow')
# sunbtn.pack()

window.mainloop()
