from tkinter import*
root=Tk()
num1=Entry(root)
num1.pack()
num2=Entry(root)
num2.pack()
def add():
    mylab1=Label(root,text=int(num1.get())+int(num2.get()))
    mylab1.pack()
def subtract():
    mylab2=Label(root,text=int(num1.get())-int(num2.get()))
    mylab2.pack()
def division():
    mylab3=Label(root,text=int(num1.get())/int(num2.get()))
    mylab3.pack()
def multiplication():
    mylab4=Label(root,text=int(num1.get())*int(num2.get()))
    mylab4.pack()
    
   
mylabel=Label(root,text="hello world")
mylabel.pack()
mybutton=Button(root,text="+",command=add)
mybutton.pack()
mybutton1=Button(root,text="-",command=subtract)
mybutton1.pack()
mybutton2=Button(root,text="/",command=division)
mybutton2.pack()
mybutton3=Button(root,text="*",command=multiplication)
mybutton3.pack()
root.configure(bg='aquamarine')

root.mainloop()
