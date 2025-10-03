import tkinter as tk           #simple project with tkinter modul

window = tk.Tk()
window.title("Miles To Kilometers")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)


def claculations() :
    result = round(float(Miles_input.get()) * 1.609,2)
    Kilos_result.config(text=result)


Miles_input = tk.Entry(width=7)
Miles_input.insert("end",string="Miles:")
Miles_input.grid(column=1,row=0)

my_lable = tk.Label(text="Miles")
my_lable.grid(column=2,row=0)

is_equal_label = tk.Label(text="is equal to ")
is_equal_label.grid(column=0,row=1)     #MILES T

Kilos_result = tk.Label(text="0")    #THANKSFOR WATCHING    
Kilos_result.grid(column=1,row=1)

Km_label = tk.Label(text="Km")
Km_label.grid(column=2,row=1)

calculate_button = tk.Button(text="Calculate",command=claculations)
calculate_button.grid(column=1,row=2)




window.mainloop()