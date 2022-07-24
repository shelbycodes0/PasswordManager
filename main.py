from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_symbols = [random.choice(symbols) for symbol in range(random.randint(1, 2))]
    password_numbers = [random.choice(numbers) for num in range(random.randint(1, 3))]

    password_list = password_letters + password_numbers +password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please complete the required fields: website, password")
    else:
        is_ok = messagebox.askokcancel(title=f"Confirm Details for {website}", message=f"Email/Username: {email} \n Password: {password} \n Would you like to save this password?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(85,100, image=lock_image)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry(width=42)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, string="shelbycodes@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1,row=3)

password_button = Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1,row=4,columnspan=2)




window.mainloop()