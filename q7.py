from tkinter import*
root=Tk()
fname=Entry(root)
fname.pack()
lname=Entry(root)
lname.pack()
def click():
    mylab=Label(root,text=fname.get()+"welcome to python")
    mylab.pack()
mylabel=Label(root,text="hello world")
mylabel.pack()
mybutton=Button(root,text="GO",command=click)
mybutton.pack()
root.configure(bg='aquamarine')
img=PhotoImage(file='starbus.png')
Label(root,image=img).pack()

root.mainloop()
