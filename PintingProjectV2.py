import turtle
import datetime

window = turtle.Screen()
window.title("PintingProjectV2")
window.bgcolor("black")    # i developped another version of the pinting project here we go 

curssor = turtle.Turtle()
color=window.textinput(title="Color",prompt="whish color u want : ").lower() #which color we want to usee ..
curssor.color(color)
time = datetime.datetime.now()

def move_forward():
    curssor.setheading(90)
    curssor.forward(20)
    curssor.speed(0)
def move_backward():
    curssor.setheading(-90)
    curssor.forward(20)
    curssor.speed(0)
def move_right():
    curssor.setheading(0)
    curssor.forward(20)
    curssor.speed(0)
def move_left():
    curssor.setheading(180)
    curssor.forward(20)
    curssor.speed(0)
def clear_all(): 
    curssor.clear()
    curssor.penup()
    curssor.hideturtle()
    curssor.speed(0)
    curssor.setx(-255)
    curssor.sety(208)
    curssor.write(f"{time.strftime("%A")},{time.strftime("%d")},{time.strftime("%B")},{time.strftime("%Y")}\nto penup press (b)\nto pendown press (v)\nto clear/delete all press (c)\nuse these ones z/s/q/d",False,"center",("arial",10,"normal"))
    curssor.home()
    curssor.showturtle()
    #curssor.pendown()
def rewrite():
    curssor.pendown()

curssor.pensize(8)
curssor.penup()
curssor.hideturtle()
curssor.speed(0)
curssor.setx(-255)
curssor.sety(208)
curssor.write(f"{time.strftime("%A")},{time.strftime("%d")},{time.strftime("%B")},{time.strftime("%Y")}\nto penup press (b)\nto pendown press (v)\nto clear/delete all press (c)\nuse these ones z/s/q/d",False,"center",("arial",10,"normal"))
curssor.home()
curssor.showturtle()
curssor.pendown()
window.onkeypress(rewrite,"v")
window.onkeypress(curssor.penup,"b")
window.onkeypress(clear_all,"c")
window.listen()
window.onkeypress(move_forward,"z")
window.onkeypress(move_backward,"s")
window.onkeypress(move_right,"d")
window.onkeypress(move_left,"q")


window.mainloop()