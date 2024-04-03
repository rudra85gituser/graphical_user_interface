from tkinter import*
root=Tk()
def click():
    mylab=Label(root,text="welcome")
    mylab.pack()
mylabel=Label(root,text="hello world")
mylabel.pack()
mybutton=Button(root,text="GO",command=click)
mybutton.pack()



root.mainloop()
