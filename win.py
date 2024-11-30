from tkinter import *
from tkinter.ttk import Treeview
from validation import *


id_list = []

def reset_form():
    id.set(0)
    price.set("")
    quantity.set("")


win = Tk()
win.geometry("700x700")
win.title("Calculator")

# id
Label(win, text="id").place(x=20,y=20)
id = IntVar()
Entry(win, textvariable=id).place(x= 80, y =20)

# pay
Label(win, text="price").place(x=20,y=70)
pay = StringVar()
Entry(win, textvariable=pay).place(x= 80, y =70)

# date
Label(win, text="quantity").place(x=20,y=120)
date = StringVar()
Entry(win, textvariable=date).place(x= 80, y =120)

# person
Label(win, text="id").place(x=20,y=170)
person = IntVar()
Entry(win, textvariable=id).place(x= 80, y =170)

# type
Label(win, text="id").place(x=20,y=220)
type = IntVar()
Entry(win, textvariable=id).place(x= 80, y =220)


# Report
#Label(win, text="Count").place(x=20,y=170)
#count = IntVar()
#Entry(win, textvariable=count, state="readonly").place(x= 80, y =170)


# Table
table = Treeview(win, columns=[1,2,3],height=12, show="headings")

# Title
table.heading(1 , text="id")
table.heading(2 , text="price")
table.heading(3 , text="quantity")

# Width
table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.place(x=250, y=20)

# Save
Button(win, text="Add", width=8).place(x=80, y=260)

win.mainloop()
