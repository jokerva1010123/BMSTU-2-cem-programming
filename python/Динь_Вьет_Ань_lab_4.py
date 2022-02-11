'''Программа сделана Динь Вьет Ань, ИУ7-24Б
    Данная программа создана для нахождения треугольника
    с вершинами – точками первого множества, внутри которого
    находится одинаковое количество точек из первого
    и из второго множеств.
'''
from tkinter import *
from tkinter import messagebox
from math import *

def clear():
    enter2Entry.delete(0, END)
    enter1Entry.delete(0, END)

def showinfo1():
    messagebox.showinfo("О авторе", "Программа сделана Динь Вьет Ань ИУ7-24Б")

def showinfo2():
    messagebox.showinfo("О программе", 'Данная программа создана для нахождения треугольника\n\
    с вершинами – точками первого множества, внутри которого\n\
    находится одинаковое количество точек\nиз первого\
    и из второго множеств.')

def list_get(enterEntry):
    try:
        list_a_b = [float(x) for x in enterEntry.get().strip().split()]
        if len(list_a_b) == 0 or isinstance(list_a_b, (str, type(None))) or len(list_a_b) % 2:
            messagebox.showerror('Error1', 'Проверьте введенные данные.')
            return 1, []
        return 0, list_a_b
    except:
        messagebox.showerror('Error2', 'Проверьте введенные данные.')
        return 1, []

def triangle(a, b, x, y, z):
    len1 = sqrt((a[x] - a[y]) ** 2 + (b[x] - b[y]) ** 2)
    len2 = sqrt((a[x] - a[z]) ** 2 + (b[x] - b[z]) ** 2)
    len3 = sqrt((a[z] - a[y]) ** 2 + (b[z] - b[y]) ** 2)
    return len1 + len2 > len3 and len1 + len3 > len2 and len2 + len3 > len1

def calc(a, b, c, d, x, y, z):
    s = fabs((a[z] - a[x]) * (b[y] - b[x]) - (b[z] - b[x]) * (a[y] - a[x]))/2
    print(a, b, c, d)
    cnt = 0
    for i in range(len(c)):
        s1 = fabs((a[z] - c[i]) * (b[y] - d[i]) - (b[z] - d[i]) * (a[y] - c[i]))/2
        s2 = fabs((c[i] - a[x]) * (b[y] - b[x]) - (d[i] - b[x]) * (a[y] - a[x]))/2
        s3 = fabs((a[z] - a[x]) * (d[i] - b[x]) - (b[z] - b[x]) * (c[i] - a[x]))/2
        if fabs(s - s1 - s2 - s3) <= 0.00001:
            cnt += 1
    return cnt

def draw(point1, point2, roots):
    point1_x = point1[::2]
    point1_y = point1[1::2]
    point2_x = point2[::2]
    point2_y = point2[1::2]
    all_point_x = point1_x + point2_x
    all_point_y = point1_y + point2_y
    if len(point1_x) < 3:
        messagebox.showerror('Error', 'Проверьте введенные данные.')
        return
    res = []
    for x in range(len(point1_x)):
        for y in range(x + 1, len(point1_x)):
            for z in range(y + 1, len(point1_x)):
                if not triangle(point1_x, point1_y, x, y, z):
                    continue
                cnt1 = calc(point1_x, point1_y, point1_x, point1_y, x, y, z) - 3
                cnt2 = calc(point1_x, point1_y, point2_x, point2_y, x, y, z)
                print(cnt1, cnt2)
                print(x,y, z)
                if cnt1 == cnt2 and cnt1 != 0:
                    res = [x, y, z]
                    break
            if res != []:
                break
        if res != []:
                break
    if res == []:
        messagebox.showinfo("Error", "Не найден треугольник")
        return
    draw_root = Toplevel(roots)
    draw_root['bg'] = '#d0f0c0'
    draw_root.grab_set()
    draw_root.geometry('600x710+500+0')
    draw_root.title('Triangle visualization')
    canv = Canvas(draw_root, width = 600, height = 600, bg = '#ffffcd')
    canv.pack()
    xmax = xmin = all_point_x[0]
    ymax = ymin = all_point_y[0]
    for i in range(len(all_point_x)):
        if all_point_x[i] > xmax:
            xmax = all_point_x[i]
        if all_point_x[i] < xmin:
            xmin = all_point_x[i]
        if all_point_y[i] > ymax:
            ymax = all_point_y[i]
        if all_point_y[i] < ymin:
            ymin = all_point_y[i]
    s_x = (600 - 50)/(xmax - xmin)
    s_y = (600 - 50)/(ymax - ymin)
    o_x = -xmin * s_x + 25
    o_y = -ymin * s_y + 25
    for i in range(len(point1_x)):
        x = point1_x[i] * s_x + o_x
        y = 600 - (point1_y[i] * s_y + o_y)
        canv.create_oval(x-6,y-6,x+6,y+6,fill='#b3007d')
    for i in range(len(point2_x)):
        x = point2_x[i] * s_x + o_x
        y = 600 - (point2_y[i] * s_y + o_y)
        canv.create_oval(x-6,y-6,x+6,y+6,fill='#42aaff')
    canv.create_line(point1_x[res[0]] * s_x + o_x, 600 - (point1_y[res[0]] * s_y + o_y), point1_x[res[1]] * s_x + o_x, 600 - (point1_y[res[1]] * s_y + o_y))
    canv.create_line(point1_x[res[2]] * s_x + o_x, 600 - (point1_y[res[2]] * s_y + o_y), point1_x[res[1]] * s_x + o_x, 600 - (point1_y[res[1]] * s_y + o_y))
    canv.create_line(point1_x[res[0]] * s_x + o_x, 600 - (point1_y[res[0]] * s_y + o_y), point1_x[res[2]] * s_x + o_x, 600 - (point1_y[res[2]] * s_y + o_y))
    r = Label(draw_root,text = 'Информация о точках\nФеолетовые точки - точки первого множества\nГолубые точки - точки второго множества',
                  font = 'consolas 12',bg = '#d0f0c0',fg = 'black')
    r.pack()
    exit_but =  Button(draw_root, text='Exit', font="consolas 12", command=draw_root.destroy)
    exit_but.pack()

