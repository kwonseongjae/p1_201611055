import turtle 
wn=turtle.Screen() 
t1=turtle.Turtle() 
marks=input("input 0~100 :")   
def computeGrade(marks):   
    if 90<=float(marks)<=100:   
             grade="A" 
    elif 80<=float(marks)<90:   
             grade="B"   
    elif 70<=float(marks)<80:   
             grade="C"  
    elif 60<=float(marks)<70:   
             grade="D"   
    else:   
             grade="F"  
    return grade   
result=computeGrade(marks)   
print ("my grade is %s" %result)   
wn.exitonclick()