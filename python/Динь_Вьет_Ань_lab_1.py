#Программа сделана Динь Вьет Ань, ИУ7-24Б
#Перевод заданного числа из 10-я сс в 6-ю и обратно

from tkinter import *
import tkinter.messagebox as box

def clearChoose():
    measure.set(0)

def clearall():
    innumEntry.delete(0, END)
    ansEntry.delete(0, END)
    measure.set(0)

def clearin():
    innumEntry.delete(0, END)

def clearout():
    ansEntry.delete(0, END)

def delete():
    t = innumEntry.get()
    innumEntry.delete(0, END)
    innumEntry.insert(0, t[:-1])

def button_add(num):
    innumEntry.insert(END, num)
    
def button_DEL():
    temp = innumEntry.get()
    innumEntry.delete(0,END)
    innumEntry.insert(0,temp[:-1])

def button_AC():
    innumEntry.delete(0,END)

def calc():
    if measure.get()==0:
        box.showinfo('Error', 'Не выбрал перевод.')
    else:
        if innumEntry.get() == '':
            box.showinfo('Error', 'Вводите число.')
            return
        instr = [i for i in innumEntry.get()]
        if ('-' in instr and (instr[0] != '-' or (instr[0] == '-' and len(instr) == 1)) or (instr[0] == '-' and instr[1] == '.')) or instr[0] == '.' or instr[-1] == '.' or instr.count('-') > 1 or instr.count('.') > 1:
            box.showinfo('Error', 'Вводите число снова')
            return
        t = ''
        if measure.get() == 1:
            if '.' in innumEntry.get():
                sb = [[], '']
                neg = 0
                remainder = [i for i in innumEntry.get().split('.')]
                remainder[0] = int(remainder[0])
                if remainder[0] < 0:
                    remainder[0] = -remainder[0]
                    neg = 1
                while remainder[0] >= 6:
                    sb[0].append(str(remainder[0] % 6))
                    remainder[0] //= 6
                sb[0].append(str(remainder[0]))
                sb[0].reverse()
                for x in sb[0]:
                    t = t + x
                sb[0]=t
                remainder[1] = float('0.'+str(remainder[1]))
                for i in range(10):
                    k = int(remainder[1]*6)
                    remainder[1] = remainder[1]*6-k
                    sb[1] = sb[1] + str(k)
                t='.'.join(sb)
                if neg:
                    t = '-' + t
            else:
                sb=[]
                neg = 0
                remainder = int(innumEntry.get())
                if remainder < 0:
                    remainder = -remainder
                    neg = 1
                while remainder >= 6:
                    sb.append(str(remainder % 6))
                    remainder //= 6
                sb.append(str(remainder))
                sb.reverse()
                for x in sb:
                    t = t + x
                if neg:
                    t = '-' + t
        else:
            if '.' in innumEntry.get():
                s = [i for i in innumEntry.get().split('.')]
                ans = 0
                neg = 0
                if int(s[0]) < 0:
                    s[0] = str(-int(s[0]))
                    neg = 1
                p = 1
                for x in range(len(s[0])):
                    ans += int(s[0][len(s[0]) - 1 - x]) * p
                    p *= 6
                    if int(s[0][x]) >= 6:
                        box.showinfo('Error', 'Вводите число снова')
                        return
                for i in range(len(s[1])):
                    ans+=int(s[1][i])*6**(-(i+1))
                    if int(s[1][i]) >= 6:
                        box.showinfo('Error', 'Вводите число снова')
                        return
                t = str(ans)
                if neg:
                    t = '-' + str(ans)
            else:
                s = innumEntry.get()
                ans = 0
                neg = 0
                if int(s) < 0:
                    s = str(-int(s))
                    neg = 1
                p = 1
                for x in range(len(s)):
                    ans += int(s[len(s) - 1 - x]) * p
                    p *= 6
                    if int(s[x]) >= 6:
                        box.showinfo('Error', 'Вводите число снова')
                        return
                t = str(ans)
                if neg:
                    t = '-' + str(ans)
        ansEntry.delete(0,END)
        ansEntry.insert(0,t)

