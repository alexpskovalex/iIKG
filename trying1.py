from tkinter import *  
# from tkinter import Menu  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('800x500') 
menu = Menu(window)  
new_item = Menu(menu)  
new_item.add_command(label='Новый')  
menu.add_cascade(label='Файл', menu=new_item)  
window.config(menu=menu)  
window.mainloop()