import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 

def lab6(): 
    year=input("input year{2000~}: ") 
    y1=int(year) 
    if(y1%4==0): 
        print ("This year is leap year") 
    else: 
        print ("This year is not leap year") 

def main(): 
    lab6() 

main() 
wn.exitonclick()