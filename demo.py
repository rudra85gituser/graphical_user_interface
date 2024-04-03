#radio button
#check box
#drop down menu/option menu
#popup(message box)
#grid
#link of page

from tkinter import*
root=Tk()
#to change font
font='Arial 20'
# to fix geometry/size
root.geometry('800x800')
#title
root.title("demo1")
#to change background color
root.configure(bg='light green')

#to change colour of label
Label(root,text='hii',bg="red",font=("Arial",20,"bold")).pack()

# to add image in background
img=PhotoImage(file='starbus.png')
Label(root,image=img).pack()

#label
Label(root,text="hello").pack()
#button
Button(root,text="go").pack()

#event
def fun():
    Label(root,text="event is added").pack()
Button(root,text="to create event click here",command=fun).pack()

# to add text box
Label(root,text="enter name").pack()
name=Entry(root)
name.pack()

#use of get function
Label(root,text='enter number 1').pack()
num1=Entry(root)
num1.pack()
Label(root,text='enter number 2').pack()
num2=Entry(root)
num2.pack()
def sum():
    Label(root,text=int(num1.get())+int(num2.get())).pack()
Button(root,text="click to get sum",command=sum).pack()

root.mainloop()
