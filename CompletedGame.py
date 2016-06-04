import turtle
import time
import math
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgcolor("Yellow")
t1.pu()
t1.goto(0,-300)
t1.pd()
t1.write("Strating Point")
t1.pu()
t1.lt(90)
k1=turtle.Turtle()
k1.pu()
k1.goto(-300,200)
k1.speed(100)
def express():
    print("Press keyboard but you must avoid Circle!!")
    print("Big retangle = 1 point ")
    print("Middle retangle = 3 points")
    print("Samll retangle = 5 points")
    print("Circle = -1 point") 
    print ("if you exit this game,press z")
    print ("score >15 game will be end")
express()
k1.pd()
k1.color("Purple")
k1.fillcolor("Purple")
k1.begin_fill()
for i in range(0,4):
    k1.fd(150)
    k1.rt(90)
k1.end_fill()
k1.pu()
k1.goto(0,150)
k1.pd()
k1.color("Blue")
k1.fillcolor("Blue")
k1.begin_fill()
for i in range(0,4):
    k1.fd(100)
    k1.rt(90)
k1.end_fill()
k1.pu()
k1.goto(200,200)
k1.pd()
k1.color("Green")
k1.fillcolor("Green")
k1.begin_fill()
for i in range(0,4):
    k1.fd(50)
    k1.rt(90)
k1.end_fill()
k1.pencolor("Black")
k1.pu()
k1.goto(-250,60)
k1.pd()
k1.write("1 score point")
k1.pu()
k1.goto(-275,175)
k1.pd()
k1.color("YellowGreen")
k1.fillcolor("YellowGreen")
k1.begin_fill()
for i in range(0,4):
    k1.fd(100)
    k1.rt(90)
k1.end_fill()
k1.pencolor("Black")
k1.pu()
k1.goto(25,50)
k1.pd()
k1.write("3 score points")
k1.pu()
k1.goto(15,130)
k1.pd()
k1.color("Orange")
k1.fillcolor("Orange")
k1.begin_fill()
for i in range(0,4):
    k1.fd(70)
    k1.rt(90)
k1.end_fill()
k1.pencolor("Black")
k1.pu()
k1.goto(225,150)
k1.pd()
k1.write("5 score points")
k1.pu()
k1.goto(215,185)
k1.pd()
k1.color("White")
k1.fillcolor("White")
k1.begin_fill()
for i in range(0,4):
    k1.fd(20)
    k1.rt(90)
k1.end_fill()
k1.pu()
k1.goto(-130,-160)
k1.pd()
k1.color("Gray")
k1.fillcolor("Gray")
k1.begin_fill()
k1.circle(70)
k1.end_fill()
k1.pu()
k1.goto(200,-150)
k1.pd()
k1.color("SkyBlue")
k1.fillcolor("SkyBlue")
k1.begin_fill()
k1.circle(100)
k1.end_fill()
k1.pu()
x=float()
y=float()
print ("Staring Score is 0")
score=0


def incir():
    (x,y)=t1.pos()
    global score
    if math.sqrt(math.pow((-130-x),2) + math.pow((-160-y),2))<=60:
        score=score-2
        print("Your scores are %d !" % score)
        t1.goto(0,-300)
    if math.sqrt(math.pow((200-x),2) + math.pow((-100-y),2))<=100:
        score=score-3
        print("Your scores are %d !" % score)
        t1.goto(0,-300)	

def h1():
    global score
    (x,y)=t1.pos()
    t1.fd(20)
    if(-275<x<-175 and 75<y<175):
        score+=1
        print ("Your scores are %d !" % score)
        t1.goto(30,-200)
    if(25<x<95 and 70<y<140):
        score+=3
        print ("Your scores are %d !" % score)
        t1.goto(30,-200)

    if(215<x<235 and 165<y<185):
        score+=5
        print ("Your scores are %d !" % score)
        t1.goto(30,-200)

    if(score>15):
        print ("You are the Best Player")
        t1.goto(0,0)
        t1.write("Good job,Friend")
        print ("Game is going to be ended after 5 seconds")
        time.sleep(5)
        wn.bye()
    incir()

def h2():
    t1.lt(45)
def h3():
    t1.rt(45)
def h4():
    t1.bk(20)
def h5():
    wn.bye()
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "Down")
wn.onkey(h5, "z")
t1.shape("turtle")
t1.color("Red")
wn.listen()

wn.exitonclick()
