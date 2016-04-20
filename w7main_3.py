def saveTracks():
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()

    t1.speed(1)
    t1.pu()
    mytracks=list()
    t1.goto(-370,370)
    t1.rt(90)
    t1.pd()

    mytracks.append(t1.pos())
    t1.pencolor("Red")

    t1.fd(300)
    t1.lt(90)

    mytracks.append(t1.pos())

    t1.fd(400)
    t1.lt(90)

    mytracks.append(t1.pos())

    t1.fd(150)
    t1.rt(90)

    mytracks.append(t1.pos())

    t1.fd(200)
    t1.rt(90)

    mytracks.append(t1.pos())

    t1.fd(300)
    t1.fd(100)
    t1.lt(90)

    mytracks.append(t1.pos())

    t1.fd(200)

    mytracks.append(t1.pos())
    return mytracks
    for i in range(0,len(mytracks)):
        t1.goto(mytracks[i])
        

def replayTracks(mytracks):
    for i in range(0,len(mytracks)):
        print(mytracks[i])
def lab7():
    mytracks=saveTracks()
    replayTracks(mytracks)
def main():
    lab7()
main()
if __name__=="main":
    main()
wn.exitonclick()


