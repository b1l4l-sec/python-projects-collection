import tkinter as tk

#window

window = tk.Tk()
window.minsize(width=500,height=500)
window.title("TkinterModuleLerning")

#labels 

my_label = tk.Label(text="Label")
my_label.config("hello world")
my_label.pack("""side= *** """)

#buttons

button = tk.Button(text="click here",command="""function""")
button.pack()

#Entries

input_text = tk.Entry(width=30)
input_text.insert(string="Start body")
input_text.pack()
text = input_text.get()

#text display

text = tk.Text(height=5,width=30)
text.focus()
text.insert("write ue lanes : ")
text.pack()

#spinbox

def spinbox_used():
    print(spinbox.get())

spinbox = tk.Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()

#scale

def scale_move():
    print(scale.get())

scale = tk.Scale(from_=0,to=100,width=5,command=scale_move)
scale.pack()

#Check button

def Check_button():
    print(check_it.get())

check_it = tk.IntVar()
checkbutton = tk.Checkbutton(text="is On?",variable=check_it,command=Check_button)
checkbutton.pack()

#RadioButtons

def radio_button() :
    print(button.get())

button = tk.IntVar
RadioButton1 = tk.Radiobutton(text= "option1",value = 1,variable=button,command=radio_button )
RadioButton2 = tk.Radiobutton(text= "option2",value = 2,variable=button,command=radio_button )
RadioButton1.pack()
RadioButton2.pack()

