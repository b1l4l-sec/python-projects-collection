import turtle as t
import random

objet = t.Turtle()
objet.home()
colors_liste = ["red","blue","purple","black","brown"]
num_of_sizes = 3
nbr = 1
objet.speed("fastest")
objet.pensize(3)
# to show the shapes in the middle of the screen 
objet.penup()
objet.setheading(180)
objet.forward(40)
objet.setheading(0)
objet.pendown()
 #nbr < 8 == 8 shapes 
while  nbr < 3  :    
    for _ in range(0,num_of_sizes) :
        angle = 360 / num_of_sizes                          #the fomula 
        objet.forward(80)
        objet.right(angle)
    color_num = random.randint(0,4)
    objet.color(colors_liste[color_num])
    num_of_sizes += 1
    nbr += 1

num_of_sizes1 = 3
nbr1 = 1

while nbr1 < 3 :
    for _ in range(0,num_of_sizes1) :
        angle = 360 / num_of_sizes1
        objet.forward(80)
        objet.left(angle)
    color_num = random.randint(0,4)
    objet.color(colors_liste[color_num])
    num_of_sizes1 += 1
    nbr1 += 1

my_screen = t.Screen()
my_screen.exitonclick()