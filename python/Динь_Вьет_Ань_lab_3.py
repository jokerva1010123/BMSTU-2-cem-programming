# Программа сделана Динь Вьет Ань, ИУ7-24Б
# С помощью Брента

from tkinter import *
from scipy import optimize
import tkinter.messagebox as box
import matplotlib.pyplot as plt
from math import sin, cos
import numpy as np

def fi(x):
    return cos(x)

def F(x):
    return sin(x)

def check():
    try:
        l, r = map(float, rangeEntry.get().strip().split())
        eps = float(epsEntry.get())
        maxiter = int(iterEntry.get())
        h = float(stepEntry.get())
        if l >= r or eps > h/2 or eps < 0 or h < 0 or maxiter <= 0:
            box.showinfo('Error', 'Проверьте введенные данные')    
            return 1
        return 0
    except:
        box.showinfo('Error', 'Проверьте введенные данные')
        return 1

def clear():
    rangeEntry.delete(0, END)
    iterEntry.delete(0, END)
    stepEntry.delete(0, END)
    epsEntry.delete(0, END)

def init():
    n_list = list()
    x_list = list()
    fx_list = list()
    left_l = list()
    right_l = list()
    error_list = list()
    n = 1
    l, r = map(float, rangeEntry.get().strip().split())
    eps = float(epsEntry.get())
    maxiters = int(iterEntry.get())
    h = float(stepEntry.get())
    while l + (n - 1) * h <= r:
        a = l + (n - 1) * h
        b = l + n * h if l + n * h <= r else r
        if F(a) * F(b) <= 0:
            try:
                x = optimize.bisect(F, a, b, maxiter=maxiters)
                if (len(x_list) == 0 or abs(x - x_list[-1]) > 2 * eps):
                    n_list.append(n)
                    x_list.append(x)
                    fx_list.append(F(x))
                    left_l.append(a)
                    right_l.append(b)
                    for i in range(maxiters, 0, -1):
                        try:
                            x = optimize.bisect(F, a, b, maxiter=i)
                        except:
                            error_list.append([i+1,0])
            except:
                for i in range(maxiters+1, 100000):
                    try:
                        x = optimize.bisect(F, a, b, maxiter = i)
                        if (len(x_list) == 0 or abs(x - x_list[-1]) > 2 * eps):
                            n_list.append(n)
                            x_list.append(x)
                            fx_list.append(F(x))
                            left_l.append(a)
                            right_l.append(b)
                            error_list.append([i, 1])
                        break
                    except: 
                        pass

        n += 1
    return n_list, x_list, fx_list, left_l, right_l, error_list

def findroot():
    all_roots = init()
    if all_roots:
        if not len(all_roots[0]):
            box.showinfo('Корни не найдены', 'Корни не найдены на заданном интервале')
        else:
            root = Toplevel(window)
            root.focus_set()
            root.geometry('600x500+700+100')
            root.title('Таблица')
            w_window_l = Label(root,text = 'Таблица приближенных корней, найденных на интервале')
            w_window_l.place(x=300,y=25,anchor ='center')
            n_label = Label(root, text = ' № ', fg = 'black')
            n_label.place(x=5,y=50)
            a_b_label = Label(root, text = '       [a,b]       ', fg = 'black')
            a_b_label.place(x=55,y=50)
            x_label = Label(root, text = '     x      ' , fg = 'black')
            x_label.place(x=180,y=50)
            fx_label = Label(root, text = '      F(x)     ', fg = 'black')
            fx_label.place(x=275,y=50)
            iter_label = Label(root, text = 'Кол-во итераций', fg = 'black')
            iter_label.place(x=390,y=50)              
            err_label = Label(root, text = 'Код ошибки', fg = 'black')
            err_label.place(x=505,y=50)
            for i in range(len(all_roots[0])):
                n_label = Label(root, text = '{:3d}'.format(i+1))
                n_label.place(x=5,y=50+30*(i+1))
                a_b_label = Label(root, text = '[{:8.4f};{:8.4f}]'.format(all_roots[3][i],all_roots[4][i]))
                a_b_label.place(x=35,y=50+30*(i+1))
                x_label = Label(root, text = '{:12.5f}'.format(all_roots[1][i]))
                x_label.place(x=180,y=50+30*(i+1))
                fx_label = Label(root, text = '{:15.0e}'.format(all_roots[2][i]))
                fx_label.place(x=275,y=50+30*(i+1))
                iter_label = Label(root, text = '{:15.0f}'.format(all_roots[5][i][0]))
                iter_label.place(x=390,y=50+30*(i+1))              
                err_label = Label(root, text = '{:10.0f}'.format(all_roots[5][i][1]))
                err_label.place(x=505,y=50+30*(i+1))
            error_code_j = Button(root, text='Код ошибки',
                                  width = 15,height = 1,
                                  bg = 'white',fg = 'black',
                                  command=lambda:box.showinfo\
                                  ('Код ошибки','0 - нет ошибки\n\
1 - кол-во итераций больше максимального'))
            error_code_j.place(x=10,y = 50+45*len(all_roots[0]))
    return all_roots

def draw():
    if check():
        return
    all_roots = findroot()
    d = [float(x) for x in rangeEntry.get().split()]
    x = np.linspace(d[0],d[1],500000)
    y = np.sin(x)
    plt.cla()
    plt.title('$sin(x)$')
    plt.grid(True)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot(x,y,'b')
    extr_list_x = list()
    extr_list_y = list()
    for i in range(1,499999):
        if abs(fi(x[i]))<= 0.0001 and fi(x[i-1])*fi(x[i+1]):
            extr_list_x.append(x[i])
            extr_list_y.append(F(x[i]))
    plt.scatter(extr_list_x,extr_list_y,color = 'red',label='Extremums')
    plt.scatter(all_roots[1],all_roots[2],color = 'green',label='Roots')
    plt.legend(loc = 'lower left')
    plt.show()

window = Tk()
window.geometry("460x400")
window['bg'] = '#adf0cd'

nameLabel = Label(window, text = "Нахождниe корней функции (sin(x)) с помощью Брента", font = 'consolas 13', fg = 'black')
nameLabel.place(x = 0, y = 0)

rangeLabel = Label(window, text = "Левая и правая граница\n(через пробел)", bg = '#adf0cd')
rangeLabel.place(x = 50, y = 100)
rangeEntry = Entry(window, width = 30)
rangeEntry.place(x = 230, y = 100)

stepLabel = Label(window, text = "Шаг", bg = "#adf0cd")
stepLabel.place(x = 100, y = 150)
stepEntry = Entry(window, width = 30)
stepEntry.place(x = 230, y = 150)

iterLabel = Label(window, text = "Максимальное количество\nитераций", bg = "#adf0cd")
iterLabel.place(x = 30, y = 180)
iterEntry = Entry(window, width = 30)
iterEntry.place(x = 230, y = 190)

epsLabel = Label(window, text = "Точность", bg = '#adf0cd')
epsLabel.place(x = 80, y = 220)
epsEntry = Entry(window, width = 30)
epsEntry.place(x = 230, y = 220)

calcButton = Button(window, text = 'Ввод данных', command = draw)
calcButton.place(x = 50, y = 300)
drawButton = Button(window, text = "Очистить", command = clear)
drawButton.place(x = 180, y = 300)
exitButton = Button(window, text = 'Выход', command = window.destroy)
exitButton.place(x = 350, y = 300)

window.mainloop()