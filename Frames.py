from tkinter import *
root=Tk()

#------------------------------------------
frm1=Frame(root, bg='red')
frm1.place(y=10,height=100,width=400)

#------------------------------------------------




btn=Button(frm1 ,text="inter")
btn.place(width=100,y=50)

btn1=Button(frm1 ,text="inter22")
btn1.place(width=100,y=50, x=100)



btn2=Button(root ,text="my")
btn2.place(width=100,y=0, x=100)






root.title("Frames")
root.maxsize(500,500)
root.minsize(500,500)
root.mainloop()
