from tkinter import *
import math as m

window = Tk()
window.title("грустная лаба номер один")
window.geometry('1000x600')
coord_system = Canvas(window, width=1000, height=600, bg="#FFFFFF")
def check_cross(x1,y1,x2,y2):
    for i in range (len(point_list)):
        k1=(y2-y1)/(x2-x1)
        k2=(point_list[i][1]-point_list[i-1][1])/(point_list[i][0]-point_list[i-1][0])
        b1=y1-k1*x1
        b2=point_list[i-1][1]-k2*point_list[i-1][0]
        x_cross=(b2-b1)/(k1-k2)
        if ((x_cross>x1) and (x_cross<x2)) or ((x_cross<x1) and (x_cross>x2)):
            return True
    return False

# point_list=[[2.1,2.1],[2,4],[4.1,4.1],[4,2]]
# print(check_cross(1,0,1.1,1))
# exit()
def rotate():
    # point_list.pop(-1)
    print(point_list)
    while len(point_list)>3:# пока больще 3 вершин - отделяем по одной
        i=0 #перебираю возможности отрезать тточку
        while check_cross(point_list[i-1][0],point_list[i-1][1],point_list[i+1][0],point_list[i+1][1]):#пока есть точки пересечения(check_cross возращзает True)
            i+1
            if(i==len(point_list)):#если не найдет точки то выведет ошибку
                print('ну тут пиздец какой-то так не должно быть')
                break
        #а если все же най
global first_point
global prev_point
# global firtst_point_element
# firtst_point_element=None
first_point = [None, None]
prev_point = [None, None]
rotate_center = [None, None]
point_list = []


def finish_construct(event):
    coord_system.create_line(prev_point[0],
                             prev_point[1],
                             first_point[0],
                             first_point[1],
                             fill="#000000",
                             width=2)
    print("ayaya")
    coord_system.unbind("<Button-1>")


def set_point(event):
    if first_point[0] == None:
        first_point[0] = event.x
        first_point[1] = event.y
        firtst_point_element = coord_system.create_oval(event.x,
                                                        event.y,
                                                        event.x,
                                                        event.y,
                                                        fill="red",
                                                        width=12,
                                                        outline="red")
        coord_system.tag_bind(firtst_point_element, '<Button-1>',
                              finish_construct)
        prev_point[0] = event.x
        prev_point[1] = event.y
    else:
        coord_system.create_oval(event.x,
                                 event.y,
                                 event.x,
                                 event.y,
                                 fill="red",
                                 width=8,
                                 outline="red")
        coord_system.create_line(prev_point[0],
                                 prev_point[1],
                                 event.x,
                                 event.y,
                                 fill="#000000",
                                 width=2)
        prev_point[0] = event.x
        prev_point[1] = event.y
    point_list.append([event.x, event.y])
    print(point_list)

def create_gui():
    lbl_main = Label(window, text="постройте замкнутый многоугольник ")
    lbl_main.pack(side=TOP)
    global ent_deg
    frm_deg = Frame(window)
    ent_deg = Entry(frm_deg, width=30)
    lbl_deg = Label(frm_deg, text="введите угол\n поворота(deg)")
    global btn_deg
    btn_deg = Button(frm_deg, text="повернуть", command=rotate)
    lbl_deg.pack(side='left')
    ent_deg.pack(side='left')
    btn_deg.pack(side='left')
    frm_deg.pack(anchor="nw")


create_gui()
coord_system = Canvas(window, width=500, height=300, bg="#FFFFFF")
coord_system.pack()
coord_system.bind("<Button-1>", set_point)
# coord_system.bind("<Button-3>", set_rotate_scenter)
window.mainloop()