# Программа сделана Динь Вьет Ань, ИУ7-24Б
# Метод Шелла

from tkinter import *
import tkinter.messagebox as box
import random
import time

def randomnumber(numEntry, NEntry, rangelEntry, rangerEntry, num):
    numEntry.delete(0, END)
    if(NEntry.get() != ''):
        try:
            n1 = int(NEntry.get())
            if n1 <= 0:
                box.showinfo("Error", "Input N1 again")
                return 1
            if rangelEntry.get() == '' or rangerEntry.get() == '':
                box.showinfo("Error", "Input range")
                return 1
        except:
            box.showinfo("Error", "Input N1 again")
            return 1
    if rangelEntry.get() != '' and rangerEntry.get() != '':
        try:
            l = float(rangelEntry.get())
            r = float(rangerEntry.get())
            if l > r:
                box.showinfo("Error", "Range is wrong")    
                return 1
            if NEntry.get() == '':
                box.showinfo("Error", "Input N1")
                return 1
            try:
                a = []
                n1 = int(NEntry.get())
                for x in range(n1):
                    k = random.randint(l*10, r * 10)
                    a.append(str(1.0 * k / 10))
                numEntry.insert(0, ' '.join(a))
            except:
                box.showinfo("Error", "Input N1 again")
                return 1
        except:
            box.showinfo("Error", "Input range list" + str(num)+ 'again')
            return 1
    if((rangelEntry.get() != '' and rangerEntry.get() == '') or (rangelEntry.get() == '' and rangerEntry.get() != '')):
        box.showinfo("Error", "Input range")
        return 1
    return 0

def rand1():
    return randomnumber(list1Entry, N1Entry, range1lEntry, range1rEntry, 1)

def rand2():
    return randomnumber(list2Entry, N2Entry, range2lEntry, range2rEntry, 2)

def rand3():
    return randomnumber(list3Entry, N3Entry, range3lEntry, range3rEntry, 3)

def randall():
    if(rand1() != 1):
        if(rand2() != 1):
            rand3()

def clear1():
    N1Entry.delete(0, END)
    list1Entry.delete(0, END)
    range1lEntry.delete(0, END)
    range1rEntry.delete(0, END)

def clear2():
    N2Entry.delete(0, END)
    list2Entry.delete(0, END)
    range2lEntry.delete(0, END)
    range2rEntry.delete(0, END)

def clear3():
    N3Entry.delete(0, END)
    list3Entry.delete(0, END)
    range3lEntry.delete(0, END)
    range3rEntry.delete(0, END)

def init():
    n21Entry.delete(0, END)
    n11Entry.delete(0, END)
    n31Entry.delete(0, END)
    n22Entry.delete(0, END)
    n12Entry.delete(0, END)
    n32Entry.delete(0, END)
    n23Entry.delete(0, END)
    n13Entry.delete(0, END)
    n33Entry.delete(0, END)

def clearall():
    init()
    clear1()
    clear2()
    clear3()

def Shellsort(arr):
	inc=len(arr)//2
	while inc:
		for i,el in enumerate(arr):
			while i>=inc and arr[i-inc]>el:
				arr[i]=arr[i-inc]
				i-=inc
			arr[i]=el
		if inc==2:
			inc=1
		else:
			inc=int(inc*5.0/11)
	return arr

def count1(arr):
    temp_arr = sorted(arr)
    t0 = time.time()
    Shellsort(temp_arr)
    return time.time() - t0

def count2(arr):
    temp_arr = arr.copy()
    random.shuffle(temp_arr)
    t0 = time.time()
    Shellsort(temp_arr)
    return time.time() - t0

def count3(arr):
    temp_arr = sorted(arr)
    temp_arr.reverse()
    t0 = time.time()
    Shellsort(temp_arr)
    return time.time() - t0

def result(aaa, bbb):
    aaa.delete(0, END)
    aaa.insert(0, bbb)

