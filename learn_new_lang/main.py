import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
temp = {}
learn = {}

try :
    data = pandas.read_csv("data/words_to_learn.csv")# so here we gonna export the data from this file if its exists if not 
except FileNotFoundError :
    original_data = pandas.read_csv("data/french_words.csv")# we gonne take the data from this file its hase the frequecy words in french to learn we can use any words of any language just enter ur words there 
    learn = original_data.to_dict(orient="records")
else :
    learn = data.to_dict(orient="records")


def next_move():
    global temp , flip_timer
    window.after_cancel(flip_timer)
    temp = random.choice(learn)
    canvas.itemconfig(title,text= "French",fill = "black")
    canvas.itemconfig(text,text= temp["French"],fill= "black")
    canvas.itemconfig(bg_item,image= card_frnt_pic)
    flip_timer = window.after(3000,func= flip_move)


def flip_move():
    canvas.itemconfig(title,text= "English",fill= "white")
    canvas.itemconfig(text,text= temp["English"],fill= "white")
    canvas.itemconfig(bg_item,image= card_end_pic)
    

def i_know_this():
    learn.remove(temp)
    print(len(learn))
    data = pandas.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_move()


window = tk.Tk()
window.title("Start learning")
window.config(padx= 50 , pady = 50, bg= BACKGROUND_COLOR)

flip_timer = window.after(3000,func= flip_move)


canvas = tk.Canvas(width=800,height=526)
card_frnt_pic = tk.PhotoImage(file="images/card_front.png")
card_end_pic = tk.PhotoImage(file="images/card_back.png")
bg_item = canvas.create_image(400,263,image = card_frnt_pic)
title = canvas.create_text(400,120,text= "Title",font=("Ariel",40,"italic"))
text = canvas.create_text(400,263,text="Text",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0 , column=0,columnspan=2)

idk_pic = tk.PhotoImage(file="images/wrong.png") 
idk_button = tk.Button(image=idk_pic,highlightthickness=0,command=next_move)
idk_button.grid(row=1,column=0)
#idk_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)

ik_pic = tk.PhotoImage(file="images/right.png")
ik_button = tk.Button(image=ik_pic,highlightthickness=0,command=i_know_this)
ik_button.grid(row=1,column=1)
#ik_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)

next_move()

window.mainloop()

#so right image to say that u know that word and u remembered it if not so the false image there for u let s see 