sel=input("Enter the words: ")
k=dict() 
word=sel 
for c in word: 
    if c not in k: 
        k[c]=1 
    else: 
        k[c]=k[c]+1 
print (k)
import matplotlib 
import matplotlib.pyplot as plt 
plt.bar(range(len(k)),k.values(),align='center') 
plt.xticks(range(len(k)),list(k.keys())) 
plt.show()
wn.exitonclick()