from tkinter import*
root=Tk()
img=PhotoImage(file='starbus.png')
Label(root,image=img).place(x=500)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 50').place(x=300,y=250)
Label(root,text='Enter Journey Details',bg='light green',fg='green').place(x=600,y=350)
Label(root,text='TO').place(x=400,y=500)
starting=Entry(root).place(x=430,y=500)
Label(root,text='FROM').place(x=600,y=500)
ending=Entry(root).place(x=640,y=500)
Label(root,text='DATE').place(x=800,y=500)
date=Entry(root).place(x=840,y=500)
Button(root,text='Show Bus',bg='light green',fg='green').place(x=1000,y=500)

root.mainloop()