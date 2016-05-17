import turtle  
wn=turtle.Screen()  
t1=turtle.Turtle()  
import math  
t1.pu()  
t1.goto(0,50)  
t1.pd()  
t1.circle(50)  
t1.penup()  
t1.home()  
def isIncircle(curpos):  
    radius=50  
    pos=(0,100)  
    if math.sqrt(math.pow(curpos[0]-pos[0],2) + math.pow(curpos[1]-pos[1],2))<=radius:  
        print ("True")  
    else:  
        print ("False")  
def k1():  
    t1.fd(30)  
    curpos=t1.pos()  
    isIncircle(curpos)  
wn.onkey(k1,"Up")  
def k2():  
    t1.lt(90)  
def k3():  
    t1.right(90)  
def k4():  
    t1.bk(30)  
    curpos=t1.pos()  
    isIncircle(curpos)  
wn.onkey(k2,"Left")  
wn.onkey(k3,"Right")  
wn.onkey(k4,"Down")  
wn.listen()  
wn.exitonclick() 
