import tkinter as tk
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)
"""
password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char
"""
def generate_password():
    psd_entry.delete(0,tk.END)
    letters_liste = [random.choice(letters) for _ in range(nr_letters)]
    numbers_liste = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_liste = [random.choice(symbols) for _ in range(nr_symbols)]

    password_liste = letters_liste + numbers_liste + symbols_liste
    random.shuffle(password_liste)
    password = "".join(password_liste)  #to connect all of the chars with no space ""
    psd_entry.insert(0,password)
    #pyperclip.copy(password)
# ----------------------------  Add DATA ------------------------------- #
def add_data() :

    website = website_entry.get()
    website_data = website.upper()
    email_data = email_entry.get()
    passwords_data = psd_entry.get()

    if len(website)==0 or len(passwords_data)==0:
        messagebox.showwarning(title="Error,  Oooops",message="Don't leave any of ur Data empty please <3")
    else :
        is_okay = messagebox.askokcancel(title=website_data,message=f"Email : {email_data}\nPassword : {passwords_data}")
        if is_okay :
            with open("Passwords_Data.txt","a") as Data :
                Data.write(f"website : {website_data}    |   email : {email_data}   |   password : {passwords_data}\n")
                website_entry.delete(0,tk.END)
                psd_entry.delete(0,tk.END)
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=50,pady=50)

canvas = tk.Canvas(height=200,width=200)
imag = tk.PhotoImage(file="logo.png")
canvas.create_image(100,100,image= imag)
canvas.grid(row=0,column=1)

#labels
website_label = tk.Label(text="Website :")
website_label.grid(row=1,column=0)
email_label = tk.Label(text= "Email :")
email_label.grid(row=2,column=0)
psd_label = tk.Label(text="Password :")
psd_label.grid(row=3,column=0)
#entries
website_entry = tk.Entry(width=45)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=45)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"CodeLover@gmail.com")
psd_entry = tk.Entry(width=25)
psd_entry.grid(row=3,column=1)
#Buttons
generate_button = tk.Button(text="Generate",width=16,command=generate_password)
generate_button.grid(row=3,column=2)
add_button = tk.Button(text="Add to File",width=38,command=add_data)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()

#u see so u can can generate passwords with urself and save them in a file on ur PC see uuuuu