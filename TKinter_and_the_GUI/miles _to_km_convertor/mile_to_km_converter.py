from tkinter import *

window = Tk()
window.title("miles to km converter")
window.minsize(height=300, width=300)
window.config(padx=100,pady=100)

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label =Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_to = Label(text="is equals to")
is_equal_to.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)


def convert():
    conversion = float(miles_input.get()) * 1.60934
    km_result.config(text=conversion)
    return conversion


button = Button(text="convert", command=convert)
button.grid(column=1, row=2)


window,mainloop()