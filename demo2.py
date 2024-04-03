from tkinter import*
root=Tk()

#background color
root.configure(bg='light blue')
#title
root.title('demo2')
#geometry
root.geometry('300x300')
#font
font='Arial 20'
#to change bg color and font of label
Label(root,text='first',bg='red',font='Arial 20',fg='green').grid(row=1,column=1)
#to change bg of text bg is used
#to change text color fg is used

#label
Label(root,text='second').grid(row=2,column=1)
#button
Button(root,text='press1').grid(row=3,column=1)

#event
def fun():
    Label(root,text='third').grid(row=5,column=1)
Button(root,text='press 2',command=fun).grid(row=4,column=1)

#text box
Label(root,text='enter fourth').grid(row=6,column=1)
name=Entry(root).grid(row=7,column=1)

# to add image
img=PhotoImage(file='starbus.png')
Label(root,image=img).pack()

root.mainloop()
