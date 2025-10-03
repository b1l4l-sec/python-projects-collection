import turtle

objet1 = turtle.Turtle()
objet1.color("purple")
my_screen = turtle.Screen()

def MoveForward() :
    objet1.forward(5)
                                                    
def MoveBackward() :
    objet1.backward(5)

def MoveClockwise() :
    objet1.right(10)

def MoveCounterClockwise() :
    objet1.left(10)

def clear_all() :
    objet1.clear()
    objet1.penup()
    objet1.home()
    objet1.pendown()

objet1.pensize(7)
my_screen.listen()
my_screen.onkey(key = "z",fun =MoveForward )
my_screen.onkey(key="s" , fun=MoveBackward)
my_screen.onkey(key="d" , fun=MoveClockwise)
my_screen.onkey(key="q" , fun=MoveCounterClockwise)
my_screen.onkey(key="c" , fun=clear_all)
my_screen.exitonclick()