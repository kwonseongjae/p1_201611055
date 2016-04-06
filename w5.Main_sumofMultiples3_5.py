import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def sumofMultiplesof3_5(begin,end):
    sum=0
    for i in range(begin,end):
        if not i%3 or i%5:
                sum=sum+i
    print (sum)
sumofMultiplesof3_5(0,1000)

wn.exitonclick()