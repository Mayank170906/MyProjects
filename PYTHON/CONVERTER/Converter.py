from tkinter import *


def calc():
    label_03.config(text=float(data.get())*1.6)


display = Tk()
display.minsize(width=500, height=300)
display.title("Mile to KM converter.")
label_01 = Label(text="Miles")
label_01.grid(row=0, column=2)
label_02 = Label(text="is equal to")
label_02.grid(row=1, column=0)
label_03 = Label(text=0)
label_03.grid(row=1, column=1)
label_04 = Label(text="KM")
label_04.grid(row=1, column=2)
data = Entry(width=30)
data.insert(END, string="Enter the value in (KM)")
data.grid(row=0, column=1)
button = Button(text="Calculate", command=calc)
button.grid(row=2, column=1)


display.mainloop()
