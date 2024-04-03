from tkinter import*
root=Tk()
amount=Entry(root)
amount.pack()
rate=Entry(root)
rate.pack()
time=Entry(root)
time.pack()

def click():
    mylab=Label(root,text=int(amount.get())*int(rate.get())*int(time.get())/100)
    mylab.pack()
mylabel=Label(root,text="hello world")
mylabel.pack()
mybutton=Button(root,text="GO",command=click)
mybutton.pack()
root.configure(bg='aquamarine')
img=PhotoImage(file='starbus.png')
Label(root,image=img).pack()

root.mainloop()
