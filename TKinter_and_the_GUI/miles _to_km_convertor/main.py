#
from tkinter import *

window = Tk()
window.minsize(height=400, width=500)
window.title("my first GUI program")

my_label = Label(text ="Hi there", font=("Arial", 24,"bold"))
my_label.pack()

def clicked():
    print("i got clicked")
    my_label.config(text="button got clicked")
my_button = Button(text="Click here", command=clicked)
my_button.pack()


input = Entry()
input.pack()
window.mainloop()

# def calculate(*args):
#     sum = 0
#     for item in args:
#        sum += item
#     return sum
# calculate(4,8,9,8,9,0,6,78)

# def calculate( **kwargs):
#    sum = kwargs["a"]+ kwargs["b"]+kwargs["c"]
#    print(sum)
# calculate(a=2, b=5, c=9)


# class Car():
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
# my_car = Car(make="nissan")
# print(my_car.make)
# print(my_car.model)

