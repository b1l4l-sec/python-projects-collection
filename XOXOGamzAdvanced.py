import turtle as t
import time

lanes = t.Turtle()
lanes.color("white")
lanes.hideturtle()
lanes.pensize(3)

object = "X"
winner = False 
count = 0 

new_x = 0
for _ in range(2) :
    if lanes.ycor() < 150:
        lanes.penup()
        lanes.goto(50+new_x,-150)
        lanes.pendown()
        lanes.setheading(90)
        lanes.forward(300)
        lanes.penup()
        lanes.home()
        new_x -= 100
new_y = 0
for _ in range(2) :
    if lanes.xcor() < 150:
        lanes.penup()
        lanes.goto(-150,50+new_y)
        lanes.pendown()
        lanes.setheading(0)
        lanes.forward(300)
        lanes.penup()
        lanes.home()
        new_y -= 100

window = t.Screen()
window.setup(width=300,height=300)
window.bgcolor("black")
window.title("XOXOGame Enjoy")
window.tracer(0)

def body(pos,which):
    body = t.Turtle()
    body.color("red")
    body.pensize(3)
    body.penup()
    body.hideturtle()
    body.goto(pos)
    body.write(which,False,"center",("Arial",40,"normal"))

def position_to_set(X) :
    match X :
        case "11" :
            return (-90,70)
        case "13":
            return (90,70)
        case "12" :
            return (0,70)
        case "21" :
            return (-90,-35)
        case "22" :
            return (0,-35)
        case "23" :
            return (90,-35) 
        case "31" :
            return (-90,-130) 
        case "32" :
            return (0,-130)
        case "33" :
            return (90,-130)  

start = window.textinput("start","start = 'on', stop ='off' ")

while not winner and start == "on": 
    if count % 2 == 0 :
        object = "X"
    else :
        object = "O"
    answer = window.textinput("Choose","enter ur cord : (11/12/13/21/22/23/31/32/33)")
    if answer == "off" :
        start = "off"
    position = position_to_set(answer)
    body(position,object)
    count+=1
    
    time.sleep(0.1)
    window.update()

#answer = window.textinput("Choose","enter ur cord : (11/12/13/21/22/23/31/32/33)")