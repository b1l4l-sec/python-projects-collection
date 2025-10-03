import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1 #25
SHORT_BREAK_MIN =1 #5   
LONG_BREAK_MIN =1 #20
reps = 0
marks_liste =""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    global reps
    global marks_liste
    reps = 0 
    marks_liste = ""
    comment.config(text="Timer",fg=RED)
    canvas.itemconfig(timer_text,text = "00:00")
    marks.config(text=marks_liste)
    #start_count()

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    global reps
    global marks_liste
    reps += 1
    if reps == 1 or reps ==  3 or reps ==  5 or reps ==  7 :
        count_down(work_secs)
        comment.config(text="Work",fg=GREEN)
    elif reps == 2 or reps ==  4 or reps ==  6 :
        count_down(short_break_secs)
        comment.config(text="Break",fg=PINK)
        marks_liste += "✔"
        marks.config(text=marks_liste)
    elif reps == 8 :
        count_down(long_break_secs)
        comment.config(text="Break",fg=RED)
        marks_liste += "✔"
        marks.config(text=marks_liste)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count) : # def count_down(seconds,WORK_MIN) :
    """
    if seconds >= 60 and WORK_MIN >= 60:
        canvas.itemconfig(timer_text,text = f"{WORK_MIN -1}:{seconds -1 }")
    elif seconds < 60 and WORK_MIN < 60 :
        canvas.itemconfig(timer_text,text = f"0{WORK_MIN -1}:0{seconds -1 }")
    elif seconds < 60 :
        canvas.itemconfig(timer_text,text = f"{WORK_MIN -1}:0{seconds -1 }")
    elif WORK_MIN < 60 :
        canvas.itemconfig(timer_text,text = f"0{WORK_MIN -1}:{seconds -1 }")
    if seconds >1 and WORK_MIN >=0:
        window.after(1000,count_down,seconds -1,WORK_MIN)
    if seconds == 1 and WORK_MIN >1:
        #WORK_MIN = WORK_MIN - 1
        seconds = 60
        window.after(1000,count_down,seconds,WORK_MIN-1) 
    """
    mins = int(count / 60)
    seconds = count % 60 
    if seconds >= 10:
        canvas.itemconfig(timer_text,text = f"{mins}:{seconds}")
    else :
        canvas.itemconfig(timer_text,text = f"{mins}:0{seconds}")
    if count > 0 :
        global timer 
        timer = window.after(1000,count_down,count-1)
    else :
        start_count()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("PomdoroChrono")
window.config(padx=100,pady=50,bg="white")

comment = tk.Label(text="Timer",fg=RED)
comment.config(font=(FONT_NAME,30,"bold"),bg="white")
comment.grid(column=1,row=0)

canvas = tk.Canvas(width=200,height=224,bg="white",highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button = tk.Button(text="Start",highlightthickness=0,command=start_count)
reset_button = tk.Button(text="Reset",highlightthickness=0,command=reset)
start_button.config(width=7)
start_button.grid(column=0,row=2)
reset_button.config(width=7)
reset_button.grid(column=2,row=2)

marks = tk.Label(text=marks_liste,fg=RED)
marks.config(font=(FONT_NAME,18,"bold"),bg="white")
marks.grid(column=1,row=5)

window.mainloop()