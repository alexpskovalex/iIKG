from tkinter import *
import math as m

window = Tk()
window.title("грустная лаба номер один")
window.geometry('1000x600')
coord_system = Canvas(window, width=2000, height=1200, bg="#FFFFFF")


def rotate():
    # point_list.pop(-1)
    print(point_list)
    deg=float(ent_deg.get())
    radian=deg/180*3.14
    # i=0
    # point_list[i][0]=rotate_center[0]+ (point_list[i][0]-rotate_center[0])*m.cos(radian) - (point_list[i][1]-rotate_center[1])*m.sin(radian)
    # point_list[i][1]=rotate_center[1]+ (point_list[i][0]-rotate_center[0])*m.sin(radian) + (point_list[i][1]-rotate_center[1])*m.cos(radian)
    for i in range(0, len(point_list)):
        point_list[i]=[\
            rotate_center[0]+ (point_list[i][0]-rotate_center[0])*m.cos(radian) - (point_list[i][1]-rotate_center[1])*m.sin(radian),\
            rotate_center[1]+ (point_list[i][0]-rotate_center[0])*m.sin(radian) + (point_list[i][1]-rotate_center[1])*m.cos(radian)\
                ]
        # point_list[i][1]=rotate_center[1]+ (point_list[i][0]-rotate_center[0])*m.sin(radian) + (point_list[i][1]-rotate_center[1])*m.cos(radian)
        coord_system.create_oval(point_list[i][0],
                                 point_list[i][1],
                                 point_list[i][0],
                                 point_list[i][1],
                                 fill="red",
                                 width=8,
                                 outline="red")
    for i in range(0, len(point_list)):
        coord_system.create_line(point_list[i-1][0],
                                 point_list[i-1][1],
                                 point_list[i][0],
                                 point_list[i][1],
                                 fill="#000000",
                                 width=2)
    # print(point_list)

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
        # prev_point[0] = event.x
        # prev_point[1] = event.y
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


def set_rotate_scenter(event):
    print("set_rotate_scenter at {0} {1}".format(event.x, event.y))
    rotate_center[0] = event.x
    rotate_center[1] = event.y
    coord_system.create_oval(event.x,
                             event.y,
                             event.x,
                             event.y,
                             fill="blue",
                             width=10,
                             outline="blue")
    coord_system.unbind("<Button-3>")


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
coord_system = Canvas(window, width=2000, height=900, bg="#FFFFFF")
coord_system.pack()
coord_system.bind("<Button-1>", set_point)
coord_system.bind("<Button-3>", set_rotate_scenter)
window.mainloop()