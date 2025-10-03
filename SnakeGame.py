#************parts problem*************
import turtle
import time
import random

window = turtle.Screen()
window.title("Snake Game")
window.setup(width=600,height=600)
window.bgcolor("black")
#parts
parts = ["head"]
#snake s head
parts[0] = turtle.Turtle()
parts[0].shape("square")
parts[0].color("white")
parts[0].speed(0)
parts[0].direction = "up"
#food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.shapesize(0.4,0.4)
rand_x = random.randint(-290,290)
rand_y = random.randint(-290,290)
food.penup()
food.goto(rand_x,rand_y)
#functions
def move() :
    for _ in parts :
        if _.direction == "up" :
            #head.penup()
            y = _.ycor()
            _.sety(y + 20)
        if _.direction == "down" :
            #head.penup()
            y = _.ycor()
            _.sety(y - 20)
        if _.direction == "right" :
            #head.penup()
            x = _.xcor()
            _.setx(x + 20)
        if _.direction == "left" :
            #head.penup()
            x = _.xcor()
            _.setx(x - 20)

def z():
    parts[0].direction = "up"
def d():
    parts[0].direction = "right"
def s():
    parts[0].direction = "down"
def q():
    parts[0].direction = "left"

def is_collusion_on() :
    if parts[0].distance(food) < 20 :
        return True
    return False
"""
def add_part(parametre):
    part = turtle.Turtle()
    part.color("purple")
    part.shape("square")
    if head.direction == "up" :
        part.penup()
        part.goto(head.xcor(),head.ycor()-(parametre * 40))
    if head.direction == "down" :
        part.penup()
        part.goto(head.xcor(),head.ycor()+(parametre * 40))
    if head.direction == "right" :
        part.penup()
        part.goto(head.xcor()-(parametre * 40),head.ycor())
    if head.direction == "up" :
        part.penup()
        part.goto(head.xcor()+(parametre * 40),head.ycor())
"""
#executions
window.listen()
window.onkeypress(z,"z")
window.onkeypress(d,"d")
window.onkeypress(q,"q")
window.onkeypress(s,"s")

while True :
    parts[0].penup()
    #move(head)
    time.sleep(0.1)
    if is_collusion_on() :
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        food.penup()
        food.goto(rand_x,rand_y)
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.color("purple")
        new_part.shape("square")
        new_part.penup()
        parts.append(new_part)
        for count in range(len(parts)-1) :
            x = parts[count].xcor()
            y = parts[count].ycor()
            parts[count+1].setx(x)
            parts[count+1].sety(y)
    #head.penup()
    move()
    #time.sleep(0.1)


window.mainloop()