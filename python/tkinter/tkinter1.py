import tkinter
import sys
mw=tkinter.Tk()
b1=tkinter.Button(mw,text='MyButton')
b1.pack()
c=tkinter.Canvas(mw)
b2=tkinter.Button(mw,text='MyButton' )
b2.pack(side=tkinter.RIGHT)
c.create_line(10,10,100,100,300,200,10,10)
c.pack()
tkinter.mainloop()