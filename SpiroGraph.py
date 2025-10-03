import turtle as t
import random 

objet = t.Turtle()
objet.speed("fastest")
t.colormode(255)

def random_color() :
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for angle in range(100) :
    objet.circle(80)
    objet.setheading(objet.heading() + 5)
    objet.color(random_color())
    if objet.heading() == 0 :
        break

my_screen = t.Screen()
my_screen.exitonclick()