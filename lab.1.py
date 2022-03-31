from tkinter import *
import math
# SINGLE_DISTANCE_X=30 #еденичный отрезок
WIDTH=1000
HEIGHT=600
PADDING=20
START_Y=0
STOP_Y=10
SINGLE_DISTANCE_Y=math.ceil((HEIGHT-3*PADDING)/(STOP_Y-START_Y+1))
if(START_Y*STOP_Y<=0):
    ZERO_POSITION_X=SINGLE_DISTANCE_Y*(-START_Y)+PADDING
else:
    ZERO_POSITION_X=PADDING
START_X=1
STOP_X=20
SINGLE_DISTANCE_X=math.ceil((WIDTH-3*PADDING)/(STOP_X-START_X+1))
if(START_X*STOP_X<=0):
    ZERO_POSITION_Y=SINGLE_DISTANCE_X*(-START_X)+PADDING
else:
    ZERO_POSITION_Y=PADDING
# def value_to_px(val):
#     return val*SINGLE_DISTANCE_X
window = Tk()  
window.title("грустная лаба номер один")  
window.geometry('1000x600') 
coord_system=Canvas(window,width=WIDTH,height=HEIGHT,bg="#FFFFFF")

def create_axis():
    coord_system.create_line(PADDING,HEIGHT-ZERO_POSITION_X,WIDTH-PADDING,HEIGHT-ZERO_POSITION_X,fill="#000000",width=3,arrow=LAST)
    coord_system.create_line(ZERO_POSITION_Y,HEIGHT-PADDING,ZERO_POSITION_Y,PADDING,fill="#000000",width=3,arrow=LAST)
    j=START_X
    # отметки на оси Х
    for i in range(PADDING,WIDTH-PADDING-SINGLE_DISTANCE_X,SINGLE_DISTANCE_X):
        coord_system.create_line(i,HEIGHT-ZERO_POSITION_X-5,i,HEIGHT-ZERO_POSITION_X+5,fill="#000000",width=2)
        coord_system.create_text(i,HEIGHT-ZERO_POSITION_X-0.5*PADDING,text=j,width=SINGLE_DISTANCE_X,justify='center')
        j+=1
    j=START_Y
        # отметки на оси У
    for i in range(HEIGHT-SINGLE_DISTANCE_Y,PADDING+SINGLE_DISTANCE_Y ,-SINGLE_DISTANCE_Y):
        coord_system.create_line(ZERO_POSITION_Y-5,i,ZERO_POSITION_Y+5,i,fill="#000000",width=2)
        coord_system.create_text(-0.5*PADDING+ZERO_POSITION_Y,i,text=j,width=PADDING-5,justify='left')
        j+=1
        # ноль
    # coord_system.create_text(PADDING,HEIGHT-0.5*PADDING,text=START_X,width=PADDING,justify='center')
    # coord_system.create_text(0.5*PADDING,HEIGHT-PADDING,text=START_Y,width=PADDING,justify='center')
def f1(x):
    return math.log(x)
def f2(x):
    return  math.log(x,10)
def plot1():
    for i in range(WIDTH-PADDING-SINGLE_DISTANCE_X):
        x=i/SINGLE_DISTANCE_X+START_X
        y=f1(x)-START_Y
        px_y=math.ceil(SINGLE_DISTANCE_Y*y)
        coord_system.create_oval(i+PADDING,HEIGHT-PADDING-px_y,i+PADDING,HEIGHT-PADDING-px_y,fill="blue",width=1,outline="blue")
        # print('{0} {1} {2} {3}'.format(x,y,i,px_y))
def plot2():
    for i in range(WIDTH-PADDING-SINGLE_DISTANCE_X):
        x=i/SINGLE_DISTANCE_X+START_X
        y=f2(x)-START_Y
        px_y=math.ceil(SINGLE_DISTANCE_Y*y)
        coord_system.create_oval(i+PADDING,HEIGHT-PADDING-px_y,i+PADDING,HEIGHT-PADDING-px_y,fill="red",width=1,outline="red")
create_axis()
plot1()
plot2()
# coord_system.create_oval(100,100,100,100,fill="blue",width=10)
print
coord_system.pack()
window.mainloop()