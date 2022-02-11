#Программа сделана Динь Вьет Ань, ИУ7-24Б

from tkinter import *
import tkinter.messagebox as box

key = ['1','0']

def calc():
    s = [x for x in innumEntry.get()]
    for x in s:
        if x not in key:
            box.showinfo('Error', 'Введите число снова')
            return
    if len(s) != 8:
        box.showinfo('Error', 'Введите число снова')
        return
    ans1Entry.delete(0,END)
    ans1Entry.insert(0,''.join(s))
    if s[0] == '1':
        for x in range(1, len(s)):
            s[x] = chr(ord('0') + 1 - int(s[x]))
    ans2Entry.delete(0,END)
    ans2Entry.insert(0,''.join(s))
    if s[0] == '1':
        for x in range(len(s)-1, 0, -1):
            if s[x] == '1':
                s[x] = '0'
            else:
                s[x] = '1'
                break
    ans3Entry.delete(0,END)
    ans3Entry.insert(0,''.join(s))

def showinfo1():
    box.showinfo('Info', 'Программа сделана Динь Вьет Ань.')

window = Tk()
window.geometry("600x400")

#Input
innumLabel = Label(window, text = 'Ввод')
innumEntry = Entry(window, width= 50)
innumLabel.place(x = 50, y = 0)
innumEntry.place(x = 100, y = 0)

#Output
ans1Label=Label(window,text='Прямый код')
ans1Entry=Entry(window, width = 40)
ans1Label.place(x = 50, y = 150)
ans1Entry.place(x = 200, y = 150)
ans2Label=Label(window,text='Обратный код')
ans2Entry=Entry(window, width = 40)
ans2Label.place(x = 50, y = 200)
ans2Entry.place(x = 200, y = 200)
ans3Label=Label(window,text='Дополнительный код')
ans3Entry=Entry(window, width = 40)
ans3Label.place(x = 50, y = 250)
ans3Entry.place(x = 200, y = 250)

calcButton=Button(window,text='Вычислить',command=calc)
calcButton.place(x = 200, y = 80)

#Menu
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label='File', menu = filemenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='О авторе', command=showinfo1)
menubar.add_cascade(label='Info', menu = infomenu)

window.config(menu=menubar)
window.mainloop()
