import translators as siroj
from tkinter import *
oyna=Tk()
oyna.title('Vaxobov Shoxruh')
oyna.geometry('1200x600')
oyna.resizable(0,0)
oyna.config(bg='#134769')
tt=Text(oyna,font=('monospace 25 bold'),width=63,height=5)
tt.place(x=30,y=300)

Label(oyna,bg='#134769',fg='#ffffff',text='Tillardan Uzb ga!',font=('monospace 40 bold')).place(x=440,y=20)
e1=Entry(oyna,font=('monospace 25 bold'),width=63,)

e1.place(x=30,y=100)
def tarjima():
      t=e1.get()
      a=siroj.google(t,from_language='auto',to_language='uz')
      tt.delete('1.0','end')
      tt.insert(END,a)

Button(oyna,command=tarjima,bg='#134769',fg='#ffffff',text=' Tarjimasi ',font=('monospace 30 bold')).place(x=500,y=150)

oyna.mainloop()
