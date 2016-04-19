
import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
d=dict()
d=({1:(0,0),2:(100,0),3:(100,-100),4:(0,-100),5:(0,0)})
def lab7():
       for i in range(1,6):
       	       t1.setpos(d[i])
def main():
      lab7()
if __name__=="__main__":
 	main()

wn.exitonclick()