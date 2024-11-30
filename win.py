from tkinter import *
from tkinter import StringVar, IntVar
from tkinter.ttk import Treeview
from validation import *
import tkinter.messagebox as msg  # alias

data_list = []


def reset_form():
    id.set(0)
    price.set("")
    person.set("")
    date.set("")

def add_click():
    if id_validator(id.get()) and price_validator(price.get())and person_validator(person.get())and date_validator(date.get()):
        data=(id.get(),price.get(),person.get(),date.get(),pay.get())
        table.insert("", END, values=data)
        reset_form()
        msg.showinfo("Save", "Saved Successful")
        data_list.append(data)
    else:
        msg.showerror("Save Error", "Invalid Data !!!")


win = Tk()
win.geometry("920x400")
win.title("Calculator")

# id
Label(win, text="id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id).place(x=80, y=20)

# pay
Label(win, text="price").place(x=20, y=70)
price =IntVar()
Entry(win, textvariable=price).place(x=80, y=70)

# date
Label(win, text="date").place(x=20, y=120)
date = StringVar()
Entry(win, textvariable=date).place(x=80, y=120)

# person
Label(win, text="person").place(x=20, y=170)
person = StringVar()
Entry(win, textvariable=person).place(x=80, y=170)

# type
pay=StringVar()
Radiobutton(win, text="pardakht",variable=pay,value="pardakht").place(x=20, y=220)
Radiobutton(win, text="daryaft",variable=pay,value="daryaft").place(x=20, y=240)

pay.set("pardakht")
# type = IntVar()
# Entry(win, textvariable=type).place(x=80, y=220)

# Report
# Label(win, text="Count").place(x=20,y=170)
# count = IntVar()
# Entry(win, textvariable=count, state="readonly").place(x= 80, y =170)


# Table
table = Treeview(win, columns=[1, 2, 3, 4, 5], height=12, show="headings")

# Title
table.heading(1, text="id")
table.heading(2, text="price")
table.heading(3, text="date")
table.heading(4, text="person")
table.heading(5, text="type")
# Width
table.column(1, width=100)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.place(x=220, y=20)

# Save
btn = Button(win, text="Add", width=8, command=add_click).place(x=80, y=260)

win.mainloop()
