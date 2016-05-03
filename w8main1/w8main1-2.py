import turtle
wn=turtle.Screen()
word = '7 Hongji'   
k=dict()  
k['str']=0  
k['int']=0  
for i in word:  
    if i.isalpha():  
        k['str']=k['str']+1  
    elif i.isdigit:  
        k['int']=k['int']+1  
print (k) 

import matplotlib  
import matplotlib.pyplot as plt 

wn.exitonclick()