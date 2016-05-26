import time
def lab12_1():
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    add='[khb edited {0}]'.format(time.strftime('%Y.%m.%d , %H:%M:%S'))
    for line in fin:
        words=line.split()
        fout.write(add)
        fout.write('\t')
        for word in words:
            if word == 'line':
                fout.write('\t')    
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
def lab12_2():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('outputHB.txt','w')
    for i in data:
        toPrint="{0}\t".format(i)
    #print toPrint,
    fout.write(toPrint)
    if i%2==0:
            fout.write('\n')
    fout.close()

def main():
    lab12_1()
    lab12_2()

if __name__=="__main__":
    main()

sel1=input()