def find():
    x, point1 = list_get(enter1Entry)
    if x:
        return
    y, point2 = list_get(enter2Entry)
    if y:
        return
    draw(point1, point2, roots)

def new():
    global root, c, xy1, xy2
    root = 0
    c1 = 0     
    xy1 = list()
    xy2 = list()

def paint(event):
    global xy1,c1
    python_green = "green"
    x1, y1 = (event.x - 6), (event.y - 6)
    x2, y2 = (event.x + 6), (event.y + 6)
    if event.widget != '.!canvas':
        return event
    xy1.append(event.x)
    xy1.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill=python_green)
    return event

def delt(event):
    global xy2,c1
    python_white = "blue"
    x1, y1 = (event.x - 6), (event.y - 6)
    x2, y2 = (event.x + 6), (event.y + 6)
    if event.widget != '.!canvas':
        return event
    xy2.append(event.x)
    xy2.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill=python_white, outline=python_white)
    return event
  
def special():
    global xy1, xy2,c1,root
    root = Tk()
    root['bg'] = '#aadaad'
    root.geometry('600x600')
    root.title("Geometric task")
    c1 = Canvas(root, width=400, height=400, bg="white")
    width = 400
    height = 400
    for line in range(0, width, 20):
        c1.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
    for line in range(0, height, 20):
        c1.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
    c1.pack()
    root.bind('<Button-1>', paint)
    root.bind('<Button-3>', delt)
    e_but =  Button(root, text='Visualization',
        font='consolas 12', command = lambda: draw(xy1, xy2, root))
    e_but.pack()
    exit_but =  Button(root, text='Exit',
            font='consolas 12', command=root.destroy)
    exit_but.pack()
    root.mainloop()

def draw_point():
    new()
    special()
    
roots = Tk()
roots.geometry('500x400')
roots.title('Triangle')

titleLabel = Label(roots, text = 'Нахождение треугольника по условию', font = 'consolas 14')
titleLabel.place(x = 90, y = 0)
enter1Label = Label(roots, text = 'Введите координаты точек первого множества', font = 'consolas 12')
enter1Label.place(x = 60, y = 50)
enter1Entry = Entry(roots, width= 70)
enter1Entry.place(x = 20, y = 90)
enter2Label = Label(roots, text = 'Введите координаты точек второй множества', font = 'consolas 12')
enter2Label.place(x = 60, y =110)
enter2Entry = Entry(roots, width= 70)
enter2Entry.place(x = 20, y = 150)

findButton = Button(roots, font = 'consolas 12', text='Find', command=find)
findButton.place(x = 205, y = 200)
paintButton = Button(roots, font = 'consolas 12', text='Paint points', command=draw_point)
paintButton.place(x = 170, y = 250)
clearButton = Button(roots, text="Clear", font="consolas 12", command=clear)
clearButton.place(x = 205, y = 300)
exitButton = Button(roots, font = 'consolas 12', text='Exit', command=roots.destroy)
exitButton.place(x = 205, y = 350)

menubar = Menu(roots)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=roots.destroy)
menubar.add_cascade(label='File', menu = filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Find", command=find)
editmenu.add_command(label="Paint point", command=draw_point)
editmenu.add_command(label="Clear all", command=clear)
menubar.add_cascade(label='Edit', menu = editmenu)
infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="About author", command=showinfo1)
infomenu.add_command(label="About program", command=showinfo2)
menubar.add_cascade(label="Info", menu = infomenu)
roots.config(menu=menubar)

roots.mainloop()