﻿import turtle
wn=turtle.Screen()
me=set(['TV','phone','camera','fridger','mixer','audio','cd player','light','computer','notebook','recoder'])
friend=set(['coffee machine','radio','camera','running machine','ramp','computer','notebook','recoder'])
print ("my machine is :")
print (me)
print ("friend machine is :")
print (friend)
all= me.union(friend)
both=me&friend
print ("allmachine is: ")
print (all)
print ("both machine is: ")
print (both)
print ("only my machine is: ")
print (me-both)
print ("only myfriend's machine is: ")
print (friend-both)
wn.exitonclick()