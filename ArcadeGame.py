import turtle as t
import time

window = t.Screen()
window.title("ArcadeGame")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

class CreatPUP(t.Turtle):

    def __init__(self,x) :
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        #self.speed("fastest")
        self.setx(x)
    
    def move_up(self) : 
        y = self.ycor() 
        self.sety(y+20)
    def move_down(self) :
        y = self.ycor()
        self.sety(y-20)

class Ball(t.Turtle):
   
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        #self.speed("slowest")

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(x=new_x,y=new_y)
    
    def bomb(self) :
        self.y_cor *= -1

    def bomb_pup(self):
        self.x_cor *= -1      

class Ranking(t.Turtle) :

    def __init__(self,position,score):
        super().__init__()
        self.clear()
        self.color("purple")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(score,False,"center",("Courier",80,"normal"))

def center_lines():
    lane1 = t.Turtle()
    lane1.color("purple")
    lane1.hideturtle()
    lane1.penup()
    lane1.goto(10,-300)
    lane1.setheading(90)
    lane1.pensize(5)
    while lane1.ycor() < 310 :
        lane1.pendown()
        lane1.forward(30)
        lane1.penup()
        lane1.forward(30)
    lane2 = t.Turtle()
    lane2.color("purple")
    lane2.hideturtle()
    lane2.penup()
    lane2.goto(-10,-300)
    lane2.setheading(90)
    lane2.pensize(5)
    while lane2.ycor() < 310 :
        lane2.pendown()
        lane2.forward(30)
        lane2.penup()
        lane2.forward(30)

r_pup = CreatPUP(350)
l_pup = CreatPUP(-350)


window.listen()
window.onkey(key="a",fun=l_pup.move_up)
window.onkey(key="q",fun=l_pup.move_down)
window.onkey(key="p",fun=r_pup.move_up)
window.onkey(key="m",fun=r_pup.move_down)

bilal = Ball()
ranke_lp = 0
ranke_rp = 0 
center_lines()
#this is also one of yhe projects that i liked  a lot lets execute
left_score = Ranking((-100,200),ranke_lp)
right_score = Ranking((100,200),ranke_rp)

game_is_on = True
while game_is_on :
    time.sleep(0.1)
    window.update()
    if bilal.ycor() == 290 or bilal.ycor() == -290:
        bilal.bomb()
    if (bilal.xcor() == 330 and bilal.ycor() >= r_pup.ycor()-50 and bilal.ycor() <= r_pup.ycor()+50) :
        bilal.bomb_pup()
    if (bilal.xcor() == -330 and bilal.ycor() >= l_pup.ycor()-50 and bilal.ycor() <= l_pup.ycor()+50) :
        bilal.bomb_pup()
    if bilal.xcor()>360 :
        left_score.clear()
        bilal.home()
        bilal.bomb_pup()    #just same code to reverse the direction of x axes
        ranke_lp+=1
        left_score = Ranking((-100,200),ranke_lp)
    if bilal.xcor()<-360 :
        right_score.clear()
        bilal.home()
        bilal.bomb_pup()    #just same code to reverse the direction of x axes
        ranke_rp+=1
        right_score = Ranking((100,200),ranke_rp)
    bilal.move()


window.exitonclick()



