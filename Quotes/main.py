from tkinter import *
import requests# this is the module that do that job

#hello everyone so the project of today is about coming with data from a website this the subject we ll see how to do it stay with me

def get_quote():
    answer = requests.get(url="https://api.kanye.rest")# here we have to enter the url of the website to come with data 
    answer.raise_for_status()
    #print(answer)
    #and this commend to show us if we have the access to the data of the web
    #so all good and we sucseeded to export the datat from the website if it was an error we will see it wait
    data = answer.json()["quote"]# we gonna export just the quote as a line 
    canvas.itemconfig(quote_text,text = data)# 200 means that we have the ok to the data look


window = Tk()
window.title("Take some Quotes") # that s all see u next <3
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click on my head to START <3", width=250,font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()