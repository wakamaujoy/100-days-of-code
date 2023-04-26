from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_new():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(1,4)
    nr_numbers = random.randint(3,6)

    password_list =[]

    for char in range(1, nr_letters +1):
        password_list += random.choice(letters)
    for sy in range(1, nr_symbols +1):
        password_list += random.choice(symbols)
    for num in range(1, nr_numbers +1):
        password_list += random.choice(numbers)
    random.shuffle(password_list)

    new_password = "".join(password_list)
    print(f"Your password is {password}")

    password_entry.insert(0,new_password)
    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if len(website)== 0  or len(password) ==0:
        messagebox.showwarning(title="oops", message="You cannot leave any field empty")
    else:
        yes =messagebox.askyesno(title="Verify your details", message=f"webisite_name: {website}\nemail:{email}\npassword:{password}\n\nIf correct should we proceed to save")

        if yes:
            with open("data.txt", mode= "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



    # --------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password_Manager")
window.config(padx=50, pady=50)


my_canvas = Canvas(height=200, width=200)
my_image = PhotoImage(file = "logo.png")
my_canvas.create_image(100,100, image=my_image)
my_canvas.grid(column=1, row=0)


website_label = Label(text="website")
website_label.grid(column =0, row =1)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1)
website_entry.focus()


email_username= Label(text="email/username")
email_username.grid(column =0, row =2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1,row=2)
email_username_entry.insert(0, "wakamaujoy@gmail.com")



password = Label(text="password")
password.grid(column =0, row =3)

password_entry = Entry(width=25)
password_entry.grid(column=1,row=3)

generate_password = Button(text="Generate Password", command=password_new)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=30, command=save_password)
add.grid(column=1, row=4)


window.mainloop()