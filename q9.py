from tkinter import*
root=Tk()
def click2():
    display=Label(root,text="Nice job")
    display.pack()

def click():
    mylab=Button(root,text="new_button",command=click2)
    
    mylab.pack()
mylabel=Label(root,text="hello world")
mylabel.pack()
mybutton=Button(root,text="GO",command=click)
mybutton.pack()
root.configure(bg='aquamarine')
img=PhotoImage(file='starbus.png')
Label(root,image=img).pack()

root.mainloop()

