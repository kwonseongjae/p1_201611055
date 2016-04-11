def computeBMI():
    w1=input("input your weight: ")
    h1=input("input your height: ")
    weight=float(w1)
    height=float(h1)
    bheight=height/100.
    Bmi=weight/(bheight*bheight)
    if(Bmi<18.5):
        print ("low weight")
    elif(18.5<=Bmi<25):
        print ("normal")
    elif(25<=Bmi<30):
        print ("over weight")
    elif(30<=Bmi):
        print ("obesity")
    else:
        print ("Error")

computeBMI()
def main():
    computeBMI()

wn.exitonclick()