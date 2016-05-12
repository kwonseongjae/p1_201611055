import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def line():
    t1.pencolor("Red")
    t1.pu()
    t1.goto (-200,200)
    t1.pd()
    t1.fd(400)
    t1.pu()
    t1.home()
    t1.pd()
    t1.pencolor("Black")
def ku():
    t1.fd(50)
    (x,y)=t1.pos()
    if(-200<x<200 and y==200):
        print "you trapped"
def kd():
    t1.bk(50)
    (x,y)=t1.pos()
    if (-200<x<200 and y==200):
        print "you trapped"
def kr():
    t1.rt(90)
def kl():
    t1.lt(90)
def mousegoto(x,y):
    t1.setpos(x,y)
    (x,y)=t1.pos(x,y)
    if (-200<x<200 and y==200):
        print "you trapped"
def end():
    wn.bye()
def addKeys():
    wn.onkey(ku,"Up")
    wn.onkey(kd,"Down")
    wn.onkey(kr,"Right")
    wn.onkey(kl,"Left")
    wn.onkey(end,"q")
def addMouse():
    wn.onclick(mousegoto)
def lab11():
    line()
    addKeys()
    addMouse()
    wn.listen()
    turtle.mainloop()
lab11()    
