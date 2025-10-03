import turtle 
import random

window = turtle.Screen()
window.setup(width=500,height=500)
window.bgcolor("black")
window.title("TurtlesRace")
num_players = int(window.textinput(title="number of players",prompt="how many players you are ?  "))
colors_liste = []

for _ in range(num_players) :
    color_chosen = window.textinput(title="COLORS",prompt=f"choose ur color please ({_+1}): ").lower()
    colors_liste.append(color_chosen)

turtles_liste = []

for count in range(num_players) :
    new_turtle = turtle.Turtle()
    new_turtle.shape("turtle")
    #new_turtle.color("purple")   
    turtles_liste.append(new_turtle)

def race(object) :
    object.forward(random.randint(0,20))

x = -200
y = -230
for _ in range(num_players) :
    turtles_liste[_].penup()
    turtles_liste[_].color(colors_liste[_])
    turtles_liste[_].color
    turtles_liste[_].setx(x)
    x+= 50
    turtles_liste[_].sety(y)
    turtles_liste[_].setheading(90)

the_end = False

while not the_end :
    for count in range(num_players) :
        turtles_liste[count].penup()
        turtles_liste[count].speed("slowest")
        race(turtles_liste[count])
        if turtles_liste[count].ycor()> 230 :
            the_end = True 
            print(f"THE WINNER WHO HAS CHOSEN '{turtles_liste[count].pencolor()}' COLOR THE PLAYER NUMBER {count+1} GG")


window.mainloop()