def showinfo1():
    box.showinfo('Info', 'Программа сделана Динь Вьет Ань.')

def showinfo2():
    box.showinfo('Info', 'Перевод заданного числа из 10-й сс в 6-ю и обратно')

window = Tk()
window.geometry("600x400")

#Input
innumLabel = Label(window, text = 'Ввод')
innumEntry = Entry(window, width= 50)
innumLabel.place(x = 50, y = 0)
innumEntry.place(x = 100, y = 0)

#Choice
measure=IntVar()
change1=Radiobutton(window,text='Перевод из 10-й сс в 6-ю',variable=measure,value=1)
change2=Radiobutton(window,text='Перевод из 6-й сс в 10-ю',variable=measure,value=2)
change1.place(x = 50, y = 40)
change2.place(x = 350, y = 40)

#ClearButton
clearinButton = Button(window,text='Clear',command=clearin)
delButton = Button(window,text='Del',command=delete)
clearoutButton = Button(window,text='Clear',command=clearout)
clearinButton.place(x = 450, y = 0)
delButton.place(x = 500, y = 0)
clearoutButton.place(x = 450, y = 150)
clearChoiceButton=Button(window,text='Clear Choice',command=clearChoose)
clearChoiceButton.place(x = 200, y = 80)

#Output
ansLabel=Label(window,text='Результат')
ansEntry=Entry(window, width = 40)
ansLabel.place(x = 50, y = 150)
ansEntry.place(x = 150, y = 150)

#NumberButton
btn1 = Button(window,text = '1', command =lambda: button_add('1'))
btn2 = Button(window,text = '2', command =lambda: button_add('2'))
btn3 = Button(window,text = '3', command =lambda: button_add('3'))
btn4 = Button(window,text = '4', command =lambda: button_add('4'))
btn5 = Button(window,text = '5', command =lambda: button_add('5'))
btn6 = Button(window,text = '6', command =lambda: button_add('6'))
btn7 = Button(window,text = '7', command =lambda: button_add('7'))
btn8 = Button(window,text = '8', command =lambda: button_add('8'))
btn9 = Button(window,text = '9', command =lambda: button_add('9'))
btn0 = Button(window,text = '0', command =lambda: button_add('0'))
btnMinus = Button(window,text = '-', command =lambda: button_add('-'))
btnDEL = Button(window,text = 'DEL', command = button_DEL)
btnAC = Button(window,text = 'AC', command = button_AC)
btndot = Button(window,text = '.', command =lambda:  button_add('.'))
btnequal = Button(window,text = '=', command = calc)
calcButton=Button(window,text='Вычислить',command=calc)

btn1.place(x = 100, y = 200, width=50)
btn2.place(x = 200, y = 200, width=50)
btn3.place(x = 300, y = 200, width=50)
btn4.place(x = 100, y = 250, width=50)
btn5.place(x = 200, y = 250, width=50)
btn6.place(x = 300, y = 250, width=50)
btn7.place(x = 100, y = 300, width=50)
btn8.place(x = 200, y = 300, width=50)
btn9.place(x = 300, y = 300, width=50)
btnMinus.place(x = 100, y = 350, width=50)
btn0.place(x = 200, y = 350, width=50)
btndot.place(x = 300, y = 350, width=50)
btnequal.place(x = 400, y = 200, width=50)
btnDEL.place(x = 400, y = 250, width=50)
btnAC.place(x = 400, y = 300, width=50)
calcButton.place(x = 400, y = 350)

#Menu
menubar = Menu(window)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.destroy)
menubar.add_cascade(label='File', menu = filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Clear input', command=clearin)
editmenu.add_command(label='Clear output', command=clearout)
editmenu.add_command(label='Clear choice', command=clearChoose)
editmenu.add_command(label='Clear all', command=clearall)
menubar.add_cascade(label='Edit', menu = editmenu)

infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label='О авторе', command=showinfo1)
infomenu.add_command(label='О программе', command=showinfo2)
menubar.add_cascade(label='Info', menu = infomenu)

window.config(menu=menubar)
window.mainloop()
