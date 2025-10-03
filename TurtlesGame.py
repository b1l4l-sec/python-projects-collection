print("*******l9mer halal a molay************")

import turtle
import random
#turtle size == 40x40
#object = turtle.Turtle()          
#object.shape("turtle")
#fastest_lvl_liste = ["fastest","fast","normal","slow","slowest"]
colors = ["red","orange","yellow","green","blue","purple"]
turtles_name = ["object1","object2","object3","object4","object5","object6"]
y_axes = [50,-50,100,-100,150,-150]
is_on = True
trouve = False

def race(shape) :
    steps = random.randint(0,10)
    #fastest_lvl = random.choice(fastest_lvl_liste)
    #turtle.speed(fastest_lvl)
    shape.forward(steps)

window = turtle.Screen()
window.setup(width= 500,height= 400)

for _ in range(6) :
    turtles_name[_] = turtle.Turtle()
    turtles_name[_].shape("turtle")
    turtles_name[_].color(colors[_])

num_playes = int(window.textinput(title="Number of players",prompt="how many players are there ?"))
colors_guessed_liste =[]

for _ in range(num_playes) :
    color_guessed = window.textinput(title="Geissing Game",prompt="wich color gonna win ? enter the color :\n \t (red/yellow/purple/orange/green/blue)")
    colors_guessed_liste.append(color_guessed)

for _ in range(6) :
    turtles_name[_].penup()
    turtle.hideturtle()
    turtles_name[_].goto(x = -225,y = y_axes[_])

while is_on :
    race(turtles_name[0])
    race(turtles_name[1])
    race(turtles_name[2])
    race(turtles_name[3])
    race(turtles_name[4])
    race(turtles_name[5])
    for _ in turtles_name :
        if _.xcor() > 230 :
            winner = _.pencolor()
            for count in range(num_playes) :
                if colors_guessed_liste[count] == winner  :
                    print(f"the winner is who has chosen the {colors_guessed_liste[count]} color the player number {count + 1}     GG") 
                    is_on = False 
                    trouve = True
                    break
            if trouve == False :
                print("THERE IS NO WINNER. YOU LOSE, TRY LATER      \n\nEND")
                is_on = False    

 
    

window.exitonclick() 