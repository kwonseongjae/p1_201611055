def lab11():
    import turtle    
    wn=turtle.Screen()
    t1=turtle.Turtle()
    wn.bgpic("myMaze.gif")
    def k1():
        t1.fd(50)
    def k2():
        t1.bk(50)
    def k3():
        t1.rt(90)
    def k4():
        t1.lt(90)
    def mousegoto(x,y):
        t1.setpos(x,y)
    def addKeys():
        wn.onkey(k1,"Up")
        wn.onkey(k2,"Down")
        wn.onkey(k3,"Right")
        wn.onkey(k4,"Left")
    def addMouse():
        wn.onclick(mousegoto)
def main():
    lab11()
    wn.listen()
    turtle.mainloop()
main()
wn.exitonclick()