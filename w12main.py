import os
mydir = os.getcwd()


def homework1():
    mydir=os.getcwd()
    filename='python.txt'
    myfilename=os.path.join(mydir, filename)

    try :
        myfile=open(myfilename, 'r')
    except IOError as e:
        print(e)
    contents=myfile.readlines()
    myfile.close()
    for content in contents :
        if content.lower().find('python')!=-1 :
            print(content)

def homework2():
    myfile=open('output.txt', 'w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third line'
    myfile.write(line3)
    myfile.close()

    mydir=os.getcwd()
    filename='output.txt'
    myfilename=os.path.join(mydir,filename)
    print (myfilename)

    try:
        myfile=open(myfilename,'r')

    except IOError as e :
            print ('error')

    contents=myfile.readlines()
    myfile.close()

    for i in contents:
        if (-1 < i.find("line")):
            print(i.upper())

def main():
    homework1()
    homework2()


main()