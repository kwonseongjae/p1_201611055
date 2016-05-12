import turtle
wn=turtle.Screen()
def speech():
    George=list()
    George=[
"President Clinton, distinguished guests and my fellow citizens, the peaceful transfer of authority is rare in history, yet common in our country. With a simple oath, we affirm old traditions and make new beginnings."
"As I begin, I thank President Clinton for his service to our nation."
"And I thank Vice President Gore for a contest conducted with spirit and ended with grace."
"I am honored and humbled to stand here, where so many of America's leaders have come before me, and so many will follow."
"We have a place, all of us, in a long story - a story we continue, but whose end we will not see. It is the story of a new world that became a friend and liberator of the old, a story of a slave-holding society that became a servant of freedom, the story of a power that went into the world to protect but not possess, to defend but not to conquer."
"It is the American story - a story of flawed and fallible people, united across the generations by grand and enduring ideals."
"The grandest of these ideals is an unfolding American promise that everyone belongs, that everyone deserves a chance, that no insignificant person was ever born."
"Americans are called to enact this promise in our lives and in our laws. And though our nation has sometimes halted, and sometimes delayed, we must follow no other course."
"Through much of the last century, America's faith in freedom and democracy was a rock in a raging sea. Now it is a seed upon the wind, taking root in many nations."
"Our democratic faith is more than the creed of our country, it is the inborn hope of our humanity, an ideal we carry but do not own, a trust we bear and pass along. And even after nearly 225 years, we have a long way yet to travel."
"While many of our citizens prosper, others doubt the promise, even the justice, of our own country. The ambitions of some Americans are limited by failing schools and hidden prejudice and the circumstances of their birth. And sometimes our differences run so deep, it seems we share a continent, but not a country."
"We do not accept this, and we will not allow it. Our unity, our union, is the serious work of leaders and citizens in every generation. And this is my solemn pledge: I will work to build a single nation of justice and opportunity."
"I know this is in our reach because we are guided by a power larger than ourselves who creates us equal in His image."
"And we are confident in principles that unite and lead us onward."
"America has never been united by blood or birth or soil. We are bound by ideals that move us beyond our backgrounds, lift us above our interests and teach us what it means to be citizens. Every child must be taught these principles. Every citizen must uphold them. And every immigrant, by embracing these ideals, makes our country more, not less, American."
"Today, we affirm a new commitment to live out our nation's promise through civility, courage, compassion and character."
    ]
    d = dict()
    for sentence in George:
        words=sentence.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
        c=10
    for a in d:
        if d[a]>c:
            print ("George : ",a)
    Obama=list()
    Obama=[
"Hello, this is Senator Barack Obama and today is Thursday, June 8th, 2006.",
"The topic today is net neutrality. ",
"The internet today is an open platform where the demand for websites and services dictates success.",
"You've got barriers to entry that are low and equal for all comers. ",
"And it's because the internet is a neutral platform that I can put on this podcast and transmit it over the internet without having to go through some corporate media middleman.", 
"I can say what I want without censorship. ",
"I don't have to pay a special charge. But the big telephone and cable companies want to change the internet as we know it.",
"They say they want to create high-speed lanes on the internet and strike exclusive contractual arrangements with internet content-providers for access to those high-speed lanes.",
"Those of us who can't pony up the cash for these high-speed connections will be relegated to the slow lanes.",
"Allowing the Bells and cable companies to act as gatekeepers with control over internet access would make the internet like cable.",
"A producer-driven market with barriers to entry for website creators and preferential treatment for specific sites based not on merit, the number of hits, but on relationships with the corporate gatekeeper.",
"If there were four or more competitive providers of broadband service to every home, then cable and telephone companies would not be able to create a bidding war for access to the high-speed lanes.", 
"But here's the problem. More than 99 percent of households get their broadband services from either cable or a telephone company.",
"So here's my view. We can't have a situation in which the corporate duopoly dictates the future of the internet and that's why I'm supporting what is called net neutrality.",
"In the House, the Energy and Commerce Committee and the Judiciary Committee reached different conclusions on network neutrality. ",
"Judiciary Committee members voted to protect net neutrality and commerce voted with the Bells and cable. ",
"That debate is going to hit the House floor this Friday.",
"In the Senate, Senators Snowe and Dorgan are leading the fight for net neutrality and I've joined in that effort. ",
"Senator Inouye, the ranking Democrat of the Commerce Committee, has joined us in this effort as well and he's working with Senator Stevens to put strong network neutrality into any Senate bill that comes before us.",
"There is widespread support among consumer groups, leading academics and the most innovative internet companies, including Google and Yahoo, in favor of net neutrality.",
"And part of the reason for that is companies like Google and Yahoo might never have gotten started had they not been in a position to easily access the internet and do so on the same terms as the big corporate companies that were interested in making money on the internet.",
"I know if you are listening to this podcast that you are going to take an intense interest in this issue as well. ",
"Congress is going to need to hear your voice because the Bell and cable companies are going to be dedicating millions of dollars to defeating network neutrality.", 
"So I'll keep you updated on this important issue and I look forward to talking to you guys again next week. Bye-bye."
    ]
    b= dict()
    for sentence in Obama:
        words=sentence.split()
        for word in words:
            if word in b:
                b[word]+=1
            else:
                b[word]=1
    c=6
    for k in b:
        if b[k]>c:
            print ("Obama : ", k)
def school():
    school=list()
    school=[["Division","Very good","good","Bad","Very bad"],["Class quality",13.1,37.1,8.7,1.5
        ],["Class way",10.6,34.6,13.4,1.9],["Friendship",27.1,40.0,2.9,1.5],["Relation with Teacher",16.2,37.8,6.8,0.8],
       ["School facility",11.4,29.8,14.8,4.9],["School environment",12.2,26.5,14.9,4.4],
        ["Major",13.5,29.7,11.1,2.4],["School life",13.7,37.6,4.1,1.2]]
    school2=school[1:]
    sum=0
    for i in school2:
        sum1=i[1]+i[2]
        sum+=sum1
    sum2=0
    for i in school2:
        sum3=i[3]+i[4]
        sum2+=sum3
    goodAverage=sum/len(school2)
    badAverage=sum2/len(school2)
    
    print ("Good average is "+str(goodAverage))
    print ("Bad average is "+str(badAverage))

def lab11():
    speech()
    school()
def main():
    lab11()
main()
wn.exitonclick()    