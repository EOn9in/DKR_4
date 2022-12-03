from tkinter import *
from tkinter import messagebox
from math import *
import matplotlib.pyplot as plt
import numpy as np


def function(x):
    f = x**3 + x**2 + 5*x + 3
    return f


def pervoobraznaya(x):
    per = (x**4)/4 + (x**3)/3 + 2.5*x**2 + 3*x
    return per


def integrel():
    a = int(aa.get())
    b = int(bb.get())
    n = int(nn.get())
    h = (b-a)/n
    s = (function(a)+function(b))/2
    x = a+h
    for i in range(n-1):
        s += function(x)
        x += h
    s *= h
    p = pervoobraznaya(b)-pervoobraznaya(a)
    messagebox.showinfo('Результат', f"Точное значение = {p}")


def trap():
    a = int(aa.get())
    b = int(bb.get())
    n = int(nn.get())
    h = (b-a)/n
    s = (function(a)+function(b))/2
    x = a+h
    for i in range(n-1):
        s += function(x)
        x += h
    s *= h
    p = pervoobraznaya(b)-pervoobraznaya(a)
    messagebox.showinfo('Результат', f"Приближённое значение (метод трапеций) ≈ {s}",
                        detail=f'Погрешность метода = {abs(p-s)}')
 

def grafic():
    a = int(aa.get())
    b = int(bb.get())
    n = int(nn.get())
    fig, ax = plt.subplots()
    ax.set_title('График функции: y=x^3+x^2+5*x+3')
    ax.grid(True)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("center")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_aspect("equal")
    x = np.linspace(-100, 100, 500)
    y = function(x)
    plt.ylabel("Ось X",labelpad = 110)
    plt.xlabel("Ось Y",labelpad = 120)
    h = (b-a)/n
    x1 = a+h
    ax.vlines(a,0,function(a),color = 'r')
    ax.text(a-0.3,-0.5,'a',color ='r')
    for i in range(n):
        if x1==b:
            ax.vlines(x1,0,function(x1),linestyle='dashed',color = 'r')
        else:
            ax.vlines(x1,0,function(x1),color = 'r')
        x1+=h
    ax.text(x1-h,-0.6,'b',color ='r')
    ax.text(2,-8,f'Кол-во трапеций: {n} \nРасстояние между линиями ≈ {h}',color = '#0000CD')
    ax.plot(x,y)
    plt.show()

def ExitApp():
    MsgBox = messagebox.askquestion(
        'Выход из программы', 'Вы уверены, что хотите выйти?', icon='error')
    if MsgBox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('С возвращением!',
                            'Мы рады, что вы остались с нами!')


root = Tk()
root.title("Вычисление площади фигуры, ограниченной кривой")
root.geometry("675x450")

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

label = Label(frame, text='Задание (Вариант 12):', font=("Arial", 14))
label.pack()
label_1 = Label(
    frame, text='1. Реализовать программу вычисления площади фигуры, ограниченной кривой 1*x^3+(1)*x^2+(5)*x+(3) и осью ОХ.')
label_1.pack()
label_2 = Label(
    frame, text='2. Вычисление определенного интеграла должно выполняться численно, с применением метода трапеций')
label_2.pack()
label_3 = Label(
    frame, text='3. Пределы интегрирования вводятся пользователем.')
label_3.pack()
label_4 = Label(
    frame, text='4. Взаимодействие с пользователем должно осуществляться посредством case-меню.')
label_4.pack()
label_5 = Label(
    frame, text='5. Требуется реализовать возможность оценки погрешности полученного результата.')
label_5.pack()
label_6 = Label(
    frame, text='6. Необходимо использовать процедуры и функции там, где это целесообразно.')
label_6.pack()

button = Button(frame, text="Понятно!", command=lambda: button.pack_forget())
button.pack()

a = Label(frame, text="Введите точку а (a<b)")
a.pack()

aa = Entry(frame)
aa.pack()

b = Label(frame, text="Введите точку b")
b.pack()

bb = Entry(frame)
bb.pack()

n = Label(frame, text="Введите количество разбиений (n)")
n.pack()

nn = Entry(frame)
nn.pack()

btn = Button(frame, text='Расчитать точное значение', command=integrel)
btn.pack(fill=X)

butn = Button(frame, text='Вычислить методом трапеций', command=trap)
butn.pack(fill=X)

buttn = Button(frame, text='График', command=grafic)
buttn.pack(fill=X)

buttonEg = Button(frame, text='Выход', command=ExitApp)
buttonEg.pack(anchor=SE)


def motionUP(event):
    children = frame.winfo_children()
    if event.widget in children:
        index = children.index(event.widget)
        index -= 1
        if index > -1:
            children[index].focus_set()


def motionDOWN(event):
    children = frame.winfo_children()
    if event.widget in children:
        index = children.index(event.widget)
        index += 1
        if index < len(children):
            children[index].focus_set()


root.bind('<Up>', motionUP)
root.bind('<Down>', motionDOWN)


root.mainloop()