def calc():
    init()
    if (list1Entry.get() != ''):
        list1 = list(map(float, list1Entry.get().split(' ')))
        result(n21Entry, count2(list1)*1000.0)
        result(n11Entry, count1(list1)*1000.0)
        result(n31Entry, count2(list1)*1000.0)
    if (list2Entry.get() != ''):
        list2 = list(map(float, list2Entry.get().split(' ')))
        result(n22Entry, count2(list2)*1000.0)
        result(n12Entry, count1(list2)*1000.0)
        result(n32Entry, count2(list2)*1000.0)
    if (list3Entry.get() != ''):
        list3 = list(map(float, list3Entry.get().split(' ')))
        result(n23Entry, count2(list3)*1000.0)
        result(n13Entry, count1(list3)*1000.0)
        result(n33Entry, count2(list3)*1000.0)

def showinfo1():
    box.showinfo('Info', 'Программа сделана Динь Вьет Ань.')

def showinfo2():
    box.showinfo('Info', 'Сортировка методом Шелла и вычисление время сортировки')

window = Tk()
window.geometry("1400x500")
window.configure(background='white')

N1Entry = Entry(window, width=5, borderwidth=2)
N1Label = Label(window, text = "N1 :", width=4, bg="white")
N1Label.config(font=("Arial", 12)) 
N2Entry = Entry(window, width=5, borderwidth=2)
N2Label = Label(window, text = "N2 :", width=4, bg="white")
N2Label.config(font=("Arial", 12))
N3Entry = Entry(window, width=5, borderwidth=2)
N3Label = Label(window, text = "N3 :", width=4, bg="white")
N3Label.config(font=("Arial", 12))
N1Label.place(x = 0, y = 10)
N2Label.place(x = 0, y = 40)
N3Label.place(x = 0, y = 70)
N1Entry.place(x = 50, y = 10)
N2Entry.place(x = 50, y = 40)
N3Entry.place(x = 50, y = 70)

list1Entry = Entry(window, width=120, borderwidth=2)
list1Label = Label(window, text = ";   list 1", width=5, bg="white")
list1Label.config(font=("Arial", 12)) 
list2Entry = Entry(window, width=120, borderwidth=2)
list2Label = Label(window, text = ";   list 2", width=5, bg="white")
list2Label.config(font=("Arial", 12)) 
list3Entry = Entry(window, width=120, borderwidth=2)
list3Label = Label(window, text = ";   list 3", width=5, bg="white")
list3Label.config(font=("Arial", 12)) 
list1Label.place(x = 90, y = 10)
list2Label.place(x = 90, y = 40)
list3Label.place(x = 90, y = 70)
list1Entry.place(x = 150, y = 10)
list2Entry.place(x = 150, y = 40)
list3Entry.place(x = 150, y = 70)

range1lEntry = Entry(window, borderwidth=2)
range1rEntry = Entry(window, borderwidth=2)
range2lEntry = Entry(window, borderwidth=2)
range2rEntry = Entry(window, borderwidth=2)
range3lEntry = Entry(window, borderwidth=2)
range3rEntry = Entry(window, borderwidth=2)
range1lEntry.place(x = 900, y = 10)
range1rEntry.place(x = 1050, y = 10)
range2lEntry.place(x = 900, y = 40)
range2rEntry.place(x = 1050, y = 40)
range3lEntry.place(x = 900, y = 70)
range3rEntry.place(x = 1050, y = 70)

rand1Button = Button(window, text = "randomize new", command = rand1, fg = 'purple')
rand2Button = Button(window, text = "randomize new", command = rand2, fg = 'purple')
rand3Button = Button(window, text = "randomize new", command = rand3, fg = 'purple')
clear1Button = Button(window, text = "clear", command = clear1, fg = 'red')
clear2Button = Button(window, text = "clear", command = clear2, fg = 'red')
clear3Button = Button(window, text = "clear", command = clear3, fg = 'red')
rand1Button.place(x = 1200, y = 10)
rand2Button.place(x = 1200, y = 40)
rand3Button.place(x = 1200, y = 70)
clear1Button.place(x = 1300, y = 10)
clear2Button.place(x = 1300, y = 40)
clear3Button.place(x = 1300, y = 70)

