from tkinter import*
from tkinter import messagebox
root=Tk()
root.title('demo3')
root.configure(bg='purple')
root.geometry('300x300')
font='Arial 50'
#branch
branch=IntVar()
Label(root,text='select your branch').grid(row=1,column=1)
Radiobutton(root,text='cse',variable=branch,value=1).grid(row=1,column=2)
Radiobutton(root,text='ece',variable=branch,value=2).grid(row=1,column=3)
Radiobutton(root,text='machenical',variable=branch,value=3).grid(row=1,column=4)
def fun():
    Label(root,text=branch.get()).grid(row=1,column=6)
Button(root,text='click',command=fun).grid(row=1,column=5)
#checkbutton
branch1=IntVar()
branch2=IntVar()
branch3=IntVar()
branch4=IntVar()
Checkbutton(root,text='one',variable=branch1,onvalue=1).grid(row=2,column=2)
Checkbutton(root,text='second',variable=branch2,onvalue=2).grid(row=2,column=3)
Checkbutton(root,text='third',variable=branch3,onvalue=3).grid(row=2,column=4)
Checkbutton(root,text='four',variable=branch4,onvalue=4).grid(row=2,column=5)
def fun2():
    Label(root,text=branch1.get()+branch2.get()+branch3.get()+branch4.get()).grid(row=2,column=6)
Button(root,text='click for sum',command=fun2).grid(row=2,column=1)
#option menu
op=StringVar()
op.set('select your branch')
option=['cse','ece','mac','civ']
OptionMenu(root,op,*option).grid(row=3,column=3)
def fun3():
    #popup
    if op.get()=='select your branch':
        messagebox.showerror('error','not selected')
    else:
        Label(root,text=op.get()).grid(row=3,column=2)
        messagebox.showinfo('nice','good job')   
Button(root,text='click',command=fun3).grid(row=3,column=1)
root.mainloop()
