import turtle as t
import pandas

window =t.Screen()
window.title("StatesGame")

image = "blank_states_img.gif"

window.addshape(image)
t.shape(image)
counteur_liste = []
answer_state = window.textinput("START","strat = on , end = off")

while len(counteur_liste) < 50 and answer_state != "off":
    answer_state = window.textinput(f"{len(counteur_liste)}/50 answers re correct","Enter a State (off=end)")
    data = pandas.read_csv("50_states.csv")
    states_liste = data.state.to_list()
    if answer_state in counteur_liste :
        continue
    if answer_state in states_liste :
        curssor= t.Turtle()
        curssor.hideturtle()
        curssor.penup()
        state_data = data[data.state == answer_state]
        positon = (int(state_data.x),int(state_data.y))
        curssor.goto(positon)
        curssor.write(answer_state,False,"center",("Arial",8,"normal"))
        counteur_liste.append(answer_state)



window.mainloop()
#Consolas,'Courier New', monospace