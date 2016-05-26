import os
mydir = os.getcwd()


def lab12_1() :
    mydir=os.getcwd()
    filename='python.txt'
    myfilename=os.path.join(mydir, filename)
    try :
        myfile=open(myfilename, 'r')
    except IOError as e:
        print (e)
    contents=myfile.readlines()
    myfile.close()
    for content in contents :
        if content.lower().find('python')!=-1 :
            print(content)

def lab12_2():
 
    myfile=open('output.txt', 'w')
    line1='first line\n'	
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third'
    myfile.write(line3)
    myfile.close()

    mydir=os.getcwd()
    filename='output.txt'
    myfilename=os.path.join(mydir,filename)
    print (myfilename)


    try:
        myfile=open(myfilename,'r')

    except IOError as e :
        print ('erorr')

    contents=myfile.readlines()
    myfile.close()

    for i in contents:
        if (-1 < i.find("line")):
            print (i.upper())

def main():
    lab12_1()
    lab12_2()


main()