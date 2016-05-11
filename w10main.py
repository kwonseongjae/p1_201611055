import turtle
wn=turtle.Screen()
def allData():
    alldata= [ 
    ["Coffee","Water","Milk","Icecream"], 
    ["Espresso","No","No","No"], 
    ["Long Black","Yes","No","No"], 
    ["Flat White","No","Yes","No"], 
    ["Cappuccino","No","Yes","No"], 
    ["Affogatto","No","No","Yes"] 
    ] 
    data= alldata[1:] 
    sum=0 
    for i in data: 
        if i[2].upper()=='YES': 
            sum=sum+1 
    print ("percent:",(float(sum)/float(len(data)))*100,"%")
def score():
    score= [
        ["English",100,"Math",200],
        ["Englsih",200,"Math",200],
        ["English",100,"Math",300]
    ]
    math=0
    for i in score:
        math=i[3]+math
    print ("Math everage:",float(math)/float(len(score)))
    english=0
    for i in score:
        english=i[1]+english
    print ("English everage:",float(english)/float(len(score)))
def Iyrics():
    Iyrics =[
    "when I find myself in times of trouble",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",
    "and in my hour of darkness",
    "she is standing right in front of me",
    "speaking words of wisdom let it be",

    "let it be let it be",
    "let it be let it be",
    "whisper words of wisdom let it be",

    "and when the broken-hearted people",
    "living in the world agree",
    "there will be an answer let it be",
    "for though they may be parted",
    "there is still a chance that they will see",
    "there will be an answer let it be",

    "let it be let it be",
    "let it be let it be",
    "yeah there will be an answer let it be",
    "let it be let it be",
    "let it be let it be",
    "whisper words of wisdom let it be",

    "let it be let it be",
    "ah let it be yeah let it be",
    "whisper words of wisdom let it be",

    "and when the night is cloudy",
    "there is still a light that shines on me",
    "shine on until tomorrow let it be",
    "i wake up to the sound of music",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",

    "let it be let it be",
    "let it be yeah let it be",
    "oh there will be an answer let it be",
    "let it be let it be",
    "let it be yeah let it be",
    "whisper words of wisdom let it be"
    ]
    for i in range(0,len(Iyrics)):
        print  (Iyrics[i].split())

    d=dict()
    for i in range(0,len(Iyrics)):
        for c in Iyrics[i].split():
            if c in d:
                d[c]=d[c]+1
                print (d)
            else:
                d[c]=1
    for c in d:
        if d[c]>=20:
            print (c)
def lab10():
    allData()
    score()
    Iyrics()
def main():
    lab10()
if __name__=="__main__":
    main()

wn.exitonclick()