RandallButton = Button(window, text = "Randomize all", command = randall, fg = 'purple')
ClearallButton = Button(window, text= "Clear all", command = clearall, fg = 'red')
ExitButton = Button(window, text= "Exit", command=window.destroy)
CalcButton = Button(window, text = "Sort & Calculate time (milisec.)", fg = "Green", command = calc)
CalcButton.config(font=("Arial", 16)) 
CalcButton.place(x = 500, y = 120, height=50, width=300)
RandallButton.place(x = 10, y= 100)
ClearallButton.place(x = 10, y = 130)
ExitButton.place(x = 600, y = 400, width=200)

line1Label = Label(window, text = "Упорядоченный массив", bg="white")
line1Label.config(font=("Arial", 12)) 
line2Label = Label(window, text = "Случайный массив", bg="white")
line2Label.config(font=("Arial", 12)) 
line3Label = Label(window, text = "Обратно упорядоченный массив", bg="white")
line3Label.config(font=("Arial", 12))
line1Label.place(x = 10, y = 250)
line2Label.place(x = 10, y = 300)
line3Label.place(x = 10, y = 350)

n1Label = Label(window, text = "N1", width=4, bg="white")
n2Label = Label(window, text = "N2", width=4, bg="white")
n3Label = Label(window, text = "N3", width=4, bg="white")
n1Label.config(font=("Arial", 12))
n2Label.config(font=("Arial", 12))
n3Label.config(font=("Arial", 12))
n1Label.place(x = 500, y = 200)
n2Label.place(x = 700, y = 200)
n3Label.place(x = 900, y = 200)

n11Entry = Entry(window, bg="white", borderwidth=0)
n12Entry = Entry(window, bg="white", borderwidth=0)
n13Entry = Entry(window, bg="white", borderwidth=0)
n21Entry = Entry(window, bg="white", borderwidth=0)
n22Entry = Entry(window, bg="white", borderwidth=0)
n23Entry = Entry(window, bg="white", borderwidth=0)
n31Entry = Entry(window, bg="white", borderwidth=0)
n32Entry = Entry(window, bg="white", borderwidth=0)
n33Entry = Entry(window, bg="white", borderwidth=0)

n11Entry.place(x = 500, y = 250)
n12Entry.place(x = 700, y = 250)
n13Entry.place(x = 900, y = 250)
n21Entry.place(x = 500, y = 300)
n22Entry.place(x = 700, y = 300)
n23Entry.place(x = 900, y = 300)
n31Entry.place(x = 500, y = 350)
n32Entry.place(x = 700, y = 350)
n33Entry.place(x = 900, y = 350)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Calc", command=calc)
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label='File', menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
randommenu = Menu(editmenu, tearoff=0)
randommenu.add_command(label='Randomize list 1', command = rand1)
randommenu.add_command(label='Randomize list 2', command = rand2)
randommenu.add_command(label='Randomize list 3', command = rand3)
randommenu.add_command(label='Randomize all', command = randall)
editmenu.add_cascade(label="Randomize", menu = randommenu)
clearmenu = Menu(editmenu, tearoff=0)
clearmenu.add_command(label='Clear list 1', command = clear1)
clearmenu.add_command(label='Clear list 2', command = clear2)
clearmenu.add_command(label='Clear list 3', command = clear3)
clearmenu.add_command(label='Clear all', command = clearall)
editmenu.add_cascade(label="Clear", menu = clearmenu)
menubar.add_cascade(label='Edit', menu = editmenu)
infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='О авторе', command=showinfo1)
infomenu.add_command(label='О программе', command=showinfo2)
menubar.add_cascade(label='Info', menu = infomenu)
window.config(menu=menubar)

window.mainloop()