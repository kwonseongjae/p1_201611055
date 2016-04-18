import  turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def drawSquareAtSave(size,pos):
    tracks=list()
    t1.pu()
    t1.goto(pos)
    t1.pd()
    for i in range(0,4):
        t1.fd(size)
        t1.rt(90)
        tracks.append(t1.pos())
    return tracks
def lab7():
    mytracks=drawSquareAtSave(70,(-30,50))
    print (mytracks)
def main():
    lab7()
main()
wn.exitonclick()