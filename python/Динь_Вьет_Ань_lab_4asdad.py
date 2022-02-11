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
    global c1, xy1, xy2
    c1.delete("all")
    width = 600
    height = 400
    for line in range(0, width, 20):
        c1.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
    for line in range(0, height, 20):
        c1.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

def showinfo1():
    messagebox.showinfo("О авторе", "Программа сделана Динь Вьет Ань ИУ7-24Б")

def showinfo2():
    messagebox.showinfo("О программе", 'Данная программа создана для нахождения треугольника\n\
    с вершинами – точками первого множества, внутри которого\n\
    находится одинаковое количество точек\nиз первого и из второго множеств.')

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
    cnt = 0
    for i in range(len(c)):
        s1 = fabs((a[z] - c[i]) * (b[y] - d[i]) - (b[z] - d[i]) * (a[y] - c[i]))/2
        s2 = fabs((c[i] - a[x]) * (b[y] - b[x]) - (d[i] - b[x]) * (a[y] - a[x]))/2
        s3 = fabs((a[z] - a[x]) * (d[i] - b[x]) - (b[z] - b[x]) * (c[i] - a[x]))/2
        if fabs(s - s1 - s2 - s3) <= 0.00001:
            cnt += 1
    return cnt

def draw(point1, point2, roots, canvas):
    clear()
    point1_x = point1[::2]
    point1_y = point1[1::2]
    point2_x = point2[::2]
    point2_y = point2[1::2]
    all_point_x = point1_x + point2_x
    all_point_y = point1_y + point2_y
    for x in range(len(point1_x)):
        x1, y1 = (point1_x[x] - 6), (point1_y[x] - 6)
        x2, y2 = (point1_x[x] + 6), (point1_y[x] + 6)
        canvas.create_oval(x1, y1, x2, y2, fill="#00ff00")
    for x in range(len(point2_x)):
        x1, y1 = (point2_x[x] - 6), (point2_y[x] - 6)
        x2, y2 = (point2_x[x] + 6), (point2_y[x] + 6)
        canvas.create_oval(x1, y1, x2, y2, fill="#FE09FF", outline="#ffffff")
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
    canvas.create_line(point1_x[res[0]], (point1_y[res[0]]), point1_x[res[1]], (point1_y[res[1]]))
    canvas.create_line(point1_x[res[2]], (point1_y[res[2]]), point1_x[res[1]], (point1_y[res[1]]))
    canvas.create_line(point1_x[res[0]], (point1_y[res[0]]), point1_x[res[2]], (point1_y[res[2]]))

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
    if str(event.widget) != ".!canvas":
        return event
    xy1.append(event.x)
    xy1.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill="#00ff00")
    return event

def delt(event):
    global xy2,c1
    python_white = "blue"
    x1, y1 = (event.x - 6), (event.y - 6)
    x2, y2 = (event.x + 6), (event.y + 6)
    if str(event.widget) != ".!canvas":
        return event
    xy2.append(event.x)
    xy2.append(event.y)
    c1.create_oval(x1, y1, x2, y2, fill="#FE09FF", outline="#ffffff")
    return event
    
roots = Tk()
roots.geometry('700x600')
roots.title('Triangle')
xy1 = []
xy2 = []
c1 = Canvas(roots, width=600, height=400, bg="white")
width = 600
height = 400
for line in range(0, width, 20):
    c1.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
for line in range(0, height, 20):
    c1.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
c1.place(x = 000, y = 0)
e_but =  Button(roots, text='Find',font='consolas 12', command = lambda: draw(xy1, xy2, roots, c1))
e_but.place(x = 300, y = 405)
exit_but =  Button(roots, text='Exit',font='consolas 12', command=roots.destroy)
exit_but.place(x = 300, y = 440)
roots.bind('<Button-1>', paint)
roots.bind('<Button-3>', delt)


roots.mainloop()
