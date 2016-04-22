import turtle
import time
wn=turtle.Screen()
t1=turtle.Turtle()
t1.pu()
t1.goto(0,-200)
t1.pd()
t1.write("Strating Point")
t1.pu()
t1.lt(90)
import turtle
k1=turtle.Turtle()
k1.pu()
k1.goto(-300,200)
k1.speed(100)
print ("if you exit this game,press z")
print ("score >15 game will be end")
k1.pd()
for i in range(0,4):
	k1.fd(150)
	k1.rt(90)
k1.pu()
k1.goto(0,150)
k1.pd()
for i in range(0,4):
	k1.fd(100)
	k1.rt(90)
k1.pu()
k1.goto(200,200)
k1.pd()
for i in range(0,4):
	k1.fd(50)
	k1.rt(90)
k1.pencolor("Green")
k1.pu()
k1.goto(-250,150)
k1.pd()
k1.write("1 score point")
k1.pu()
k1.goto(-275,175)
k1.pd()
for i in range(0,4):
	k1.fd(100)
	k1.rt(90)
k1.pu()
k1.goto(25,75)
k1.pd()
k1.write("3 score points")
k1.pu()
k1.goto(15,130)
k1.pd()
for i in range(0,4):
	k1.fd(70)
	k1.rt(90)
	
k1.pu()
k1.goto(225,175)
k1.pd()
k1.write("5 score points")
k1.pu()
k1.goto(215,185)
k1.pd()
for i in range(0,4):
	k1.fd(20)
	k1.rt(90)
k1.color("Pink")
x=float()
y=float()
print ("Staring Score is zero")
score=0
def h1():
	global score
	(x,y)=t1.pos()
	t1.fd(20)
	if(-275<x<-175 and 75<y<175):
		score+=1
		print ("your scores are %d !" % score)
		t1.goto(30,-200)
	if(25<x<95 and 70<y<140):
		score+=3
		print ("your scores are %d !" % score)
		t1.goto(30,-200)
	
	if(215<x<235 and 165<y<185):
		score+=5
		print ("your scores are %d !" % score)
		t1.goto(30,-200)
	if(score>15):
		print ("You are the Best Player")
		t1.goto(0,0)
		t1.write("Good job,Friend")
		print ("game is going to be ended after 10 seconds")
		time.sleep(10)
		wn.bye()	
	
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
timeout=0
for i in range(timeout,0,-1):
	print (timeout)
	time.sleep(5)
	timeout-=5
wn.exitonclick()