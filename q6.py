from tkinter import*
root=Tk()
e=Entry(root)
e.pack()
def click():
    mylab=Label(root,text="welcome")
    mylab.pack()
mylabel=Label(root,text="hello world")
mylabel.pack()
mybutton=Button(root,text="GO",command=click)
mybutton.pack()
root.configure(bg='aquamarine')
img=PhotoImage(file='starbus.png')
Label(root,image=img).pack()

root.mainloop()
